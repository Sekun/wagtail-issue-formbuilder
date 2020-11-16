from django.db import models
from wagtail.core.models import Page
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from wagtail.admin.edit_handlers import InlinePanel
from modelcluster.fields import ParentalKey


class HomePage(Page):
    pass


class BuilderPage(AbstractForm):
    content_panels = Page.content_panels + [
        InlinePanel("form_fields", label="Form fields"),
    ]


class CustomField(AbstractFormField):
    page = ParentalKey(
        BuilderPage, on_delete=models.CASCADE, related_name="form_fields"
    )

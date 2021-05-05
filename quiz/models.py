from django.db import models
from django.utils.translation import ugettext as _


class Category(models.Model):

    name = models.CharField(_("name"), max_length=250)
    is_active = models.BooleanField(_("Is Active"), default=True)
    created_at = models.DateTimeField(
        _("Created"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        _("Updated"), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class SubCategory(models.Model):

    category = models.ForeignKey(Category, related_name='subcategory', verbose_name=_(
        "Category"), on_delete=models.PROTECT)
    name = models.CharField(_("name"), max_length=250)
    is_active = models.BooleanField(_("Is Active"), default=True)
    created_at = models.DateTimeField(
        _("Created"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        _("Updated"), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class Quiz(models.Model):

    subcategory = models.ForeignKey(SubCategory, related_name="quiz", verbose_name=_("SubCategory"), null=True, on_delete=models.PROTECT)

    name = models.CharField(_("name"), max_length=250)
    created_by = models.CharField(_("Created By"), max_length=250, null=True)
    is_active = models.BooleanField(_("Is Active"), default=True)
    expires_at = models.DateField(_("Expires At"))
    created_at = models.DateTimeField(
        _("Created"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        _("Updated"), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name
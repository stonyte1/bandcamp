from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(_("name"), max_length=20)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})


class SubCategory(models.Model):
    name = models.CharField(_("name"), max_length=50)
    category = models.ForeignKey(
        Category, 
        verbose_name=_("category"), 
        on_delete=models.CASCADE,
        related_name='subcategories')

    class Meta:
        verbose_name = _("sub category")
        verbose_name_plural = _("sub categories")

    def __str__(self):
        return f"{self.name}/{self.category}"

    def get_absolute_url(self):
        return reverse("subcategory_detail", kwargs={"pk": self.pk})


class Merch(models.Model):
    name = models.CharField(_("name"), max_length=100)
    category = models.ForeignKey(
        SubCategory, 
        verbose_name=_("category"), 
        on_delete=models.CASCADE,
        related_name="merches"
    )
    album = models.ForeignKey(
        "music.Album", 
        verbose_name=_("album"), 
        on_delete=models.CASCADE,
        related_name="merches",
        null=True,
        blank=True
    )
    price = models.FloatField(_("price"))
    quantity = models.IntegerField(_("quantity"))
    picture = models.ImageField(_("picture"), upload_to='merch/')
    description = models.TextField(_("description"))

    class Meta:
        verbose_name = _("merch")
        verbose_name_plural = _("merches")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("merch_detail", kwargs={"pk": self.pk})

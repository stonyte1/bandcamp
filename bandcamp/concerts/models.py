from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class ConcertCity(models.Model):
    name = models.CharField(_("name"), max_length=250)
    
    class Meta:
        verbose_name = _("concert city")
        verbose_name_plural = _("concert citys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("concertcity_detail", kwargs={"pk": self.pk})


class ConcertVenue(models.Model):
    name = models.CharField(_("name"), max_length=250)
    city = models.ForeignKey(
        ConcertCity,
        verbose_name=_("city"), 
        on_delete=models.CASCADE,
        related_name='concert_venues',
        null=True, blank=True
    )
    
    class Meta:
        verbose_name = _("concert venue")
        verbose_name_plural = _("concert venues")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("concertvenue_detail", kwargs={"pk": self.pk})


class Concert(models.Model):
    city = models.ForeignKey(
        ConcertCity,
        verbose_name=_("city"), 
        on_delete=models.CASCADE,
        related_name='concerts'
    )
    venue = models.ForeignKey(
        ConcertVenue, 
        verbose_name=_("venue"), 
        on_delete=models.CASCADE,
        related_name='concerts',
    )
    date= models.DateField(_("date"), default=None)
    STATUS_CHOICES = (
        (0, _('TBA')),
        (1, _('Free')),
        (2, _('In Stock')),
        (3, _('Sold out')),
        (4, _('Cancelled'))
    )
    ticket_status = models.PositiveBigIntegerField(
        _("ticket status"),
        choices=STATUS_CHOICES,
        default=0,
        db_index=True
    )
    link = models.TextField(_("link"), max_length=500)
    visible = models.BooleanField(_("visible"), default=False)

    class Meta:
        verbose_name = _("concert")
        verbose_name_plural = _("concerts")

    def __str__(self):
        return f'{self.date}'

    def get_absolute_url(self):
        return reverse("conert_detail", kwargs={"pk": self.pk})


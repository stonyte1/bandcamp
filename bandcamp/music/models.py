from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Song(models.Model):
    title = models.CharField(_("title"), max_length=250)
    audio = models.FileField(_("audio"), upload_to='music/', blank=True, null=True)
    duration = models.CharField(_("duration"), max_length=5)
    
    class Meta:
        verbose_name = _("song")
        verbose_name_plural = _("songs")

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("song_detail", kwargs={"pk": self.pk})


class Album(models.Model):
    title = models.CharField(_("title"), max_length=250)
    cover = models.ImageField(_("cover"), upload_to='music/')
    song = models.ForeignKey(
        Song, 
        verbose_name=_("song"), 
        on_delete=models.CASCADE,
        related_name='albums'
        )
    release_date = models.DateField(_("release_"), default=None)
    summary = models.TextField(_("summary"), blank=True, null=True)
    TYPE = (
        (0, 'None'),
        (1, 'Single'),
        (2, 'EP'),
        (3, 'Album')
    )
    realese_type = models.CharField(
        _("realese_type"), 
        max_length=1,
        choices=TYPE,
        default=0
        )
    
    class Meta:
        verbose_name = _("album")
        verbose_name_plural = _("albums")

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("album_detail", kwargs={"pk": self.pk})

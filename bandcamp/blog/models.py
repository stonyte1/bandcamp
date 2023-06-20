from django.db import models
from  embed_video.fields  import  EmbedVideoField
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(_("title"), max_length=50)
    summary = models.TextField(_("summary"), null=True, blank=True)
    content = models.TextField(_("content"))
    video = EmbedVideoField(_("video"), null=True, blank=True)
    picture = models.ImageField(_("picture"),null=True, blank=True, upload_to='pictures/')
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("blog post")
        verbose_name_plural = _("blog posts")

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("blogpost_detail", kwargs={"pk": self.pk})

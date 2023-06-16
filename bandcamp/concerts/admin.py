from django.contrib import admin
from . import models


admin.site.register(models.ConcertCity)
admin.site.register(models.ConcertVenue)
admin.site.register(models.Concert)

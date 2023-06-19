from django.contrib import admin
from . import models

class ConcertsAdmin(admin.ModelAdmin):
    list_display = ('date', 'city', 'venue', 'ticket_status', 'link', 'is_visible')
    list_editable = ('ticket_status',) 

    def is_visible(self, obj):
        return obj.visible
    
    is_visible.boolean = True

admin.site.register(models.ConcertCity)
admin.site.register(models.ConcertVenue)
admin.site.register(models.Concert, ConcertsAdmin)

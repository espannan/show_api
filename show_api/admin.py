# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Show
from .models import ShowVenue


class ShowAdmin(admin.ModelAdmin):
    model = Show
    exclude = ('removed_at',)


admin.site.register(ShowVenue)
admin.site.register(Show, ShowAdmin)

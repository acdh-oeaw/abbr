from django.contrib import admin
from .models import *


class AbbreviationAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'orth', 'expanded', 'lemma', 'pos'
    )
    list_filter = ['pos']
    search_fields = ['orth', 'expanded', 'lemma']


admin.site.register(Abbreviation, AbbreviationAdmin)

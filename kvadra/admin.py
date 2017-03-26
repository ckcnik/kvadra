from .models import Text
from django.contrib import admin


class TextAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')

admin.site.register(Text, TextAdmin)

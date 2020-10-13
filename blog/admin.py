from django.contrib import admin
from django.utils.html import format_html

from .models import *


class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'contenido', 'autor', 'f_pub')
    readonly_fields = ['f_pub']

admin.site.register(Categoria)
admin.site.register(Publicacion, PublicacionAdmin)
from distutils.command import register
from django.contrib import admin

from .models import Post


admin.site.register(Post)

admin.site.site_header = "Ine API"
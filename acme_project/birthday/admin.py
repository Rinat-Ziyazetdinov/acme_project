from django.contrib import admin
from .models import Tag

# Регистрируем модель в админке:
admin.site.register(Tag)

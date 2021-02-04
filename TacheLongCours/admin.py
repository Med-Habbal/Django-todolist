from django.contrib import admin
from .models import Tache, Category, TypeDeTache
# Register your models here.

admin.site.register(Tache)
admin.site.register(Category)
admin.site.register(TypeDeTache)
from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Article, Category


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article)
admin.site.unregister(Group)

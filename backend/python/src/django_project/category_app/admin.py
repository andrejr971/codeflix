from django.contrib import admin

from src.django_project.category_app.models import Category


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)

from django.contrib import admin

from apps.categories.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    list_filter = ('parent', )


admin.site.register(Category, CategoryAdmin)

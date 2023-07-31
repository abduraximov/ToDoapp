from django.contrib import admin
from apps.api.todo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Todo, TodoAdmin)

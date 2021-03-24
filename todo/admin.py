from django.contrib import admin
from .models import ToDo

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ('text', 'added_date', 'priority', 'status', 'user')


admin.site.register(ToDo, TodoAdmin)
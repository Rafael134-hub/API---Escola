from django.contrib import admin
from .models import *

# Register your models here.
class datTeacher(admin.ModelAdmin):
    list_display = ('id', 'ni', 'name', 'email', 'phone', 'ocupacao')
    list_display_links = ('id',)
    search_fields = ('id', 'ni', 'name', 'email', 'phone', 'ocupacao',)
    list_per_page = 15

admin.site.register(Teacher, datTeacher)
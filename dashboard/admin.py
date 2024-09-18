from django.contrib import admin
from .models import *


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass
@admin.register(Homework)
class HomworkAdmin(admin.ModelAdmin):
    pass
@admin.register(Todo)
class Todo(admin.ModelAdmin):
    pass
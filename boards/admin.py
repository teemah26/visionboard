from django.contrib import admin

# Register your models here.
from .models import Board, Item
from django.contrib import admin

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at")

@admin.register(Item)
class BoardItemAdmin(admin.ModelAdmin):
    list_display = ("board", "caption", "added_at")


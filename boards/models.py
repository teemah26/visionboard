

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="boards")
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="items")
    image = models.ImageField(upload_to="board_items/")
    caption = models.CharField(max_length=255, blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.title
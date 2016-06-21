from django.db import models

class Room(models.Model):
    label = models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    author = models.ForeignKey('teams.User', related_name='messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

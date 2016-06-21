from django.db import models

from teams.models import User


class Entry(models.Model):
	title = models.CharField(max_length=140)
	content = models.TextField(default=None)
	author = models.ForeignKey(User)
	rating = models.PositiveSmallIntegerField(default=1)
	pub_date = models.DateTimeField(auto_now_add=True)
	mod_date = models.DateTimeField(auto_now=True)

	def __str__(self):
	    return self.title

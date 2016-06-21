from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name


class Question(models.Model):
	author = models.ForeignKey('teams.User', related_name='asked')
	targets = models.ManyToManyField('teams.User', related_name='recived')
	category = models.ForeignKey(Category, null=True)

	title = models.CharField(max_length=140)
	specifics = models.TextField(default=None)
	answered = models.BooleanField(default=False)
	pub_date = models.DateTimeField(auto_now_add=True)
	mod_date = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.title


class Answer(models.Model):
	author = models.ForeignKey('teams.User')
	question = models.ForeignKey(Question)

	text = models.TextField(default=None)
	pub_date = models.DateTimeField(auto_now_add=True)
	mod_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'Answer to: {}'.format(self.question.title)

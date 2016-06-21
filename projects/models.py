from django.db import models
from model_utils import Choices
from teams.models import User


class Project(models.Model):
    name = models.CharField(max_length=64)
    team = models.ManyToManyField(User, related_name='projects')
    current_sprint = models.OneToOneField('Sprint', related_name='active_in',
                                          null=True, blank=True)
    def __str__(self):
        return self.name


class Sprint(models.Model):
    number = models.PositiveSmallIntegerField(null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    project = models.ForeignKey(Project, related_name='sprints')
    def __str__(self):
        return str(self.number)+"-"+str(self.project)


class Issue(models.Model):
    summary = models.CharField(max_length=128)
    description = models.TextField()

    STATUS = Choices(('to_do', 'TO DO'), ('in_progress', 'In progress'), 'Fixed')
    status = models.CharField(choices=STATUS, max_length=20)

    sprint = models.ForeignKey(Sprint, related_name='issues', null=True,
                               blank=True)
    assignee = models.ForeignKey(User, related_name='issues', null=True,
                                 blank=True)
    completion_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.summary

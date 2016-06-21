from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils import timezone
from projects.models import Issue, Project


@login_required
def tasks(request, pk):
    projects = request.user.projects.all()
    current_sprint = Project.objects.get(pk=pk).current_sprint

    if current_sprint:
        to_do = current_sprint.issues.filter(assignee=request.user,
                                             status='to_do')
        in_progress = current_sprint.issues.filter(assignee=request.user,
                                                   status='in_progress')
        done = current_sprint.issues.filter(assignee=request.user, status='Fixed')

        all_to_do = current_sprint.issues.filter(status='to_do')
        all_in_progress = current_sprint.issues.filter(status='in_progress')
        all_done = current_sprint.issues.filter(status='Fixed')

        return render(request, 'projects/tasks.html',
                      {'projects': request.user.projects.all(),
                       'current_sprint': current_sprint,
                       'to_do': to_do,
                       'in_progress': in_progress,
                       'done': done,
                       'all_to_do': all_to_do,
                       'all_in_progress': all_in_progress,
                       'all_done': all_done})
    else:
        return render(request, 'projects/tasks.html',
                      {'projects': request.user.projects.all(),
                       'current_sprint': current_sprint})

@login_required
def pick(request):
    return render(request, 'projects/pick.html',
                  {'projects': request.user.projects.all()})


@login_required
def start_task(request, pk):
    task = Issue.objects.get(pk=pk)
    task.status = 'in_progress'
    task.save()
    return redirect('projects:tasks', pk=task.sprint.project.id)


@login_required
def resolve_task(request, pk):
    task = Issue.objects.get(pk=pk)
    task.status = 'Fixed'
    task.completion_date = timezone.now()
    task.save()
    return redirect('projects:tasks', pk=task.sprint.project.id)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
import collections
from projects.models import Issue, Project

# Create your views here.

@login_required
def dash(request):
    projects = request.user.projects.all()
    all_current = []
    burn = []
    burnDict = {}
    for proj in projects:
        burnDict = {}
        todo = proj.current_sprint.issues.filter(status='to_do').count()
        inp =  proj.current_sprint.issues.filter(status='in_progress').count()
        fixed = proj.current_sprint.issues.filter(status='Fixed')
        for x in fixed:
            dateString = x.completion_date.strftime("%d %b %Y")
            if dateString not in burn:
                burn.append(dateString)
                burnDict[dateString] = todo+inp
            if burnDict[dateString] >0:
                burnDict[dateString] = burnDict[dateString]-1
        burn.sort()
        burnDict = list(burnDict.values())
        all_current.append({'project':proj.name, 'values':[todo,inp,len(fixed)],'id':proj.id,
                            'fixed_dates': burn,'count_dates':burnDict})


    return render(request, 'scrum/index.html',{'all_current':all_current})

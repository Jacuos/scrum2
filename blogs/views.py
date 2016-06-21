from django.shortcuts import render, redirect
from django.db.models import F
from django.http import HttpResponseRedirect

from .models import Entry
from teams.models import User


def entries(request, page=1):
	page = int(page)
	entries_latest = Entry.objects.reverse()[(page-1)*9:page*9]
	entries_top = Entry.objects.order_by('rating')[(page-1)*9:page*9]
	pages = Entry.objects.count() // 9 + 1
	subscriptions = request.user.subscriptions.all()
	entries_subscribed = Entry.objects.filter(author__in=subscriptions)
	return render(request, 'blogs/entries.html', {
		'entries_latest': entries_latest,
		'entries_top': entries_top,
		'entires_subscribed': entries_subscribed,
		'pages': range(1, pages+1),
	})


def write(request):
	if request.method == 'POST':
		title = request.POST['title']
		content = request.POST['content']
		author = request.user
		entry = Entry(title=title, content=content, author=author)
		entry.save()
		return redirect('blogs:entries')
	return render(request, 'blogs/write.html')


def remove(request, entry_id):
	request.user.entry_set.get(id=entry_id).delete()
	return redirect('blogs:entries')


def entry(request, entry_id):
	entry = Entry.objects.get(id=entry_id)
	return render(request, 'blogs/entry.html', {'entry': entry })


def subscribe(request, entry_id):
	user = Entry.objects.get(id=entry_id).author
	request.user.subscriptions.add(user)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def like(request, entry_id):
	if not request.user.liked.filter(id=entry_id).exists():
		entry = Entry.objects.get(id=entry_id)
		entry.rating = F('rating') + 1
		entry.save()
		request.user.liked.add(entry)
	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

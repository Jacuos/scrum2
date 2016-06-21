from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib import messages

from .models import Category, Question, Answer


def questions(request):
	return render(request, 'qanda/questions.html', {'categories': Category.objects.all()})


def ask(request):
	if request.method == 'POST':
		title = request.POST['title']
		specifics = request.POST['specifics']
		author = request.user
		category = Category.objects.get(id=int(request.POST['category']))
		question = Question(title=title, specifics=specifics, author=author, category=category)
		question.save()
		targets = category.user_set.all()
		question.targets.add(*list(targets))
		return redirect('qanda:questions')
	return render(request, 'qanda/ask.html', {'categories': Category.objects.all()})


def ignore(request, question_id):
	request.user.recived.remove(question_id)
	return redirect('qanda:questions')


def archive(request, question_id):
	question = request.user.asked.get(id=question_id)
	question.active = False
	question.targets.clear()
	question.save()
	return redirect('qanda:questions')


def remove(request, question_id):
	request.user.asked.get(id=question_id).delete()
	return redirect('qanda:questions')


def answer(request, question_id):
	question = request.user.recived.get(id=question_id)
	if request.method == 'POST':
		author = request.user
		text = request.POST['text']
		answer = Answer(author=author, text=text, question=question)
		answer.save()
		request.user.recived.remove(question)
		return redirect('qanda:questions')
	return render(request, 'qanda/answer.html', {'question': question})


def details(request, question_id):
	question = Question.objects.get(id=question_id)
	return render(request, 'qanda/details.html', {'question': question})


def search(request):
	if request.method == 'POST':
		query = request.POST['search']
		title_match = Question.objects.filter(title__contains=query)
		specifics_match = Question.objects.filter(specifics__icontains=query)
		results = title_match | specifics_match
		return render(request, 'qanda/search.html', {'results': results})
	return redirect('qanda:questions')


def settings(request):
	if request.method == 'POST':
		checks = request.POST.getlist('checks')
		print(checks)
		for category in Category.objects.all():
			if category.name in checks:
				request.user.categories.add(category)
			else:
				request.user.categories.remove(category)
		messages.info(request, 'Categories modified.')
		return redirect('qanda:settings')
	return render(request, 'qanda/settings.html', {'categories': Category.objects.all()})

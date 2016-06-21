import random
import string

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .models import Room


@login_required
def start_room(request):
    if request.method == 'POST':
        new_room = Room.objects.create(label=request.POST['label'])
        return redirect(reverse('chat:pick_room', args=[new_room.label]))
    else:
        return render(request, 'chat/start.html', {
            'rooms': Room.objects.all()})

@login_required
def pick_room(request, label):
    current_room = Room.objects.get(label=label)
    return render(request, 'chat/room.html', {
        'rooms': Room.objects.all(),
        'current_room': current_room,
        'room_messages': reversed(
            current_room.messages.order_by('-timestamp')[:50])})

import json

from django.http import HttpResponse

from channels import Group
from channels.handler import AsgiHandler
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http
from .models import Room, Message


@channel_session
@channel_session_user_from_http
def connect(message):
    try:
        label = message['path'].strip('/').split('/')[-1]
        room = Room.objects.get(label=label)
    except Room.DoesNotExist:
        return

    Group(label).add(message.reply_channel)
    message.channel_session['room'] = room.label

@channel_session
@channel_session_user
def receive(message):
    label = message.channel_session['room']
    room = Room.objects.get(label=label)

    content = Message.objects.create(message=message['text'],
        author_id=message.user.id, room=room)

    content_json = json.dumps({
        'message': content.message,
        'author': content.author.email
    })

    Group(label).send({'text': content_json})

@channel_session
def disconnect(message):
    try:
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
        Group(label).discard(message.reply_channel)
    except (KeyError, Room.DoesNotExist):
        pass

def hold(message):
    Group('w8').add(message.reply_channel)

def relase(request):
    response = HttpResponse('ok')

    for chunk in AsgiHandler.encode_response(response):
        Group('w8').send(chunk)

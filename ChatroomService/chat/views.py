from django.shortcuts import render
from django.contrib.auth.models import User
from chat.models import ChatModel


def index(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'index.html', context={'users': users})


def chatPage(request):
    users = User.objects.exclude(username=request.user.username)

    return render(request, 'main_chat.html',
                  context={'users': users})

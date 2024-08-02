from django.shortcuts import render


def select_chat_view(request, *args, **kwargs):
  return render(request, 'chat/select_chat.html')
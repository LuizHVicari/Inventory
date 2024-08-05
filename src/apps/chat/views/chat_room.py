from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from loguru import logger

from apps.chat.models import Chat, Message


@login_required
def chat_room_view(request, room_name, *args, **kwargs):
    user = request.user

    # avoids not authorized users to access to room
    if user.username != room_name and not user.is_staff:
        messages.warning(request, 'Essa sala não é permitida para você')
        return redirect('list_items')
    try:
        chat = Chat.objects.get(user__username=room_name)
    except Chat.DoesNotExist:
        messages.warning(request, 'Essa sala não existe')
        return redirect('select-chat-room')
    chat_messages = Message.objects.filter(chat=chat).order_by('created_at')

    context = {
        'room_name': room_name,
        'chat_messages': chat_messages
    }

    return render(request, 'chat/chat_room.html', context)

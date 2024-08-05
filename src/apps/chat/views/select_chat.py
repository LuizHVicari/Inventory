from django.shortcuts import render, redirect
from django.contrib import messages
from loguru import logger


def select_chat_view(request, *args, **kwargs):
    if request.user.is_staff:
        return render(request, 'chat/select_chat.html')
    else:
        messages.warning(request, 'Não é permitido buscar conversas')
        logger.warning(f'O usuário {request.user} tentou buscar uma sala')
        return redirect('list_items')

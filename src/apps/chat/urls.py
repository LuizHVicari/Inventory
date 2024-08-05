from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import select_chat_view, chat_room_view


urlpatterns = [
  path('', select_chat_view, name='select-chat-room'),
  path('<str:room_name>/', chat_room_view, name='chat-room')
]

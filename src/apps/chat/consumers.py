import json
from channels.generic.websocket import AsyncWebsocketConsumer
from loguru import logger
from asgiref import sync
from channels.db import database_sync_to_async
from channels.auth import login
from datetime import timedelta
from django.utils.timezone import now
from decouple import config

from .models import Chat, Message


CHAT_MESSAGES_RATE_LIMIT = config('CHAT_MESSAGES_RATE_LIMIT', cast=int, default=10)
CHAT_MESSAGES_MAX_LENGTH = config('CHAT_MESSAGES_MAX_LENGTH', cast=int, default=200)


class ChatConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    self.room_name = self.scope['url_route']['kwargs']['room_name']
    self.room_group_name = f"chat_{self.room_name}"

    self.user = self.scope['user']
    logger.info(f'O usuário {self.user} se conectou ao chat')

    await self.channel_layer.group_add(self.room_group_name, self.channel_name)
    await self.accept()


  async def disconnect(self, code):
    await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

  
  async def receive(self, text_data):
    total_messages = await self.user_last_messages_count() 
    message_sender = self.scope['user']
    if total_messages >= CHAT_MESSAGES_RATE_LIMIT:
      logger.warning(f'O usuário {message_sender} está enviando muitas mensagens')
      return 
    
    text_data_json = json.loads(text_data)
    message = text_data_json['message']

    if len(message) > CHAT_MESSAGES_MAX_LENGTH:
      return
  
    
    await self.save_message(message)

    await self.channel_layer.group_send(
      self.room_group_name,
      {
        'type': 'chat.message',
        'message': message,
        'message_sender': str(message_sender)
      }
    )


  async def chat_message(self, event):
    message = event['message']
    message_sender = event['message_sender']
    await self.send(text_data=json.dumps({'message': message, 'message_sender': message_sender}))

  
  @database_sync_to_async
  def save_message(self, message):
    chat = Chat.objects.get(user__username__iexact=self.room_name.upper())
    message = Message(
      sender = self.user,
      message = message,
      chat = chat
    )
    message.full_clean()
    message.save()

  
  @database_sync_to_async
  def user_last_messages_count(self):
    return Message.objects.filter(sender=self.user, created_at__gte=now() - timedelta(minutes=1)).count()
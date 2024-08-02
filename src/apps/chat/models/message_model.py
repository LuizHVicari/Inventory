from django.db import models
from django.contrib.auth.models import User

from .chat_model import Chat



class Message(models.Model):
  message = models.TextField(verbose_name='mensagem')
  sender = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='remetente', related_name='message_sender')
  chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='conversa')

  created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')

  
  class Meta:
    verbose_name = 'Mensagem'
    verbose_name_plural = 'Mensagens'

  
  def __str__(self):
    return f'{self.sender} -> {self.chat}: {self.message}'
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save



class Chat(models.Model):
  user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='usuário')

  created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')


  class Meta:
    verbose_name = 'Conversa'
    verbose_name_plural = 'Conversas'

  
  def __str__(self):
    return self.user.username
  

@receiver(post_save, sender=User)
def create_user_chat_on_user_creation(sender, instance=None, created=False, *args, **kwargs):
  if created:
    chat = Chat(
      user = instance
    )
    chat.full_clean()
    chat.save()
  else:
    try:
      chat = Chat.objects.get(user=instance)
    except Chat.DoesNotExist:
      chat = Chat(
      user = instance
    )
    chat.full_clean()
    chat.save()
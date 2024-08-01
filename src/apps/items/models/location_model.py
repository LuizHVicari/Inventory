from django.db import models

from .room_model import Room

class Location(models.Model):
  name = models.CharField(max_length=50, verbose_name='nome')
  description = models.TextField(blank=True, null=True, verbose_name='descrição')
  room = models.ForeignKey(Room, null=True, blank=True, on_delete=models.PROTECT, verbose_name='sala')  

  created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')


  class Meta:
    verbose_name = 'Lugar'
    verbose_name_plural = 'Lugares'

  
  def __str__(self):
    return self.name
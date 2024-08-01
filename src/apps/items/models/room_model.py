from django.db import models

from .building_model import Building


class Room(models.Model):
  name = models.CharField(max_length=5, verbose_name='nome')
  block = models.ForeignKey(Building, on_delete=models.PROTECT, verbose_name='bloco')

  created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')

  
  class Meta:
    verbose_name = 'Sala'
    verbose_name_plural = 'Salas'

  
  def __str__(self):
    return self.name


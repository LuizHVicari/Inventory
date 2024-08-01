from django.db import models
from django.core.validators import MinValueValidator

from .location_model import Location


class Item(models.Model):
  name = models.CharField(max_length=50, verbose_name='nome')
  description = models.TextField(verbose_name='descrição', blank=True, null=True)
  quantity = models.IntegerField(validators=[MinValueValidator(1)], verbose_name='quantidade')
  quantity_avaliable = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='quantidade disponível')
  patrimony_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='número de patrimônio', unique=True)
  location = models.ManyToManyField(Location, related_name='item', verbose_name='lugar')

  created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')


  class Meta:
    verbose_name = 'Item'
    verbose_name_plural = 'Itens'

  
  def __str__(self):
    return self.name
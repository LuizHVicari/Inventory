from django.db import models


class Building(models.Model):
  name = models.CharField(max_length=10, verbose_name='nome')

  created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')

  
  class Meta:
    verbose_name = 'Bloco'
    verbose_name_plural = 'Blocos'


  def __str__(self):
    return self.name
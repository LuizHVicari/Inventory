from django.db import models


class Course(models.Model):
  name = models.CharField(max_length=50)

  created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')

  class Meta:
    verbose_name = 'Curso'
    verbose_name_plural = 'Cursos'

  
  def __str__(self):
    return self.name
  
from django.db import models

from .course_model import Course


class Department(models.Model):
  name = models.CharField(max_length=50, verbose_name='nome')
  acronym = models.CharField(max_length=6, verbose_name='sigla')

  courses = models.ManyToManyField(Course, related_name='departments', verbose_name='cursos')

  created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')


  class Meta:
    verbose_name = 'Departamento'
    verbose_name_plural = 'Departamentos'

  
  def __str__(self):
    return self.name
from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from .department_model import Department
from .course_model import Course


def validate_siape(value: str):
  if not value.isnumeric():
    raise ValidationError('O registro no SIAPE deve ser numérico')

class Professor(models.Model):
  name = models.CharField(max_length=50, verbose_name='nome')
  department = models.ForeignKey(Department, on_delete=models.PROTECT, verbose_name='departamento')
  siape = models.CharField(max_length=8, validators=[MinLengthValidator(7), validate_siape], verbose_name='Sistema Integrado de Administração de Pessoal', unique=True)
  courses = models.ManyToManyField(Course, verbose_name='cursos', related_name='professor')
  user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='usuário')
  nothing_listed_emmited = models.BooleanField(default=False, verbose_name='nada consta emitido')

  created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')

  class Meta:
    verbose_name = 'Professor'
    verbose_name_plural = 'Professores'

  
  def __str__(self):
    return self.name
    
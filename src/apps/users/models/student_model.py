from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .course_model import Course


def validate_academic_register(value: str):
  if not value[0].isalpha():
    raise ValidationError('RA deve começar com uma letra')
  if not value[1:].isnumeric():
    raise ValidationError('Todos os caractéres do RA, exceto o primeiro devem ser números')
  

class Student(models.Model):
  user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='usuário')
  course = models.ForeignKey(Course, on_delete=models.PROTECT, verbose_name='curso')
  academic_register = models.CharField(max_length=10, unique=True, verbose_name='registro acadêmico', validators=[validate_academic_register])
  name = models.CharField(max_length=50, verbose_name='nome')
  nothing_listed_emmited = models.BooleanField(default=False, verbose_name='nada consta emitido')

  created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')


  class Meta:
    verbose_name = 'Aluno'
    verbose_name_plural = 'Alunos'

  
  def __str__(self):
    return self.name
  
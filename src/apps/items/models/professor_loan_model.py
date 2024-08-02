from typing import Any, Iterable
from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.timezone import now

from .item_model import Item
from .location_model import Location
from apps.users.models import Professor


class ProfessorLoan(models.Model):
  professor = models.ForeignKey(Professor, verbose_name='professor', on_delete=models.PROTECT)
  item = models.ForeignKey(Item, verbose_name='item', on_delete=models.PROTECT)
  amount = models.IntegerField(validators=[MinValueValidator(1)], verbose_name='quantidade')
  date_of_loan = models.DateField(verbose_name='data do empréstimo', default=now)
  return_date = models.DateField(blank=True, null=True, verbose_name='data da devolução')
  location = models.ManyToManyField(Location, verbose_name='lugar', blank=True)

  created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')

  
  class Meta:
    verbose_name = 'Empréstimo do Professor'
    verbose_name_plural = 'Empréstimos de Professores'

  
  def __str__(self):
    return f'Professor: {self.professor} item: {self.item} quantidade: {self.amount}'
  

  def clean(self) -> None:
    if self.professor.nothing_listed_emmited:
      raise ValidationError({'professor': 'Não é possível fazer empréstimo para alunos com nada consta emitido'})
    if self.amount > self.item.quantity_available and not self.return_date:
      raise ValidationError({'amount': 'A quantidade emprestada não pode ser maior que a quantidade disponível'})
    return super().clean()
  

  def save(self, *args, **kwargs) -> None:
    if self.return_date:
      self.item.quantity_available += self.amount
      self.item.full_clean()
      self.item.save()
    else:
      self.item.quantity_available -= self.amount
      self.item.full_clean()
      self.item.save()
    return super().save(*args, **kwargs)
  

  def delete(self, *args, **kwargs) -> tuple[int, dict[str, int]]:
    self.item.quantity_available += self.amount
    return super().delete(*args, **kwargs)
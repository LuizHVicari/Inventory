from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages

from apps.users.models import Student
from apps.items.models import StudentLoan


class StudentLoans(TemplateView):
  def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    context = dict()
    
    user = self.request.user
    context['user'] = user

    try:
      student = Student.objects.get(user=user)
    except Student.DoesNotExist:
      messages.error('Apenas disponível para estudantes')
      return redirect('my_user_details')
    else:
      student_active_loans = StudentLoan.objects.filter(student=student)
      total_loans = student_active_loans.count()
      context['loans'] = student_active_loans
      context['total_loans'] = total_loans
      context['user_type'] = 'Estudante'

    print('to aqui')
    return render(request, 'users/all_loans.html', context)


student_loans_view = StudentLoans.as_view()
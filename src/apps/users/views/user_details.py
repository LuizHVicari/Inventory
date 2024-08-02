from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from apps.users.models import Student, Professor
from apps.items.models import StudentLoan, ProfessorLoan


class UserDetails(TemplateView):
  def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    context = dict()
    
    user = self.request.user
    context['user'] = user

    total_loans_student = 0
    total_loans_professor = 0

    try:
      student = Student.objects.get(user=user)
    except Student.DoesNotExist:
      pass
    else:
      context['student'] = student
      student_active_loans = StudentLoan.objects.filter(
        student=student, 
        return_date__isnull=True
      )
      total_loans_student = student_active_loans.count()
      context['student_loans'] = student_active_loans
      context['student_loans_active'] = True
      context['student_can_ask_nothing_listed'] = total_loans_student == 0
      

    try:
      professor =  Professor.objects.get(user=user)
      professor_active_loans = ProfessorLoan.objects.filter(
        professor=professor, 
        return_date__isnull=True
      )
      context['professor_loans'] = professor_active_loans
      context['professor_loans_active'] = True
      total_loans_professor = professor_active_loans.count()
      context['professor_can_ask_nothing_listed'] = total_loans_professor == 0
    except Professor.DoesNotExist:
      pass
    else:
      context['professor'] = professor
    
    context['total_loans'] = total_loans_professor + total_loans_student
    return render(request, 'users/user_detail.html', context)


user_details_view = UserDetails.as_view()
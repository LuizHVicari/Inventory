from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages

from apps.users.models import Professor
from apps.items.models import ProfessorLoan


class ProfessorLoans(TemplateView):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        context = dict()

        user = self.request.user
        context['user'] = user

        try:
            professor = Professor.objects.get(user=user)
        except Professor.DoesNotExist:
            messages.error(request, 'Apenas disponível para professores')
            return redirect('list_items')
        else:
            professor_active_loans = ProfessorLoan.objects.filter(
                professor=professor)
            total_loans = professor_active_loans.count()
            context['loans'] = professor_active_loans
            context['total_loans'] = total_loans
            context['user_type'] = 'Professor'

        return render(request, 'users/all_loans.html', context)


professor_loans_view = ProfessorLoans.as_view()

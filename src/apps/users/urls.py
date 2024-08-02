from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import user_details_view, student_loans_view, professor_loans_view


urlpatterns = [
  path('me/', login_required(user_details_view), name='my_user_details'),
  path('loans/student/', login_required(student_loans_view), name='student_loans'),
  path('loans/professor/', login_required(professor_loans_view), name='professor_loans'),
]

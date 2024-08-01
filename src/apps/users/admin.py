from django.contrib import admin

from .models import Course, Student, Department, Professor


class ProfessorInline(admin.TabularInline):
  model = Professor


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = ['name', 'academic_register', 'nothing_listed_emmited', 'created_at']
  list_filter = ['course', 'nothing_listed_emmited', 'course', 'created_at', 'updated_at']
  list_editable = ['nothing_listed_emmited',]
  search_fields = ['name', 'academic_register']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
  list_display = ['name', 'created_at' ]
  list_filter = ['name', 'created_at', 'updated_at']
  search_fields = ['name']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
  inlines = [ProfessorInline, ]
  list_display = ['name', 'acronym', 'created_at']
  list_filter = ['courses', 'created_at', 'updated_at']
  search_fields = ['name', 'courses']


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
  list_display = ['name', 'siape', 'department', 'created_at']
  list_filter = ['department', 'courses', 'created_at', 'updated_at']
  search_fields = ['name', 'siape', 'department__name', 'courses__name']


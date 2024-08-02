from django.contrib import admin

from .models import Item, Building, Location, Room, StudentLoan, ProfessorLoan


class LocationInline(admin.TabularInline):
  model = Location

class RoomInline(admin.TabularInline):
  model = Room

class ItemInline(admin.TabularInline):
  model = Item.location.through


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
  list_display = ['name', 'quantity', 'quantity_available', 'patrimony_number', 'available_for_students' ,'created_at']
  list_editable = ['quantity']
  list_filter = ['location', 'available_for_students', 'created_at', 'updated_at']
  search_fields = ['name', 'patrimony_number', 'location__name']


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
  inlines = [RoomInline]
  list_display = ['name', 'created_at']
  search_fields = ['name',]
  list_filter = ['created_at', 'updated_at']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
  inlines = [ItemInline,]
  list_display = ['name', 'room', 'created_at']
  list_filter = ['room', 'created_at', 'updated_at']
  list_editable = ['room',]
  search_fields = ['name', 'room__name']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
  inlines = [LocationInline]
  list_display = ['name', 'block', 'created_at']
  list_filter = ['block', 'created_at', 'updated_at']
  search_fields = ['name', 'block__name']


@admin.register(StudentLoan)
class StudentAdmin(admin.ModelAdmin):
  list_display = ['student', 'item', 'amount', 'date_of_loan', 'return_date', 'created_at']
  list_filter = ['student', 'item', 'date_of_loan', ('return_date', admin.EmptyFieldListFilter), 'created_at', 'updated_at']
  search_fields = ['student__name', 'student__academic_register', 'item__name', 'item__patrimony_number']
  list_editable = ['return_date']


@admin.register(ProfessorLoan)
class ProfessorLoanAdmin(admin.ModelAdmin):
  list_display = ['professor', 'item', 'amount', 'date_of_loan', 'return_date', 'created_at']
  list_filter = ['professor', 'item', 'date_of_loan', ('return_date', admin.EmptyFieldListFilter), 'location']
  search_fields = ['professor_name', 'professor_siape', 'item_name', 'item_patrimony_number', 'location']




  



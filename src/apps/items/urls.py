from django.urls import path

from .views import list_items_view, item_details_view

urlpatterns = [
  path('', list_items_view, name='list_items'),
  path('', item_details_view, name='item_detail'),
  path('<int:pk>/', item_details_view, name='item_detail')
]
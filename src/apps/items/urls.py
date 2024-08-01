from django.urls import path

from .views import list_items_view, search_item_view

urlpatterns = [
  path('', list_items_view, name='list_items'),
  path('item/', search_item_view, name='search_item')
]
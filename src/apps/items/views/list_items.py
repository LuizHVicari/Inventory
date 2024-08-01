from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from apps.items.models import Item


class ListItems(TemplateView):
  template_name = 'items/list_items.html'
  model = Item
  context_object_name = 'items'
  fields = [
    'name',
    'quantity'
  ]

  def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    items = Item.objects.all()
    
    context = {
      'items': items
    }
    return render(request, 'items/list_items.html', context)




list_items_view = ListItems.as_view()
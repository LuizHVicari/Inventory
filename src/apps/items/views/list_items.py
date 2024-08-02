from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages

from apps.items.models import Item


class ListItems(TemplateView):
  def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    search = request.GET.get('search')
    if search:
      items = Item.objects.filter(name__icontains=search.strip())
    else: 
      items = Item.objects.all()

    if not len(items):
      messages.error('Nenhum item corresponse à pesquisa')
    
    context = {
      'items': items
    }
    return render(request, 'items/list_items.html', context)

list_items_view = ListItems.as_view()
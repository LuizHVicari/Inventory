from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages

from apps.items.models import Item



class SearchItem(TemplateView):
  def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    item_name = self.request.GET.get('search')

    if item_name:
      result = Item.objects.filter(name__iexact=item_name.strip()).order_by('-created_at').first()
      print(result)
      if not result:
        messages.error(request, 'Item não encontrado')
        return redirect('list_items')
    else:
      messages.error(request, 'Informe um item')
      return redirect('list_items')
    
    context = {
      'item': result
    }
    return render(request, 'items/item_detail.html', context)




search_item_view = SearchItem.as_view()
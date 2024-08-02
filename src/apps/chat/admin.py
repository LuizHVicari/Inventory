from django.contrib import admin
from django.http import HttpRequest

from .models import Message, Chat


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
  fields = ['sender', 'chat', 'created_at']
  readonly_fields = fields
  search_fields = ['message', 'sender__username', 'chat__name']
  list_filter = ['sender', 'chat', 'created_at', 'updated_at']
  ordering = ['-updated_at', ]


  def has_change_permission(self, request: HttpRequest, obj = None):
    return False
  
  def has_delete_permission(self, request: HttpRequest, obj = None ):
    return False
  
  def has_add_permission(self, request: HttpRequest) -> bool:
    return False
  

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
  fields = ['user', 'created_at']
  readonly_fields = fields
  search_fields = ['user',] 
  list_filter = ['created_at', 'updated_at']

  def has_change_permission(self, request: HttpRequest, obj = None):
    return False
  
  def has_delete_permission(self, request: HttpRequest, obj = None ):
    return False
  
  def has_add_permission(self, request: HttpRequest) -> bool:
    return False

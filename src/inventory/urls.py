from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import DasahboardView


admin.site.site_title = 'Administração de Invetário'
admin.site.site_header = 'Administração de Inventário'
admin.site.index_title = 'Administração de Inventário'


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/', include('allauth.urls')),

    path('', DasahboardView.as_view(), name='dashboard')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
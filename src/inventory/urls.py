from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from allauth.account import views as allauth_views


admin.site.site_title = 'Administração de Invetário'
admin.site.site_header = 'Administração de Inventário'
admin.site.index_title = 'Administração de Inventário'


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path('accounts/', include('allauth.urls')),
    path('', include('apps.items.urls')),
    path('user/', include('apps.users.urls')),

    path('accounts/login/', allauth_views.LoginView.as_view(), name='account_login'),
    path('accounts/logout/', allauth_views.LogoutView.as_view(), name='account_logout'),
    path('accounts/password/change/', allauth_views.PasswordChangeView.as_view(), name='account_change_password'),
    path('accounts/password/reset/', allauth_views.PasswordResetView.as_view(), name='account_reset_password'),
    path('accounts/signup/', allauth_views.LoginView.as_view(), name='account_signup'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
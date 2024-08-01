from django.contrib.admin import AdminSite

class AdminPage(AdminSite):
  site_title = 'Administração do inventário'

admin_site = AdminPage()
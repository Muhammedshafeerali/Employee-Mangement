from django.urls import path
from . import views

urlpatterns = [
    # path("",views.home,name='home'),
    path('admin/',views.admin,name='admin'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('addemployee/',views.addemployee,name='addemployee'),
    path('editemployee/<int:id>/',views.editemployee,name='editemployee'),
    path('deleteemployee/<int:id>/',views.deleteemployee,name='deleteemployee'),
    path('logout/',views.logout,name='logout'),
    path('',views.home,name='home')

]
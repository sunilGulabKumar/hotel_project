from django.urls import path
from . import views

urlpatterns = [
    path('',views.create_employee,name="insert_recored"),
    path('<int:id>/',views.create_employee,name="edit_recored"),
    path('list/',views.employee_list),
    path('<int:id>/',views.employee_delete,name="delete_recored"),

]

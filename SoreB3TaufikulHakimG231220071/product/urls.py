from django.urls import path
from . import views

urlpatterns =  [
  # product/
  path('', views.index, name = 'product.index'),
  # product/add/
  path('add/', views.add, name = 'product.add'),
  # product/save/
  path('save/', views.save, name = 'product.save'),
  # product/edit/
  path('edit/<int:produc_id>/', views.edit, name = 'product.edit'),
  # product/update/
  path('update/<int:produc_id>/', views.update, name= 'product.update'),
  # product/delete/
  path('delete/<int:produc_id>/', views.delete, name = 'product.delete'),
]
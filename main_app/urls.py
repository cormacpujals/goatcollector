from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('goats/', views.goats_index, name='index'),
  path('goats/<int:goat_id>/', views.goats_detail, name='detail'),
  path('goats/create/', views.GoatCreate.as_view(), name='goats_create'),
  path('goats/<int:pk>/update/', views.GoatUpdate.as_view(), name='goats_update'),
  path('goats/<int:pk>/delete/', views.GoatDelete.as_view(), name='goats_delete'),
  path('goats/<int:goat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  
  path('goats/<int:goat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  path('goats/<int:goat_id>/unassoc_toy/<int:toy_id>/', views.unassoc_toy, name='unassoc_toy'),

  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]
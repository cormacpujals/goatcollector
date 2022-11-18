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
]
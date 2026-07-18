from django.urls import path
from booking import views


urlpatterns = [
  path('houses/', views.houses_list_view, name='houses-list'),
  path('houses/booked', views.houses_booked_view, name='booked-houses-list'),
  path('houses/detail/<int:pk>', views.house_detail_view, name='house-detail'),
  path('houses/create/', views.house_create_view, name='house-create'),
  path('houses/update/<int:pk>', views.house_update_view, name='house-update'),
  path('houses/delete/<int:pk>', views.house_delete_view, name='house-delete'),
]
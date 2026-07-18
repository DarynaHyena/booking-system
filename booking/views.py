from django.shortcuts import get_object_or_404, render, redirect
from booking.models import HouseModel, BookingModel


def houses_list_view(request):
  houses = HouseModel.objects.all()
  context = {
    "houses": houses
  }
  return render(
    request, 
    'houses/list.html', 
    context
    )






def house_detail_view(request, pk):
  house = get_object_or_404(HouseModel, pk=pk)
  context = {
    "house": house
  }
  return render(
    request, 
    'houses/detail.html', 
    context
    )

def house_create_view(request):
  pass

def house_update_view(request):
  pass

def house_delete_view(request, pk):
  house = get_object_or_404(HouseModel, pk=pk)
  house.delete()
  return redirect('house-list')
from django.http.response import HttpResponse
from django.shortcuts import get_list_or_404, render
from .models import Room
# Create your views here.


def index(request):
    return render(request, 'base.html')


def room(request):
    room_list = get_list_or_404(Room)
    return render(request, 'base.html', {'room_list':room_list})
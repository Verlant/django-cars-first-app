from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Car


def detail(request, car_id):
    return HttpResponse("You're looking at car %s." % car_id)


def index(request):
    car_list = Car.objects.all()
    context = {'car_list': car_list}
    return render(request, 'app/index.html', context)
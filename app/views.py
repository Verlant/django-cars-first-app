from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from .forms import CarForm


def car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CarForm()
    return render(request, 'app/cars.html', {'form': form})


def details(request, car_id):
    car = Car.objects.get(id=car_id)
    context = {'car': car}
    return render(request, 'app/details.html', context)


def index(request):
    car_list = Car.objects.all()
    context = {'car_list': car_list}
    return render(request, 'app/index.html', context)
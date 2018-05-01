from django.shortcuts import render, redirect, get_object_or_404 
from .models import Car
from .forms import CarModelForm


def index(request):
    cars = Car.objects.filter(is_deleted=False)
    return render(request, 'index.html', {'cars':cars})


def deleted_cars(request):
    deleted_cars = Car.objects.filter(is_deleted=True)
    return render(request, 'index.html', {'cars':deleted_cars})

def car_create(request):
    form = CarModelForm()
    if request.method == "POST":
        form = CarModelForm(request.POST)
        if form.is_valid():
            car = form.save()
            return redirect('myapp:car_details', pk=car.pk)
    context = {'form': form}
    return render(request, 'car_create.html', context)

def car_details(request, pk):
    carss = get_object_or_404(Car, pk=pk)
    context = {'c': carss}
    return render(request, 'car_details.html', context)

def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = CarModelForm(instance=car)
    if request.method == 'POST':
        # Сохраняем изменения в экземпляре car (т.е. не создаем новую запись)
        form = CarModelForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save()
            return redirect('myapp:car_details', pk=car.pk)
    context = {'form':form, 'ca': car}
    return render(request, 'car_edit.html', context)

def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.is_deleted = True
        car.save()
        return redirect('myapp:index')
    context = {'car': car}
    return render(request, 'car_delete.html', context)

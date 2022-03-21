from django.shortcuts import render, redirect
from .forms import Contact
from .models import *




def homepage(request):
    orders = Pizza.objects.all()

    context = {'orders': orders}
    return render(request, 'store/index.html', context)


def about(request):
    employees = Employees.objects.all()
    context = {'employees': employees}
    return render(request, 'store/about.html', context)


def contact(request):
    form = Contact
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {'form': form}
    return render(request, 'store/contact.html', context)


def salad(request):
    orders = Salad.objects.all()
    context = {'orders': orders}
    return render(request, 'store/salad.html', context)


def noodle(request):
    noodles = Noodle.objects.all()
    context = {'noodles': noodles}
    return render(request, 'store/noodle.html', context)

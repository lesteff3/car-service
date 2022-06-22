from django.shortcuts import render, redirect
from django.views import View
from .models import OrderItems
from .forms import OrderItemsForm

from main.models import *


def country(request):
    model = Country.objects.all()
    context = {
        'title': 'Аренда автомобилей',
        'model': model

    }
    return render(request, 'main/rent.html', context=context)


def detail(request, country_id):

    brand_detail = Brand.objects.filter(country_id=country_id)
    return render(request, 'main/details_view.html', {'brand_detail': brand_detail,
                                                      'title': 'Список автомобилей из выбранной категории'})


def auto(request, brand_id):
    auto_detail = Auto.objects.filter(brand_id=brand_id)
    return render(request, 'main/auto.html', {'auto_detail': auto_detail,
                                              'title': 'Список автомобилей из выбранной категории'})


class AutoDetailView(View):
    def get(self, request, pk):
        auto = Auto.objects.get(id=pk)
        return render(request, 'main/auto_details.html', {'auto': auto,
                                                          'title': 'Информация про выбранный автомобиль'})


def register_rent_car(request):
    error = ''
    user = OrderItems.objects.filter(order=request.user).first()
    if request.method == 'POST':
        form = OrderItemsForm(request.POST, instance=user)
        if form.is_valid():
            order = form.save(commit=False)
            order.order = request.user
            order.save()
            return redirect('successful')
        else:
            error = 'Не верно заполнили заявку'

    form = OrderItemsForm(instance=user)

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/rent_car.html', data)


def successful_register(request):
    return render(request, 'main/succsesful_register.html')
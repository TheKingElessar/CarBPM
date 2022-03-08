# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from bpm.models import CarBPM


def index(request):
    cars_list = CarBPM.objects.order_by('-car_last_updated_date')
    return render(request, 'bpm/index.html', {'cars_list': cars_list})


def make(request, make_string):
    cars_list = CarBPM.objects.order_by('-car_last_updated_date')
    make_list = []
    car: CarBPM
    for car in cars_list:
        if str(car.car_make_text).lower() == str(make_string).lower():
            make_list.append(car)
    if len(make_list) == 0:
        raise Http404(f"Car make \"{make_string}\" doesn't exist in our database!")

    return render(request, 'bpm/make.html', {'make_string': make_string, 'make_list': make_list})


def model(request, make_string, model_string):
    response = f"You're looking at make/model {make_string}/{model_string}."
    return HttpResponse(response)


def year(request, make_string, model_string, year_int):
    response = f"You're looking at make/model/year {make_string}/{model_string}/{year_int}."
    return HttpResponse(response)


def edit(request, make_string, model_string, year_int):
    response = f"You would like to edit make/model/year {make_string}/{model_string}/{year_int}."
    return HttpResponse(response)


def new(request):
    return HttpResponse("You're at the /new/ page to enter a new BPM!")

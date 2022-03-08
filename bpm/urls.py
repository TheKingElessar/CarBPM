from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('/bpm/<make_string>/', views.make, name = 'make'),
    path('/bpm/<make_string>/<model_string>', views.model, name = 'model'),
    path('/bpm/<make_string>/<model_string>/<year_int>', views.year, name = 'year'),
    path('/bpm/new/', views.new, name = 'new'),
]

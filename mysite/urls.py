"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from bpm import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('bpm.urls')),
    path('bpm/', include('bpm.urls')),

    path('bpm/new/', views.new, name = 'new'),

    # ex: /bpm/jeep/
    path('bpm/<make_string>/', views.make, name = 'make'),
    # ex: /bpm/jeep/patriot
    path('bpm/<make_string>/<model_string>/', views.model, name = 'model'),
    # ex: /bpm/jeep/patriot/2014
    path('bpm/<make_string>/<model_string>/<int:year_int>', views.year, name = 'year'),
    # ex: /bpm/jeep/patriot/2014/edit
    path('bpm/<make_string>/<model_string>/<int:year_int>/edit', views.edit, name = 'edit'),
]

from django.urls import path, include

from . import views

app_name = 'cars'

urlpatterns = [
    path('makes', views.CarMakeFilterView.as_view()),
]

from django.urls import path
from .views import *
urlpatterns = [
    path('',PageApi.as_view(),name="page")
]
from django.urls import path
from .views import ProfileApiView,ProfileTemplateView

urlpatterns = [
    path('api/reg',ProfileApiView.as_view(),name="reg"),
    path('reg',ProfileTemplateView.as_view(),name="template-reg")
]
from django.urls import path
from .views import *
urlpatterns = [
    path('',base_landing_page,name="base-landing"),
    path('sign-in',LoginTemplateView.as_view(),name="sign-in"),
    path('login-check',sign_in,name="login-check"),
    path('api/login',LoginView.as_view(),name="login"),
    path('richtext',RichTextTemplateView.as_view(),name="richtext"),
    path('practice',PracticeTemplateView.as_view(),name="richtext")
]
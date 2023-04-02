from django.urls import path
from .views import *
urlpatterns =[
    path('default',show,name="default"),
    path('no-toolbar',secondSetion,name="no-toolbar"),
    path('base',base,name="show-base"),
    path('light-aside',thirdSection,name='light-aside'),
    path('only-header',fourthsection,name="only-header"),
    path('/side-menu',SideMenuList.as_view(),name="side-menu")
    
]
from django.urls import path
from .views import HomePage,Aboutpage,Servicespage


urlpatterns =[
    path("", HomePage.as_view(), name="home"),
    path("about/", Aboutpage.as_view(), name="about"),
    path("service/", Servicespage.as_view(), name="service")
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home.as_view(), name='home'),
    url(r'^Annual_report/', views.Annual_report.as_view(), name='Annual'),
    url(r'^IR_service/', views.IR_service.as_view(), name='IR_service'),
    url(r'^iss/', views.iss.as_view(), name='iss'),
    url(r'^iro/', views.iro.as_view(), name='iro'), 
    url(r'^ipo/', views.ipo.as_view(), name='ipo'),
    url(r'^contact/', views.contact.as_view(), name='contact'),  
]

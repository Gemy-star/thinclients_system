from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('features', views.features_page, name='features'),
    path('about', views.about_page, name='about'),
    path('contact', views.contact_page, name='contact'),
    path('reports', views.report_page, name='reports'),

]

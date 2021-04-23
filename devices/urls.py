from django.urls import path
from . import views

urlpatterns = [
    path('allUnits', views.all_Units, name='all-units'),
    path('Unit/detail/<int:pk>', views.unit_details, name='unit-detail'),
    path('delete/thin', views.delete_thin, name='delete_thin'),
    path('get/thin', views.get_thin_byId, name='get_thin'),
    path('update/thin', views.update_thin, name='update_thin'),
    path('create/thin', views.create_thin, name='create_thin'),
    path('unit/report', views.report, name='report_unit'),
    path('get/unit', views.get_unit_byId, name='get_unit'),
    path('delete/unit', views.delete_unit, name='delete_unit'),
    path('update/unit', views.update_unit, name='update_unit'),
    path('create/unit', views.create_unit, name='create_unit'),
]

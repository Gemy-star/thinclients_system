from django.urls import path
from . import views

urlpatterns = [
    path('allUnits', views.all_Units, name='all-units'),
    path('codeName', views.all_codeName, name='code-name'),
    path('codePlace', views.all_codeplace, name='code-place'),
    path('codeTotal', views.all_codetotal, name='code-total'),
    path('Unit/code/<int:pk>', views.unit_details_code, name='unit-detail-code'),
    path('delete/thin', views.delete_thin, name='delete_thin'),
    path('get/thin', views.get_thin_byId, name='get_thin'),
    path('update/thin', views.update_thin, name='update_thin'),
    path('create/thin', views.create_thin, name='create_thin'),
    path('unit/report', views.report, name='report_unit'),
    path('get/codeName', views.get_codeName_byId, name='codeName-id'),
    path('get/codePlace', views.get_codePlace_byId, name='codePlace-id'),
    path('get/codeTotal', views.get_codeTotal_byId, name='codeTotal-id'),
    path('delete/code_name', views.delete_codeName, name='delete_codeName'),
    path('delete/code_place', views.delete_codeplace, name='delete_codePlace'),
    path('delete/code_total', views.delete_codetotal, name='delete_codeTotal'),
    path('update/codeName', views.update_code_name, name='update_codeName'),
    path('update/codePlace', views.update_code_place, name='update_codePlace'),
    path('update/codeTotal', views.update_code_total, name='update_codeTotal'),
    path('create/codeName', views.create_code_name, name='create_codeName'),
    path('create/codePlace', views.create_code_place, name='create_codePlace'),
    path('create/codeTotal', views.create_code_total, name='create_codeTotal'),

]

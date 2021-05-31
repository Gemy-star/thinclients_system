from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from .models import ThinUnits, ThinDevicesUnits, ThinCodeName, ThinCodeTotal, ThinCodePlace
from thin_clients.utils import render_to_pdf
from django.template.loader import get_template
from datetime import datetime
from django.db.models import Sum


def all_Units(request):
    units = ThinCodeTotal.objects.all()
    context = {"units": units}
    return render(request, 'devices/all_units.html', context)


def all_codeName(request):
    units = ThinCodeName.objects.all()
    names = [x for x in ThinCodeName.NAME_CHOICES if x not in units.values_list('name', flat=True)]
    context = {"units": units, "unit_names": names}
    return render(request, 'devices/code_unitname.html', context)


def all_codeplace(request):
    units = ThinCodePlace.objects.all()
    names = [x for x in ThinCodeName.NAME_CHOICES if x in units.values_list('code__name', flat=True)]
    context = {"units": units, "unit_names": names}
    return render(request, 'devices/code_place.html', context)


def all_codetotal(request):
    units = ThinCodeTotal.objects.all()
    names = [x for x in ThinCodeName.NAME_CHOICES if x in units.values_list('code__name', flat=True)]
    context = {"units": units, "unit_names": names}
    return render(request, 'devices/code_total.html', context)


def unit_details_code(request, pk):
    unit = ThinCodeName.objects.get(pk=pk)
    total = ThinCodeTotal.objects.get(code=unit)
    thinclients = ThinDevicesUnits.objects.filter(code=unit)
    total_devices = total.total
    devices_done = thinclients.aggregate(Sum('devices_done'))
    if total_devices is None:
        per25 = 0
        per50 = 0
    else:
        per25 = int(total_devices) * 25 / 100
        per50 = int(total_devices) * 50 / 100

    context = {"clients": thinclients, "pk": pk, "total_devices": total_devices, "unit": unit,
               "devices_done": devices_done['devices_done__sum'], "per25": per25, "per50": per50}
    return render(request, 'devices/unit_details.html', context)


def delete_thin(request):
    if request.method == "POST" and request.is_ajax:
        id = request.POST.get("id")
        thin = ThinDevicesUnits.objects.get(pk=id)
        thin.delete()
        return JsonResponse({"data": 1})


def delete_codeName(request):
    if request.method == "POST" and request.is_ajax:
        id = request.POST.get("id")
        thin = ThinCodeName.objects.get(pk=id)
        thin.delete()
        return JsonResponse({"data": 1})


def delete_codeplace(request):
    if request.method == "POST" and request.is_ajax:
        id = request.POST.get("id")
        thin = ThinCodePlace.objects.get(pk=id)
        thin.delete()
        return JsonResponse({"data": 1})


def delete_codetotal(request):
    if request.method == "POST" and request.is_ajax:
        id = request.POST.get("id")
        thin = ThinCodeTotal.objects.get(pk=id)
        thin.delete()
        return JsonResponse({"data": 1})


def get_thin_byId(request):
    if request.method == 'POST' and request.is_ajax:
        id = request.POST.get('id')
        thin = ThinDevicesUnits.objects.filter(pk=id)
        qs_json = serializers.serialize('json', list(thin))
        return JsonResponse({"data": qs_json})


def get_codeName_byId(request):
    if request.method == 'POST' and request.is_ajax:
        id = request.POST.get('id')
        thin = ThinCodeName.objects.filter(pk=id)
        qs_json = serializers.serialize('json', list(thin))
        return JsonResponse({"data": qs_json})


def get_codePlace_byId(request):
    if request.method == 'POST' and request.is_ajax:
        id = request.POST.get('id')
        thin = ThinCodePlace.objects.get(pk=id)
        name = thin.code.name
        qs_json = serializers.serialize('json', queryset=[thin])
        return JsonResponse({"data": qs_json, "name": name})


def get_codeTotal_byId(request):
    if request.method == 'POST' and request.is_ajax:
        id = request.POST.get('id')
        thin = ThinCodeTotal.objects.get(pk=id)
        name = thin.code.name
        qs_json = serializers.serialize('json', queryset=[thin])
        return JsonResponse({"data": qs_json, "name": name})


def update_thin(request):
    if request.method == "POST" and request.is_ajax:
        update_id = request.POST.get('update_id')
        cdb = request.POST.get('cdb')
        epg = request.POST.get('epg')
        re_date = request.POST.get('re_date')
        de_date = request.POST.get('de_date')
        short_name = request.POST.get('short_name')
        database_zone = request.POST.get('database_zone')
        database_name = request.POST.get('database_name')
        devices_done = request.POST.get('devices_done')
        thin = ThinDevicesUnits.objects.get(pk=update_id)
        thin.cdb = cdb
        thin.epg = epg
        thin.short_name = short_name
        thin.database_name = database_name
        thin.database_zone = database_zone
        thin.devices_done = devices_done
        thin.recieved_date = re_date
        thin.delivery_date = de_date
        try:
            thin.save()
            return JsonResponse({"data": 1})
        except:
            return JsonResponse({"data": -1})


def update_code_name(request):
    if request.method == "POST" and request.is_ajax:
        update_id = request.POST.get('update_id')
        name = request.POST.get('name')
        code = request.POST.get('code')
        thin = ThinCodeName.objects.get(pk=update_id)
        thin.name = name
        thin.code = code
        try:
            thin.save()
            return JsonResponse({"data": 1})
        except:
            return JsonResponse({"data": -1})


def update_code_place(request):
    if request.method == "POST" and request.is_ajax:
        update_id = request.POST.get('update_id')
        place = request.POST.get('place')
        code = request.POST.get('code')
        thin = ThinCodePlace.objects.get(pk=update_id)
        if ThinCodeName.objects.filter(name=code).exists():
            code_obj = ThinCodeName.objects.get(name__exact=code)
            thin.place = place
            thin.code = code_obj
            try:
                thin.save()
                return JsonResponse({"data": 1})
            except:
                return JsonResponse({"data": -1})
        else:
            return JsonResponse({"data": -1})


def update_code_total(request):
    if request.method == "POST" and request.is_ajax:
        update_id = request.POST.get('update_id')
        total = request.POST.get('total')
        code = request.POST.get('code')
        thin = ThinCodeTotal.objects.get(pk=update_id)
        if ThinCodeName.objects.filter(name=code).exists():
            code_obj = ThinCodeName.objects.get(name__exact=code)
            thin.total = total
            thin.code = code_obj
            try:
                thin.save()
                return JsonResponse({"data": 1})
            except:
                return JsonResponse({"data": -1})
        else:
            return JsonResponse({"data": -1})


def create_thin(request):
    if request.method == "POST" and request.is_ajax:
        pk = request.POST.get('pk')
        cdb = request.POST.get('cdb')
        epg = request.POST.get('epg')
        code_obj = ThinCodeName.objects.get(pk=pk)
        short_name = request.POST.get('short_name')
        re_date = request.POST.get('re_date')
        de_date = request.POST.get('de_date')
        database_zone = request.POST.get('database_zone')
        database_name = request.POST.get('database_name')
        devices_done = request.POST.get('devices_done')
        if ThinCodeTotal.objects.filter(code=code_obj).exists():
            total_devices = ThinCodeTotal.objects.get(code=code_obj)
            thin = ThinDevicesUnits(cdb=cdb, epg=epg, code=code_obj,
                                    short_name=short_name,recieved_date=re_date , delivery_date=de_date,
                                    database_name=database_name
                                    , database_zone=database_zone, devices_done=devices_done,
                                    total_devices=total_devices)
            try:
                thin.save()
                return JsonResponse({"data": 1})
            except:
                return JsonResponse({"data": -1})
        else:
            thin = ThinDevicesUnits(cdb=cdb, epg=epg, code=code_obj,
                                    short_name=short_name,
                                    database_name=database_name
                                    , database_zone=database_zone, devices_done=devices_done,
                                    recieved_date=re_date , delivery_date=de_date)
            try:
                thin.save()
                return JsonResponse({"data": 1})
            except:
                return JsonResponse({"data": -1})


def create_code_name(request):
    if request.method == "POST" and request.is_ajax:
        name = request.POST.get('name')
        code = request.POST.get('code')
        thin = ThinCodeName(name=name, code=code)
        try:
            thin.save()
            return JsonResponse({"data": 1})
        except:
            return JsonResponse({"data": -1})


def create_code_place(request):
    if request.method == "POST" and request.is_ajax:
        place = request.POST.get('place')
        code = request.POST.get('code')
        if ThinCodeName.objects.filter(name__exact=code).exists():
            if ThinCodePlace.objects.filter(code__name=code).exists():
                return JsonResponse({"data": -1})
            code_obj = ThinCodeName.objects.get(name__exact=code)
            thin = ThinCodePlace(place=place, code=code_obj)
            try:
                thin.save()
                return JsonResponse({"data": 1})
            except:
                return JsonResponse({"data": -1})
        else:
            return JsonResponse({"data": -1})


def create_code_total(request):
    if request.method == "POST" and request.is_ajax:
        total = request.POST.get('total')
        code = request.POST.get('code')
        if ThinCodeName.objects.filter(name__exact=code).exists():
            if ThinCodeTotal.objects.filter(code__name=code).exists():
                return JsonResponse({"data": -1})
            code_obj = ThinCodeName.objects.get(name__exact=code)
            thin = ThinCodeTotal(total=total, code=code_obj)
            try:
                thin.save()
                return JsonResponse({"data": 1})
            except:
                return JsonResponse({"data": -1})
        else:
            return JsonResponse({"data": -1})


def report(request):
    context = {"units": ThinUnits.objects.all()}
    if request.method == "POST":
        pk = request.POST.get('pk')
        template = get_template('uint_reports.html')
        thin = ThinUnits.objects.get(pk=pk)
        units = ThinDevicesUnits.objects.filter(unit=thin)
        context = {
            "company": "مركز النظم و الدعم المتكامل",
            "devices": units,
            "unit": thin,
            "topic": "تفاصيل العمل اليومى للوحدة  ",
            "today": datetime.today().strftime('%Y-%m-%d'),
        }
        html = template.render(context)
        pdf = render_to_pdf('uint_reports.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
    return render(request, 'devices/filterreport.html', context=context)

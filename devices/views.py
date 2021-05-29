from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from .models import ThinUnits, ThinDevicesUnits, ThinCodeName, ThinCodeTotal, ThinCodePlace
from users.models import User
from thin_clients.utils import render_to_pdf
from django.template.loader import get_template
from datetime import datetime
from django.db.models import Sum


def all_Units(request):
    units = ThinUnits.objects.all()
    context = {"units": units, "codes": ThinCodeName.objects.all(), "unit_names": ThinCodeName.NAME_CHOICES}
    return render(request, 'devices/all_units.html', context)


def all_codeName(request):
    units = ThinCodeName.objects.all()
    context = {"units": units, "unit_names": ThinCodeName.NAME_CHOICES}
    return render(request, 'devices/code_unitname.html', context)


def all_codeplace(request):
    units = ThinCodePlace.objects.all()
    context = {"units": units, "codes": ThinCodeName.objects.all()}
    return render(request, 'devices/code_place.html', context)


def all_codetotal(request):
    units = ThinCodeTotal.objects.all()
    context = {"units": units, "codes": ThinCodeName.objects.all()}
    return render(request, 'devices/code_total.html', context)


def unit_details(request, pk):
    unit = ThinUnits.objects.get(pk=pk)
    thinclients = ThinDevicesUnits.objects.filter(unit=unit)
    total_devices = ThinDevicesUnits.objects.aggregate(Sum('total_devices'))
    per25 = total_devices['total_devices_sum']*25 / 100
    per50 = total_devices['total_devices_sum']*50 / 100
    devices_done = ThinDevicesUnits.objects.aggregate(Sum('devices_done'))
    context = {"clients": thinclients, "pk": pk, "total_devices": total_devices['total_devices_sum'],
               "devices_done": devices_done['devices_done_sum'] , "per25":per25 , "per50":per50}
    return render(request, 'devices/unit_details.html', context)


def unit_details_code(request, pk):
    unit = ThinCodeName.objects.get(pk=pk)
    thinclients = ThinDevicesUnits.objects.filter(code=unit)
    codes = ThinCodeName.objects.all()
    total_devices = thinclients.aggregate(Sum('total_devices'))
    devices_done = thinclients.aggregate(Sum('devices_done'))
    if total_devices['total_devices__sum'] is None :
        per25 = 0
        per50 = 0
    else:
        per25 = total_devices['total_devices__sum'] * 25 / 100
        per50 = total_devices['total_devices__sum'] * 50 / 100
    context = {"clients": thinclients, "pk": pk, "total_devices": total_devices['total_devices__sum'],"codes":codes,
               "devices_done": devices_done['devices_done__sum'], "per25": per25, "per50": per50}
    return render(request, 'devices/unit_details.html', context)


def delete_thin(request):
    if request.method == "POST" and request.is_ajax:
        id = request.POST.get("id")
        thin = ThinDevicesUnits.objects.get(pk=id)
        thin.delete()
        return JsonResponse({"data": 1})


def delete_unit(request):
    if request.method == "POST" and request.is_ajax:
        id = request.POST.get("id")
        thin = ThinUnits.objects.get(pk=id)
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


def get_unit_byId(request):
    if request.method == 'POST' and request.is_ajax:
        id = request.POST.get('id')
        thin = ThinUnits.objects.filter(pk=id)
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
        thin = ThinCodePlace.objects.filter(pk=id)
        qs_json = serializers.serialize('json', list(thin))
        return JsonResponse({"data": qs_json})


def get_codeTotal_byId(request):
    if request.method == 'POST' and request.is_ajax:
        id = request.POST.get('id')
        thin = ThinCodeTotal.objects.filter(pk=id)
        qs_json = serializers.serialize('json', list(thin))
        return JsonResponse({"data": qs_json})


def update_thin(request):
    if request.method == "POST" and request.is_ajax:
        update_id = request.POST.get('update_id')
        user = User.objects.get(pk=request.user.pk)
        cdb = request.POST.get('cdb')
        epg = request.POST.get('epg')
        code = request.POST.get('code')
        code_obj = ThinCodeName.objects.get(pk=code)
        short_name = request.POST.get('short_name')
        database_zone = request.POST.get('database_zone')
        database_name = request.POST.get('database_name')
        devices_done = request.POST.get('devices_done')
        total_devices = request.POST.get('total_devices')
        thin = ThinDevicesUnits.objects.get(pk=update_id)
        thin.added_by = user
        thin.cdb = cdb
        thin.epg = epg
        thin.code = code_obj
        thin.short_name = short_name
        thin.database_name = database_name
        thin.database_zone = database_zone
        thin.devices_done = devices_done
        thin.total_devices = total_devices
        thin.save()
        return JsonResponse({"data": 1})


def update_unit(request):
    if request.method == "POST" and request.is_ajax:
        update_id = request.POST.get('update_id')
        name = request.POST.get('name')
        code = request.POST.get('code')
        total = request.POST.get('total')
        status = request.POST.get('status')
        thin = ThinUnits.objects.get(pk=update_id)
        thin.total.code.name = name
        thin.status = status
        thin.total.code.code = code
        thin.total.total = total
        thin.save()
        return JsonResponse({"data": 1})


def update_code_name(request):
    if request.method == "POST" and request.is_ajax:
        update_id = request.POST.get('update_id')
        name = request.POST.get('name')
        code = request.POST.get('code')
        thin = ThinCodeName.objects.get(pk=update_id)
        thin.name = name
        thin.code = code
        thin.save()
        return JsonResponse({"data": 1})


def update_code_place(request):
    if request.method == "POST" and request.is_ajax:
        update_id = request.POST.get('update_id')
        place = request.POST.get('place')
        code = request.POST.get('code')
        code_obj = ThinCodeName.objects.get(pk=code)
        thin = ThinCodePlace.objects.get(pk=update_id)
        thin.place = place
        thin.code = code_obj
        thin.save()
        return JsonResponse({"data": 1})


def update_code_total(request):
    if request.method == "POST" and request.is_ajax:
        update_id = request.POST.get('update_id')
        total = request.POST.get('total')
        code = request.POST.get('code')
        code_obj = ThinCodeName.objects.get(pk=code)
        thin = ThinCodeTotal.objects.get(pk=update_id)
        thin.total = total
        thin.code = code_obj
        thin.save()
        return JsonResponse({"data": 1})


def create_thin(request):
    if request.method == "POST" and request.is_ajax:
        user_obj = User.objects.get(pk=request.user.pk)
        pk = request.POST.get('pk')
        cdb = request.POST.get('cdb')
        epg = request.POST.get('epg')
        code = request.POST.get('code')
        code_obj = ThinCodeName.objects.get(pk=code)
        short_name = request.POST.get('short_name')
        database_zone = request.POST.get('database_zone')
        database_name = request.POST.get('database_name')
        devices_done = request.POST.get('devices_done')
        total_devices = request.POST.get('total_devices')
        thin = ThinDevicesUnits(added_by=user_obj, cdb=cdb, epg=epg, code=code_obj,
                                short_name=short_name,
                                database_name=database_name
                                , database_zone=database_zone, devices_done=devices_done,
                                total_devices=total_devices)
        thin.save()
        if thin.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def create_unit(request):
    if request.method == "POST" and request.is_ajax:
        name = request.POST.get('name')
        code = request.POST.get('code')
        code_name = ThinCodeName(name=name, code=code)
        code_name.save()
        total = request.POST.get('total')
        total_obj = ThinCodeTotal(code=code_name, total=total)
        total_obj.save()
        status = request.POST.get('status')
        thin = ThinUnits(total=total_obj, status=status)
        thin.save()
        if thin.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def create_code_name(request):
    if request.method == "POST" and request.is_ajax:
        name = request.POST.get('name')
        code = request.POST.get('code')
        thin = ThinCodeName(name=name, code=code)
        thin.save()
        if thin.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def create_code_place(request):
    if request.method == "POST" and request.is_ajax:
        place = request.POST.get('place')
        code = request.POST.get('code')
        code_obj = ThinCodeName.objects.get(pk=code)
        thin = ThinCodePlace(place=place, code=code_obj)
        thin.save()
        if thin.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def create_code_total(request):
    if request.method == "POST" and request.is_ajax:
        total = request.POST.get('total')
        code = request.POST.get('code')
        code_obj = ThinCodeName.objects.get(pk=code)
        thin = ThinCodeTotal(total=total, code=code_obj)
        thin.save()
        if thin.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def report(request):
    context = {"units": ThinUnits.objects.all()}
    if request.method == "POST":
        pk = request.POST.get('pk')
        template = get_template('uint_reports.html')
        thin = ThinUnits.objects.get(pk=pk)
        units = ThinDevicesUnits.objects.filter(unit=thin)
        user_obj = User.objects.get(pk=request.user.pk)
        context = {
            "company": "مركز النظم و الدعم المتكامل",
            "user": user_obj,
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

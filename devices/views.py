from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from .models import ThinUnits, ThinDevicesUnits
from users.models import User
from thin_clients.utils import render_to_pdf
from django.template.loader import get_template
from datetime import datetime
from django.db.models import Sum


def all_Units(request):
    units = ThinUnits.objects.all()
    context = {"units": units, "unit_names": ThinUnits.NAME_CHOICES}
    return render(request, 'devices/all_units.html', context)


def unit_details(request, pk):
    unit = ThinUnits.objects.get(pk=pk)
    thinclients = ThinDevicesUnits.objects.filter(unit=unit)
    per25 = ThinDevicesUnits.objects.aggregate(Sum('twinte_five_percentgy'))
    per50 = ThinDevicesUnits.objects.aggregate(Sum('fifty_percentgy'))
    context = {"clients": thinclients, "pk": pk, "per25": dict(per25).values(), "per50": dict(per50).values()}
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


def update_thin(request):
    if request.method == "POST" and request.is_ajax:
        update_id = request.POST.get('update_id')
        user = User.objects.get(pk=request.user.pk)
        cdb = request.POST.get('cdb')
        epg = request.POST.get('epg')
        per25 = request.POST.get('per25')
        per50 = request.POST.get('per50')
        short_name = request.POST.get('short_name')
        database_zone = request.POST.get('database_zone')
        database_name = request.POST.get('database_name')
        devices_done = request.POST.get('devices_done')
        total_devices = request.POST.get('total_devices')
        thin = ThinDevicesUnits.objects.get(pk=update_id)
        thin.added_by = user
        thin.cdb = cdb
        thin.epg = epg
        thin.short_name = short_name
        thin.database_name = database_name
        thin.database_zone = database_zone
        thin.devices_done = devices_done
        thin.twinte_five_percentgy = per25
        thin.fifty_percentgy = per50
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
        thin.name = name
        thin.status = status
        thin.code = code
        thin.total = total
        thin.save()
        return JsonResponse({"data": 1})


def create_thin(request):
    if request.method == "POST" and request.is_ajax:
        user_obj = User.objects.get(pk=request.user.pk)
        pk = request.POST.get('pk')
        thin = ThinUnits.objects.get(pk=pk)
        cdb = request.POST.get('cdb')
        epg = request.POST.get('epg')
        per25 = request.POST.get('per25')
        per50 = request.POST.get('per50')
        short_name = request.POST.get('short_name')
        database_zone = request.POST.get('database_zone')
        database_name = request.POST.get('database_name')
        devices_done = request.POST.get('devices_done')
        total_devices = request.POST.get('total_devices')
        thin = ThinDevicesUnits(unit=thin, added_by=user_obj, cdb=cdb, epg=epg,
                                short_name=short_name,
                                database_name=database_name
                                , database_zone=database_zone, devices_done=devices_done,
                                total_devices=total_devices, fifty_percentgy=per50, twinte_five_percentgy=per25)
        thin.save()
        if thin.pk:
            return JsonResponse({"data": 1})
        else:
            return JsonResponse({"data": -1})


def create_unit(request):
    if request.method == "POST" and request.is_ajax:
        name = request.POST.get('name')
        status = request.POST.get('status')
        code = request.POST.get('code')
        total = request.POST.get('total')
        thin = ThinUnits(name=name, status=status, code=code, total=total)
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

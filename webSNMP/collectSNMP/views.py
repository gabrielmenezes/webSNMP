from django.shortcuts import render
from django.template import loader
# Create your views here.

from django.http import HttpResponse

from .models import Device


def index(request):
    device_list = Device.objects.all()
    template = loader.get_template("collectSNMP/index.html")
    context = {
        'device_list': device_list,
    }
    return HttpResponse(template.render(context, request))


def selectOid(request, device_id):
    device = Device.objects.get(id=device_id)
    return HttpResponse("Selecionado device %s" % device.device_name)


def viewGraph(request, device_id, oid_id):
    return HttpResponse("Voce esta vendo o grafico %s do device %s" % oid_id % device_id)

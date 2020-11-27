from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from .models import Notification
# Create your views here.
import json
from django.core import serializers
def DisplayAll(request):

    note = {}
    id =1
    SomeModel_json = serializers.serialize("json", Notification.objects.all())
    data = {"SomeModel_json": SomeModel_json}
    for foo in Notification.objects.all():
        note[id]= {"namemsg":foo.name,"msg":foo.msg}
        id = 1+id

    return JsonResponse(note)

def DjangoAjax(request):


    return render(request,'DjangoAjax.html',context={})
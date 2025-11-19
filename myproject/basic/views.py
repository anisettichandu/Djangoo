from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from .models import Users


def sample(requests):
    return HttpResponse("hello world")

def SampleInfo(request):
    data={
        "name":"Chandu",
        "age":32,
        "place":"hyd"
    }
    return JsonResponse(data)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt   
def signup(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        user=Users.objects.create(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password')
            )
        return JsonResponse({"data":"success"},status=200)


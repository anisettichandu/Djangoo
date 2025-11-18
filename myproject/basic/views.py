from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def sample(requests):
    return HttpResponse("hello world")

def SampleInfo(request):
    data={
        "name":"Chandu",
        "age":32,
        "place":"hyd"
    }
    return JsonResponse(data)


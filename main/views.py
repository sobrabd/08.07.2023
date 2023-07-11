from django.shortcuts import render
from django.http import HttpResponse


def contacts(request):
    return render(request, 'main/contacts.html')


def name(request):
    name = request.POST["your_name"]
    return HttpResponse(f"i am {name}.")


def not_name(request):
    name = request.POST["your_name"]
    return HttpResponse(f"i am NOT {name}.")
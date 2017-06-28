from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


def view1(request):
    data1 = 111
    data2 = 222
    return render(request, 'apkt/view2.html',
                  {'data1': data1,})

def ts(request):
    return HttpResponse("You're looking at question")

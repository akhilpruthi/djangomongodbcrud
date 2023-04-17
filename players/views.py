from django.shortcuts import render
from django.http import request,response,HttpResponse
from django.shortcuts import render
from .models import Player


def home(request):
    return render(request,'addplayer.html')

def addplayers(request):
    if request.method=="POST":
        name = request.POST['player1']
        address = request.POST['player2']
        obj=Player.objects.create(name=name,address=address)
        obj.save()
        print("obj:::::",obj)
        return HttpResponse(obj)

    
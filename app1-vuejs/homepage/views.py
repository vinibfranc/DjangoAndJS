from django.shortcuts import render
from .models import Game
from django.core.serializers import serialize
from django.http import HttpResponse

def index(request):
    games = Game.objects.all()
    return render(request, "homepage/index.html", { 'games' : games })

def games(request):
    games = serialize("json", Game.objects.all())
    return HttpResponse(games, content_type="application/json")

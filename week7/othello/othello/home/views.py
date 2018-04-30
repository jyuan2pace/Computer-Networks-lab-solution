from django.shortcuts import render
from .models import gamer
from django.http import HttpResponse, Http404, JsonResponse
from random import randint
# Create your views here.

def index (request) :
	return render(request, "index.html", {})

def play (request) :
	token = randint(1,100)
	gamer.objects.create(token=token, count=1, turn=1)
	print(token)	
	return render(request, "home.html", {'token':token, 'you':1})


def join (request) :
	print(request.POST)
	token=request.POST['token']
	obj = gamer.objects.get(token=token)

	if obj.count == 2 :
		return render(request, "index.html", {})

	obj.count = 2
	obj.save()	
	# print(token)
	return render(request, "home.html", {'token':token, 'you':2})

def save (request) :
	print(request.POST)
	board = request.POST['board']
	token = request.POST['token']
	turn = request.POST['turn']
	x = gamer.objects.get(token=token)
	x.board=board
	x.turn=turn
	x.save()
	return HttpResponse("OK")

def check (request) :
	print(request.POST)
	token = request.POST['token']
	obj = gamer.objects.get(token=token)
	return JsonResponse({'token':token, 'turn':obj.turn, 'move':obj.board})
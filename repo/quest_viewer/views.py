from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('Test')

def discipline(request,discipline_id):
	return HttpResponse('ID used for discipline: %s' % discipline_id)

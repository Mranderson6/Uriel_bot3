from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404

def about (request):
   return render(request, 'about.html')
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404

def adhesion (request):
   return render(request, 'adhesion/index.html')

def adhesion_login(request):
   return render(request, 'adhesion/home/sign_up.html')
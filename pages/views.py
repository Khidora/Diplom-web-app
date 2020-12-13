from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm


def first_view(request):
   return render(request, 'pages/home.html', locals())

def second_view(request):
   return render(request, 'pages/about.html', locals())

def third_view(request):
   return render(request, 'pages/contacts.html', locals())


def fourth_view(request):
   return render(request, 'pages/interview.html', locals())

def five_view(request):
   return render(request, 'pages/resume.html', locals())

def five(request):
   return render(request, 'pages/register.html', locals())

def register(request):
   form = None
   if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid ():
         pass
   else:
      form = UserRegisterForm()
   context = {'form': form}
   return render(request, 'register.html', context)
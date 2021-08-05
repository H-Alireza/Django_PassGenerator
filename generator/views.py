from django.shortcuts import render
from django.http import HttpResponse
import random

def home (request):
     return render (request, 'generator/home.html')




def result (request):
      if request.GET.get('uppercase'):
          characters= list('abcdefghijklmnopqrstuvwxyz')
          characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

      if request.GET.get('special'):
          characters.extend(list('!@#$%^&*()'))

      if request.GET.get('numbers'):
         characters.extend(list('0123456789'))

      password=""
      length=int(request.GET.get('length'))
      for x in range (length):
          password += random.choice(characters)
      return render (request, 'generator/result.html' , {'password':password})

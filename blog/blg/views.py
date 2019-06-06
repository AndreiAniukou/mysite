from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def posts_list(request):
    n = ['Andrei', 'ellie', 'tanya']
    return render(request, 'blg/index.html', context={'names': n})
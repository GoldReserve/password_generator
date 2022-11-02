import random
from django.shortcuts import render
from django.http import HttpResponse
import string


# Create your views here.


def home(request):
    return render(request, 'generator/home.html')

def password(request):
    length = int(request.GET.get('length'), 12)
    characters = f'{string.ascii_lowercase}'
    digits = f'{string.digits}'
    special = f'{string.punctuation}'
    symbols = ''
    if request.GET.get('uppercase'):
        characters = [i.upper() if count % 2 else i for count, i in enumerate(characters)]
        symbols = ''.join(characters)
    else:
        symbols += characters
    if request.GET.get('numbers'):
        symbols += digits
    if request.GET.get('special'):
        symbols += special
    symbols = list(symbols)
    random.shuffle(symbols)
    password = ''
    for i in range(length):
        password += random.choice(symbols)
    return render(request, 'generator/password.html', {'password': password})

def about(request):
    return render(request, 'generator/about.html')
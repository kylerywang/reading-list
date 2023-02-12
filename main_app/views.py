from django.shortcuts import render
from .models import Media

# media =[
#     {'name': 'Elephant in the Brain', 'type': 'Book', 'author':'Kevin Simler & Robin Hanson', 'status':'finished','rating': 5, 'notes': 'great book'},
#     {'name': 'Elephant in the Brain', 'type': 'Book', 'author':'Kevin Simler & Robin Hanson', 'status':'finished','rating': 5, 'notes': 'great book'},
#     {'name': 'Elephant in the Brain', 'type': 'Book', 'author':'Kevin Simler & Robin Hanson', 'status':'finished','rating': 5, 'notes': 'great book'},
#     {'name': 'Elephant in the Brain', 'type': 'Book', 'author':'Kevin Simler & Robin Hanson', 'status':'finished','rating': 5, 'notes': 'great book'},
# ]

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'home.html')

def media_index(request):
    media= Media.objects.all()
    return render(request,'media/index.html',{
        'media': media
    })
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

def media_detail(request, media_id):
    media = Media.objects.get(id=media_id)

    return render(request, 'media/detail.html',{
        'media': media
    })

class MediaCreate(CreateView):
    model = Media
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)


class MediaUpdate(UpdateView):
    model = Media
    fields = '__all__'

class MediaDelete(DeleteView):
    model = Media
    succes_url = '/cats'
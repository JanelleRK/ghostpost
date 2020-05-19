from django.shortcuts import render
from ghostapp.models import GhostPost

# Create your views here.
def index(request):
    posts = GhostPost.objects.all()
    return render(request, 'index.html', { 'posts': posts})


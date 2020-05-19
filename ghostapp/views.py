from django.shortcuts import render, reverse, HttpResponseRedirect
from ghostapp.models import GhostPost

# Create your views here.
def index(request):
    posts = GhostPost.objects.all()
    return render(request, 'index.html', { 'posts': posts})

def up_vote(request, id):
    up_post = GhostPost.objects.get(pk=id)
    up_post.score += 1
    up_post.save()
    return HttpResponseRedirect(reverse('homepage'))

def down_vote(request, id):
    down_post = GhostPost.objects.get(pk=id)
    down_post.score -= 1
    down_post.save()
    return HttpResponseRedirect(reverse('homepage'))
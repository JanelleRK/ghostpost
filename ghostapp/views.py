from django.shortcuts import render, reverse, HttpResponseRedirect
from ghostapp.models import GhostPost
from ghostapp.forms import GhostPostForm

# Create your views here.
def index(request):
    posts = GhostPost.objects.all().order_by('-date')
    return render(request, 'index.html', { 'posts': posts})


def add_ghost_post(request):
    #help from Matt
    html = "addghostpost.html"

    if request.method == "POST":
        form = GhostPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GhostPost.objects.create(
                post_input = data['post_input'],
                boast = data['boast']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = GhostPostForm()

    return render(request, html, {"form": form})


def up_vote(request, id):
    #http://www.cs.virginia.edu/~evans/cs1120-f09/ps/project/django.html
    up_post = GhostPost.objects.get(id=id)
    up_post.up_vote += 1
    up_post.sum_of_votes += 1
    up_post.save()
    return HttpResponseRedirect(reverse('homepage'))


def down_vote(request, id):
    down_post = GhostPost.objects.get(id=id)
    down_post.down_vote += 1
    down_post.sum_of_votes -= 1
    down_post.save()
    return HttpResponseRedirect(reverse('homepage'))


def roast(request):
    html='roast.html'
    roasts = GhostPost.objects.all().filter(boast=False).order_by('-date')
    return render(request, html, { 'roasts': roasts})

def boast(request):
    html='boast.html'
    boasts = GhostPost.objects.all().filter(boast=True).order_by('-date')
    return render(request, html, { 'boasts': boasts })


def sum_of_votes_view(request):
    html='voting.html'
    posts = GhostPost.objects.order_by('-sum_of_votes')
    return render(request, html, { 'posts': posts })
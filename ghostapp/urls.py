
from django.urls import path
from ghostapp import views

urlpatterns = [
    path('', views.index),
    path(r'^upvote/(?P<id>[0-9]+)/$', views.up_vote, name='upvote'),
]
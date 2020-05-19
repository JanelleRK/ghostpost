from django.db import models
from django.utils import timezone

# Create your models here.
class GhostPost(models.Model):
    post_input = models.CharField(max_length=100)
    #Boolean??
    #up_vote = models.IntegerField()
    #down_vote = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)



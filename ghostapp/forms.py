from django import forms

class AddGhostPostForm(forms.Form):
    post_input = forms.CharField(max_length=100)







"""

class GhostPost(models.Model):
    post_input = models.CharField(max_length=100)
    #Boolean??
    #up_vote = models.IntegerField(default=0)
    #down_vote = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_input



"""


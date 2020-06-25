
from django.urls import path
from ghostapp import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('post/', views.add_ghost_post),
    path('up_vote/<int:id>/', views.up_vote),
    path('down_vote/<int:id>/', views.down_vote),
    path('roasts/', views.roast),
    path('boasts/', views.boast),
    path('voting/', views.sum_of_votes_view)

]
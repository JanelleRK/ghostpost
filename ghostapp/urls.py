
from django.urls import path
from ghostapp import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('post/', views.add_ghost_post),
    path('up_vote/<int:id>/', views.up_vote),
    path('down_vote/<int:id>/', views.down_vote),
    path('roast/', views.is_roast),
    path('boast/', views.is_boast)

]
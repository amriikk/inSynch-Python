from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    

    path('<str:mood>/', views.songs_mood, name='mood'),
    path('songs/create/', views.SongCreate.as_view(), name='songs_create'),
    path('<str:pk>/update/', views.SongUpdate.as_view(), name='songs_update'),
]
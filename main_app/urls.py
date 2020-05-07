from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    

    path('<str:mood>/', views.songs_mood, name='mood'),
    path('songs/create/', views.SongCreate.as_view(), name='songs_create'),
    path('<str:pk>/update/', views.SongUpdate.as_view(), name='songs_update'),
    path('<str:pk>/delete/', views.SongDelete.as_view(), name='songs_delete'),
    path('<str:song_id>/voteagree/', views.vote_agree, name='vote_agree'),
    path('<str:song_id>/votedisagree/', views.vote_disagree, name='vote_disagree'),
]
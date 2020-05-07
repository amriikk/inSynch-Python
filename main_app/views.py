from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Song
from .spotify import SpotifyAPI
from django.contrib.auth.mixins import LoginRequiredMixin



# Define the home view
def home(request):
  # print(SpotifyAPI.get_token_data(self)) include self in params above
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')

class SongCreate(LoginRequiredMixin, CreateView):
  model = Song
  fields = ['name', 'band', 'mood']
  
  def form_valid(self, form):
    form.instance.posted_by = self.request.user
    # return redirect('mood', mood=form.instance.mood)
    return super().form_valid(form)


def vote_agree(request, song_id):
  song = Song.objects.get(id=song_id)
  song.agree += 1
  song.save()
  #return redirect('mood', {'mood': song.mood})
  songs = Song.objects.filter(mood=song.mood)
  return render(request, 'index.html', { 'songs': songs , 'mood': song.mood })

def vote_disagree(request, song_id):
  song = Song.objects.get(id=song_id)
  song.disagree += 1
  song.save()
  songs = Song.objects.filter(mood=song.mood)
  return render(request, 'index.html', { 'songs': songs , 'mood': song.mood })

def songs_mood(request, mood):
  songs = Song.objects.filter(mood=mood)
  print(songs)
  return render(request, 'index.html', { 'songs': songs , 'mood': mood })

class SongUpdate(LoginRequiredMixin, UpdateView):
  model = Song
  fields = ['name', 'band', 'mood']

class SongDelete(LoginRequiredMixin, DeleteView):
  model = Song
  success_url = '/'


def accounts(request):
  return render(request, 'registration/login.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again!'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)    
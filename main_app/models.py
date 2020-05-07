from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

MOODS = (
    ('angry', 'angry'),
    ('melancholy', 'melancholy'),
    ('cheerful', 'cheerful'),
    ('calm', 'calm'),
    ('romantic', 'romantic'),
    ('mysterious', 'mysterious')
)



class Song(models.Model):
    name = models.CharField(max_length=100)
    band = models.CharField(max_length=100)
    mood = models.CharField(max_length=20,choices=MOODS,default=MOODS[0][0])
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    agree = models.IntegerField(default=0)
    disagree = models.IntegerField(default=0)
    

    def __str__(self):
        return f"{self.name} by {self.band}"

    def get_absolute_url(self):
        return reverse('home')

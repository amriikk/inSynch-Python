from django.db import models
from django.contrib.auth.models import User

# Create your models here.

MOODS = (
    ('A', 'Angry'),
    ('B', 'Melancholy'),
    ('C', 'Cheerful'),
    ('D', 'Calm'),
    ('E', 'Romantic'),
    ('F', 'Mysterious')
)

class Song(models.Model):
    mood = models.CharField(
        max_length=1,
        choices=MOODS,
        default=MOODS[0][0]
    )
    name = models.CharField(max_length=100)
    band = models.CharField(max_length=100)
    


	# def __str__(self):
    #     return f"{self.name} on {self.band}"
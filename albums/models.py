from django.db import models
from musics.models import Music

# Create your models here.
album_rating=[(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')]

class Album(models.Model):
    album_name=models.CharField(max_length=12)
    release_date=models.DateField()
    rating=models.PositiveSmallIntegerField(choices=album_rating)
    musician=models.OneToOneField(Music, on_delete=models.CASCADE, default= None)

    def __str__(self):
        return self.album_name
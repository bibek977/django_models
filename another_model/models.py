from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class FemArtist(models.Model):
    fname = models.CharField(max_length=200)
    def __str__(self):
        return self.fname

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.OneToOneField(Artist,on_delete=models.CASCADE)
    fArtist = models.ManyToManyField(FemArtist)
    def __str__(self):
        return self.title

class Cocert(models.Model):
    location = models.CharField(max_length=200)
    artist = models.ManyToManyField(Artist)
    fArtist = models.ManyToManyField(FemArtist)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)
    def __str__(self):
        return self.location
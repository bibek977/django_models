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
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    fArtist = models.ForeignKey(FemArtist,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Cocert(models.Model):
    location = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    fArtist = models.ForeignKey(FemArtist,on_delete=models.CASCADE)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)

    def __str__(self):
        return self.location
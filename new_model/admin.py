from django.contrib import admin
from .models import *

class ArtistAdminModel(admin.ModelAdmin):
    list_display = ['id','name']

class FemArtistAdminModel(admin.ModelAdmin):
    list_display = ['id','fname']
    
class AlbumAdminModel(admin.ModelAdmin):
    list_display = ['id','title']

class CocertAdminModel(admin.ModelAdmin):
    list_display = ['id','location']

admin.site.register(Artist,ArtistAdminModel)
admin.site.register(FemArtist,FemArtistAdminModel)
admin.site.register(Album,AlbumAdminModel)
admin.site.register(Cocert,CocertAdminModel)
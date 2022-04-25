from django.contrib import admin
from . models import Gig, Song, User, Setlist

# Register your models here.
admin.site.register(Gig)
admin.site.register(Song)
admin.site.register(User)
admin.site.register(Setlist)


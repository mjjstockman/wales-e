from django.shortcuts import render
from . forms import SetlistForm

# Create your views here.
def createSetlist(request):
    form = SetlistForm()
    context = {'form': form}
    return render(request, 'appone/create-setlist.html', context)
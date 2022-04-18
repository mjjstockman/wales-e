from django.shortcuts import render

# Create your views here.
def create_setlist(request):
    """ view to return index page """
    return render(request, 'appone/create-setlist.html')
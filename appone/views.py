from django.shortcuts import render, redirect
from . forms import SetlistForm
from . models import Setlist

# Create your views here.
def createSetlist(request):
    form = SetlistForm()
    if request.method == 'POST':
        # print(request.POST)
        form = SetlistForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('home')

    context = {'form': form}
    return render(request, 'appone/create-setlist.html', context)


def setlist(request):
    setlists = Setlist.objects.all()
    context = {'setlists': setlists}
    return render(request, 'appone/setlist.html', context)


def updateSetlist(request, pk):
    setlist = Setlist.objects.get(id=pk)
    form = SetlistForm(instance=setlist)

    if request.method == 'POST':
        form = SetlistForm(request.POST, instance=setlist)
        if form.is_valid():
            form.save()
            # return redirect('home')

    context = {'form': form}
    
    return render(request, 'appone/create-setlist.html', context)


def deleteSetlist(request, pk):
    setlist = Setlist.objects.get(id=pk)
    if request.method == 'POST':
        setlist.delete()
        # return redirect('home')
        
    # setlist = Setlist.objects.get(id=pk)
    # form = SetlistForm(instance=setlist)

    # if request.method == 'POST':
    #     form = SetlistForm(request.POST, instance=setlist)
    #     if form.is_valid():
    #         form.save()
    #         # return redirect('home')

    context = {}
    
    return render(request, 'appone/delete-setlist.html', {'setlist': setlist})

from django.http.request import HttpRequest
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from shows.models import Network, Show

# Create your views here.
def index(request):
    return redirect(reverse("my_shows"))

def shows(request):
    shows = Show.objects.all()
    
    context = {
        'all_shows': shows
    }
    return render(request, "shows.html", context)

def new(request):
    # getting networks
    all_networks = Network.objects.all().order_by("title")
    
    context = {
        'all_networks': all_networks
    }
    
    return render(request, "new.html", context)

def edit(request, show_id):
    this_show = Show.objects.get(id=show_id)
    all_networks = Network.objects.all().order_by("title")
    
    context = {
        'this_show': this_show,
        'all_networks': all_networks
    }
    return render(request, "edit.html", context)

def view(request, show_id):
    this_show = Show.objects.get(id=show_id)
    
    context = {
        'this_show': this_show,
    }
    return render(request, "view.html", context)

def create(request):
    print (request.POST)
    
    # getting form variables
    show_title = request.POST['show_title']
    show_network = request.POST['show_network']
    show_date = request.POST['show_date']
    show_description = request.POST['show_description']
    
    # getting a network instance
    this_network = Network.objects.get(id=show_network)
    
    # create the show instance using the network object
    this_show = Show.objects.create(title=show_title, description=show_description, release_date=show_date, network =this_network)
    
    return redirect(reverse("my_shows"))

def update(request, show_id):
    # getting form variables
    show_title = request.POST['show_title']    
    show_network = Network.objects.get(id=request.POST['show_network'])
    show_date = request.POST['show_date']
    show_description = request.POST['show_description']
    
    # updating show
    show_to_update= Show.objects.get(id=show_id)
    show_to_update.title = show_title
    show_to_update.network = show_network
    show_to_update.release_date = show_date
    show_to_update.description = show_description
    show_to_update.save()
    
    # once updated, redirect to homepage (shows)
    return redirect(reverse("my_shows"))

def destroy(request, show_id):    
    # deleting show
    show_to_delete= Show.objects.get(id=show_id)
    show_to_delete.delete()
    
    # once updated, redirect to homepage (shows)
    return redirect(reverse("my_shows"))
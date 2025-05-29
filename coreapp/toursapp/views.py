from django.shortcuts import render
from django.conf import settings
from .models import Tour
import requests

eventbriteRequest = requests.get("")
eventbriteData = eventbriteRequest.json()

cdn = settings.CDN_URL

# ----- MAIN PAGES ----- #

def home(request):
    return render(request, 'tourapp/index.html')

# query the db for all tours, context is a dictionary that will be passed to the template
def tours(request):
    tours = Tour.objects.all()
    context = {
        'tours': tours
    }
    return render(request, 'tourapp/tour-packages.html', context)

def about(request):
    return render(request, 'tourapp/about.html')

def contact(request):
    return render(request, 'tourapp/contact.html')


# ----- OTHER PAGES ----- #

def terms(request):
    return render(request, 'tourapp/terms.html')

def privacy(request):
    return render(request, 'tourapp/privacy.html')


# ----- ERROR PAGES ----- #

def error_404(request, exception):
    return render(request, 'tourapp/404.html')
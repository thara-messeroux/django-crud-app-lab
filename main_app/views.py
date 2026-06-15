from django.shortcuts import render
from .models import Discovery


def home(request):
    # Shows the TrailTales homepage.
    return render(request, 'home.html')


def discovery_index(request):
    # Gets all discoveries so users can scan their trail journal.
    discoveries = Discovery.objects.all().order_by('-date_seen')

    # Sends discovery data to the index page.
    return render(request, 'discoveries/index.html', {
        'discoveries': discoveries
    })
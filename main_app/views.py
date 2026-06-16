from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DiscoveryForm
from .models import Discovery


def home(request):
    # Shows the TrailTales landing page.
    return render(request, 'home.html')


@login_required
def discovery_index(request):
    # Shows only the logged-in user's discoveries for privacy and ownership.
    discoveries = Discovery.objects.filter(user=request.user).order_by('-date_seen')

    return render(request, 'discoveries/index.html', {
        'discoveries': discoveries
    })


@login_required
def discovery_detail(request, discovery_id):
    # Finds one discovery, but only if it belongs to the logged-in user.
    discovery = get_object_or_404(Discovery, id=discovery_id, user=request.user)

    return render(request, 'discoveries/detail.html', {
        'discovery': discovery
    })


@login_required
def discovery_create(request):
    # Handles both showing the form and saving a new discovery.
    if request.method == 'POST':
        form = DiscoveryForm(request.POST)

        if form.is_valid():
            # Save later so we can attach the logged-in user first.
            discovery = form.save(commit=False)
            discovery.user = request.user
            discovery.save()
            return redirect('discovery-detail', discovery_id=discovery.id)
    else:
        form = DiscoveryForm()

    return render(request, 'discoveries/form.html', {
        'form': form,
        'page_title': 'Add Discovery',
        'button_text': 'Save discovery'
    })


@login_required
def discovery_update(request, discovery_id):
    # Allows users to edit only their own discovery.
    discovery = get_object_or_404(Discovery, id=discovery_id, user=request.user)

    if request.method == 'POST':
        form = DiscoveryForm(request.POST, instance=discovery)

        if form.is_valid():
            form.save()
            return redirect('discovery-detail', discovery_id=discovery.id)
    else:
        form = DiscoveryForm(instance=discovery)

    return render(request, 'discoveries/form.html', {
        'form': form,
        'page_title': 'Edit Discovery',
        'button_text': 'Update discovery'
    })


@login_required
def discovery_delete(request, discovery_id):
    # Allows users to delete only their own discovery.
    discovery = get_object_or_404(Discovery, id=discovery_id, user=request.user)

    if request.method == 'POST':
        discovery.delete()
        return redirect('discovery-index')

    return render(request, 'discoveries/confirm_delete.html', {
        'discovery': discovery
    })


def signup(request):
    # Creates a new account, then logs the user in right away.
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('discovery-index')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {
        'form': form
    })

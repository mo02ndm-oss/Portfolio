from django.shortcuts import render, get_object_or_404
from .models import Profile, Project

def portfolio_details(request, username_slug):
    profile = get_object_or_404(Profile, slug=username_slug)
    projects = profile.projects.filter(is_visible=True).prefetch_related('attachments')
    return render(request, 'core/home.html', {
        'profile': profile,
        'projects': projects,
    })

def home(request):
    # Generic landing page without profile listings
    return render(request, 'core/landing.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, Experience
from .forms import FeedbackForm


def profile(request):
    pic = Profile.objects.all()
    exp = Experience.objects.all()

    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():  # Correctly calling is_valid() method on the form instance
            form.save()
            return redirect('profile')  # Assuming 'profile' is the name of the URL pattern for this view
    else:
        form = FeedbackForm()

    context = {
        'pic': pic,
        'exp': exp,
        'form': form
    }
    return render(request, 'inde.html', context)


def new(request):
    exp = Experience.objects.all()

    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():  # Correctly calling is_valid() method on the form instance
            form.save()
            return redirect('profile')  # Assuming 'profile' is the name of the URL pattern for this view
    else:
        form = FeedbackForm()

    context = {
        'exp': exp,
        'form': form
    }
    return render(request, 'contact.html', context)


def map_view(request):
    return render(request, 'location.html')


def home(request):
    return render(request, 'HOME.html')

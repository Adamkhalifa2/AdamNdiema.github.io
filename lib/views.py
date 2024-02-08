from django.shortcuts import render, redirect
from .models import Resources  # Import Resources model
from .forms import ResourcesForm  # Import ResourcesForm

def index(request):
    # Fetch all books from the database
    books = Resources.objects.all()
    context = {
        'books': books
    }
    return render(request, 'index.html', context)

def book_upload(request):
    if request.method == 'POST':
        form = ResourcesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the index page after successful form submission
    else:
        form = ResourcesForm()
    context = {
        'form': form
    }
    return render(request, 'resourceupload.html', context)

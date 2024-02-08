from django.shortcuts import render
from .models import Student, ImageYangu

def recap_view(request):
    students = Student.objects.all()
    images = ImageYangu.objects.all()
    context = {
        'students': students,
        'images': images  # corrected variable name
    }
    return render(request, 'rock.html', context)

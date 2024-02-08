from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("My name is Adam Ndiema")

def rock(request):
    student = Student.objects.all().values()
    context ={
        'student': student
    }
    return render(request,context, 'rock.html')

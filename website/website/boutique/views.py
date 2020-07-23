from django.shortcuts import render
from django.http import HttpResponse

from .models import Course, User, Formation, Inspiration


def index(request):
    user_list = User.objects.all()
    inspiration_list = Inspiration.objects.all()
    context = {'user_list': user_list, 'inspiration_list' : inspiration_list}
    return render(request, 'boutique/index.html', context)

def assessment(request):
    context = {}
    return render(request, 'boutique/assessment.html', context)

def trainings(request):
    course_list = Course.objects.all()
    context = {'course_list': course_list}
    return render(request, 'boutique/trainings.html', context)

def course(request, name):
    course = Course.objects.get(course_name=name)
    context = {'course': course}
    return render(request, 'boutique/course.html', context)

def consulting(request):
    context = {}
    return render(request, 'boutique/consulting.html', context)

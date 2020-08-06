from django.shortcuts import render
from django.http import HttpResponse

from .models import Course, User, Formation, Inspiration, CourseReview, CourseInstance
import json
import jsonpickle

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
    inspiration_list = Inspiration.objects.all()
    course_reviews = CourseReview.objects.filter(course=course)
    context = {'course': course, 'inspiration_list' : inspiration_list, 'course_reviews': course_reviews}
    return render(request, 'boutique/course.html', context)

def calendar(request):
    instances_list = CourseInstance.objects.order_by('date')
    context = {'instances_list_wierd': jsonpickle.encode(instances_list, unpicklable=False), 'instances_list': instances_list}
    return render(request, 'boutique/calendar.html', context)

def consulting(request):
    context = {}
    return render(request, 'boutique/consulting.html', context)

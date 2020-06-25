from django.shortcuts import render
from django.http import HttpResponse

from .models import Course, User, Formation

def index(request):
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return render(request, 'boutique/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-uptaded_at')
    context = {'tasks': tasks}
    return render(request, 'home.html', context)
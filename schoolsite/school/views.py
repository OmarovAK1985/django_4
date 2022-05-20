from django.shortcuts import render
from .models import Teacher


def school_list(request):
    teachers = Teacher.objects.all()
    values = {
        'teachers': teachers,
        'title': 'Список учеников и учителей'
    }
    return render(request, 'school/index.html', values)



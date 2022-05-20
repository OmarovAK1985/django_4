import os
from django.core.management.base import BaseCommand
import json
from school.models import Teacher, Student


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        name_teacher = Teacher.objects.all()
        for i in name_teacher:
            Teacher.delete(i)

        name_students = Student.objects.all()
        for i in name_students:
            Student.delete(i)

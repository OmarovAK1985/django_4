import os
from django.core.management.base import BaseCommand
import json
from school.models import Teacher, Student


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        teacher_list = []
        student_list = []
        file = os.path.join(os.getcwd(), 'school.json')
        with open(file, mode='r', encoding='utf-8') as file_json:
            read = json.load(file_json)
            for i in read:
                if i['model'] == 'school.teacher':
                    teacher_list.append(i)
                elif i['model'] == 'school.student':
                    student_list.append(i)
        teacher_number_list = []
        for i in teacher_list:
            for k, v in i.items():
                teacher_number = i['pk']
                if len(Teacher.objects.all()) == 0:
                     Teacher.objects.create(name=i['fields']['name'], subject=i['fields']['subject'],
                                           teacher_number=teacher_number)
                elif len(Teacher.objects.all()) > 0:
                    for teacher_number_from_model in Teacher.objects.all():
                        teacher_number_list.append(teacher_number_from_model.teacher_number)
                    if teacher_number not in teacher_number_list:
                        Teacher.objects.create(name=i['fields']['name'], subject=i['fields']['subject'],
                                                   teacher_number=teacher_number)

        for i in student_list:
            student_number_list = []
            teacher_number = i['fields']['teacher']
            teacher = Teacher.objects.get(teacher_number = teacher_number)
            students = Student.objects.all()
            name = i['fields']['name']
            group = i['fields']['group']
            student_number = i['pk']
            if len(students)==0:
                teacher.student.create(name=name, group=group, student_number=student_number)
            elif len(students) > 0:
                for student_number_from_model in students:
                    student_number_list.append(student_number_from_model.student_number)
                if student_number not in student_number_list:
                    teacher.student.create(name=name, group=group, student_number=student_number)















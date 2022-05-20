from django.contrib import admin
from .models import Teacher, Student, Student_teacher


class Student_teacher_inline(admin.TabularInline):
    model = Student_teacher
    extra = 3


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['teacher_number', 'name', 'subject']
    list_filter = ['name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_number', 'name', 'group']
    inlines = [Student_teacher_inline,]
    list_filter = ['teacher']










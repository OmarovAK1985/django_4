# Generated by Django 4.0.4 on 2022-05-19 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacher_number',
            field=models.IntegerField(default=1),
        ),
    ]

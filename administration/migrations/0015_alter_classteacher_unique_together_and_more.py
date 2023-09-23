# Generated by Django 4.1 on 2023-09-23 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_alter_teachersattendance_teacher_and_more'),
        ('administration', '0014_academicyear_day_school_delete_classjournal'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='classteacher',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='classteacher',
            name='class_section',
        ),
        migrations.RemoveField(
            model_name='classteacher',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='ClassSection',
        ),
        migrations.DeleteModel(
            name='ClassTeacher',
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-11 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_studentprofile_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherprofile',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='StudentProfile',
        ),
        migrations.DeleteModel(
            name='TeacherProfile',
        ),
    ]

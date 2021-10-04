# Generated by Django 4.0.dev20210910103700 on 2021-10-04 12:25

import Class.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Course', '0002_alter_coursematerial_course'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.course')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tutor')),
            ],
        ),
        migrations.CreateModel(
            name='ClassActivity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default='04/10/2021 19:25:31')),
                ('submitted_date', models.DateTimeField(blank=True, null=True)),
                ('is_assignment', models.BooleanField(default=False)),
                ('class_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Class.class')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityMaterial',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('file', models.FileField(upload_to=Class.models.file_directory_path)),
                ('class_activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Class.classactivity')),
            ],
        ),
    ]

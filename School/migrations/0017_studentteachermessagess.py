# Generated by Django 5.0.6 on 2024-06-07 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0016_auto_20240607_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTeacherMessagess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sent_Message_Studentt', models.CharField(max_length=250)),
                ('Received_Message_Student', models.CharField(max_length=250)),
                ('Message_Student_ID', models.IntegerField(unique=True)),
                ('Sent_Message_Teacher', models.CharField(max_length=250)),
                ('Received_Message_Teacher', models.CharField(max_length=250)),
                ('Message_Teacher_ID', models.IntegerField(unique=True)),
                ('Message_Date', models.CharField(max_length=250)),
                ('Message_Hour', models.IntegerField()),
                ('Message_Minute', models.IntegerField()),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.studentinformation')),
                ('Teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School.teacherinformation')),
            ],
        ),
    ]

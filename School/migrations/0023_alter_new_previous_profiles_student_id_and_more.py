# Generated by Django 5.0.6 on 2024-06-08 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('School', '0022_new_previous_profiles_delete_profiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_previous_profiles',
            name='Student_ID',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='new_previous_profiles',
            name='Teacher_ID',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-23 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the Project.', max_length=110)),
                ('creation_time', models.DateTimeField(auto_now_add=True, help_text='The is creatig time')),
                ('completion_time', models.DateTimeField(help_text='The is completion time')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the Task.', max_length=110)),
                ('description', models.TextField(help_text='  ')),
                ('time_estimate', models.IntegerField(help_text='  ')),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-24 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the Project.', max_length=100)),
                ('creation_time', models.DateTimeField(auto_now_add=True, help_text='The date and time the project was created.')),
                ('completion_time', models.DateTimeField(help_text='The date and time the project was completed.', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text=' Title of the Task.', max_length=100)),
                ('description', models.TextField(help_text='description of the Task.')),
                ('time_estimate', models.IntegerField(help_text=' estimate for the Task.')),
                ('completed', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PMApp.project')),
            ],
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-15 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_rename_stud1_stud'),
    ]

    operations = [
        migrations.CreateModel(
            name='stud2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
# Generated by Django 3.0.8 on 2020-08-15 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('marks', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]
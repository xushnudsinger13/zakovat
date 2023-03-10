# Generated by Django 4.1 on 2022-12-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255)),
                ('team_name', models.CharField(max_length=50, unique=True)),
                ('username', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
                ('choice', models.IntegerField(choices=[(1, "Ro'yhatdan o'tgan"), (2, "Ro'yhatdan o'tmagan")], default=1)),
            ],
        ),
    ]

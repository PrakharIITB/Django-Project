# Generated by Django 4.0.4 on 2022-05-10 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamId', models.CharField(max_length=50)),
                ('teamName', models.CharField(max_length=50)),
                ('player1', models.TextField()),
                ('player2', models.TextField()),
                ('player3', models.TextField()),
                ('player4', models.TextField()),
            ],
        ),
    ]

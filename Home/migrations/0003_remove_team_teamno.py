# Generated by Django 4.0.4 on 2022-05-11 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_team_teamno_alter_team_player1_alter_team_player2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='teamNo',
        ),
    ]

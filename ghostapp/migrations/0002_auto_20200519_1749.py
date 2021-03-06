# Generated by Django 3.0.6 on 2020-05-19 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ghostpost',
            name='down_vote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ghostpost',
            name='post_type',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ghostpost',
            name='sum_of_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ghostpost',
            name='up_vote',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ghostpost',
            name='post_input',
            field=models.CharField(max_length=150),
        ),
    ]

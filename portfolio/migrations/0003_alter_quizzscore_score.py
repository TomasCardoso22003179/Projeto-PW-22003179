# Generated by Django 3.2.13 on 2022-05-28 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_quizz_quizzscore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizzscore',
            name='score',
            field=models.IntegerField(),
        ),
    ]

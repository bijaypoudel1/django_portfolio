# Generated by Django 4.0 on 2021-12-27 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_expertteam_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertteam',
            name='facebook',
            field=models.CharField(default='#', max_length=50),
        ),
        migrations.AddField(
            model_name='expertteam',
            name='instagram',
            field=models.CharField(default='#', max_length=50),
        ),
        migrations.AddField(
            model_name='expertteam',
            name='twitter',
            field=models.CharField(default='#', max_length=50),
        ),
    ]

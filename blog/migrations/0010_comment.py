# Generated by Django 4.0 on 2021-12-30 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]

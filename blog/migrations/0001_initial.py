# Generated by Django 4.0 on 2021-12-29 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=20)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
    ]
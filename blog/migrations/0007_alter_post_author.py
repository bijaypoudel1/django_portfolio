# Generated by Django 4.0 on 2021-12-29 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default='Admin', max_length=20),
        ),
    ]

# Generated by Django 4.0 on 2021-12-29 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Category',
            new_name='category',
        ),
    ]

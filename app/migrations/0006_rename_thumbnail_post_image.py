# Generated by Django 4.2.5 on 2023-09-28 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_post_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='thumbnail',
            new_name='image',
        ),
    ]

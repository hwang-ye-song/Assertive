# Generated by Django 4.0 on 2022-12-12 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_post_board'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='read',
        ),
    ]
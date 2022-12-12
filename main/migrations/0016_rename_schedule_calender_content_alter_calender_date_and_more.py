# Generated by Django 4.0 on 2022-12-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0015_delete_cctv_delete_park'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calender',
            old_name='schedule',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='calender',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
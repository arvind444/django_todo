# Generated by Django 3.2.5 on 2021-07-19 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0004_alter_list_date_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='date_completed',
        ),
    ]
# Generated by Django 3.2.5 on 2021-07-15 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_alter_list_date_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='date_completed',
            field=models.DateTimeField(),
        ),
    ]
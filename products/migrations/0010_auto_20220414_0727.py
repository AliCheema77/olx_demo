# Generated by Django 3.2.9 on 2022-04-14 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_chat_group'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]

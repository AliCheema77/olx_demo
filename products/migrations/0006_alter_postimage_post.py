# Generated by Django 3.2.9 on 2022-04-05 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_images', to='products.post'),
        ),
    ]

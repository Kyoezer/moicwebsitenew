# Generated by Django 3.0 on 2022-04-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0008_auto_20220413_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='image_slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, upload_to='pics')),
            ],
        ),
    ]
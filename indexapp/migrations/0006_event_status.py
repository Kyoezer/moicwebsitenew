# Generated by Django 3.0 on 2022-04-27 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0005_event_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(blank='True', choices=[('draft', 'Draft'), ('publish', 'Publish')], max_length=100, null='True'),
            preserve_default='True',
        ),
    ]
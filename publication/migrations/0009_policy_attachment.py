# Generated by Django 3.0 on 2022-04-26 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0008_auto_20220420_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
    ]
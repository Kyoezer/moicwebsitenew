# Generated by Django 3.0 on 2022-04-20 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='post_views', to='indexapp.IpModel'),
        ),
    ]
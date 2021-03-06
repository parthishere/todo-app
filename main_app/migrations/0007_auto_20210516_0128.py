# Generated by Django 3.1.7 on 2021-05-15 19:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210425_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='end_time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='todomodel',
            name='start_time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='end_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='start_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]

# Generated by Django 2.2.7 on 2019-12-17 04:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inside', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sai',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
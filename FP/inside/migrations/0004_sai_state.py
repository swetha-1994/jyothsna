# Generated by Django 2.2.7 on 2019-12-17 07:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inside', '0003_sai_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sai',
            name='state',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-02 10:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afroholichome', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='first_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(upload_to='static/images/project/ '),
        ),
    ]
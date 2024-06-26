# Generated by Django 5.0.3 on 2024-06-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afroholichome', '0007_alter_upcomingproject1_artist_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='merch1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merch_name', models.CharField(max_length=25)),
                ('merch_image', models.ImageField(upload_to='static/images/merch/')),
                ('merch_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='merch2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merch_name', models.CharField(max_length=25)),
                ('merch_image', models.ImageField(upload_to='static/images/merch/')),
                ('merch_link', models.URLField()),
            ],
        ),
    ]

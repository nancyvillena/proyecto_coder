# Generated by Django 4.0.6 on 2022-07-20 18:43

from django.db import migrations, models
import django.db.models.fields.files


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0002_alter_film_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='poster',
            field=models.ImageField(default=django.db.models.fields.files.ImageField, upload_to=''),
        ),
    ]

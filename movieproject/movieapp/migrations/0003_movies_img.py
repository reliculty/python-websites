# Generated by Django 4.2.2 on 2023-06-30 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movies'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='img',
            field=models.ImageField(default='brrod', upload_to=''),
            preserve_default=False,
        ),
    ]

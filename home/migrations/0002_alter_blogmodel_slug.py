# Generated by Django 3.2.16 on 2023-01-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, null=True),
        ),
    ]
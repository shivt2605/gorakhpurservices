# Generated by Django 4.2.3 on 2023-07-29 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_alter_response_submitter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_info',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
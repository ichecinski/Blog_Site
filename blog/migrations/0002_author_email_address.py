# Generated by Django 4.1.7 on 2023-04-04 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email_address',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
    ]

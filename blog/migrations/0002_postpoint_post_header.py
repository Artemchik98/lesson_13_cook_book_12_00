# Generated by Django 3.1.4 on 2021-01-30 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpoint',
            name='post_header',
            field=models.CharField(default='HEADER', max_length=250),
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='vid_id',
            field=models.CharField(default='000', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]

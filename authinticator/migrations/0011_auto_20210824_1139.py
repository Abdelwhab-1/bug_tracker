# Generated by Django 3.2.6 on 2021-08-24 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authinticator', '0010_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_demo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profils/%Y/%m/%d '),
        ),
    ]
# Generated by Django 3.2.6 on 2021-08-24 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_auto_20210823_0738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='Priority',
            new_name='priority',
        ),
    ]

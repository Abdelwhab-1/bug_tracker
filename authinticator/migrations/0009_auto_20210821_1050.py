# Generated by Django 3.2.6 on 2021-08-21 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authinticator', '0008_alter_ticket_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='developers',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_manager',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='project',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]

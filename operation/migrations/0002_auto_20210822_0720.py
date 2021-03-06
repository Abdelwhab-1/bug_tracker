# Generated by Django 3.2.6 on 2021-08-22 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='replies_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operation.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='solution_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solution', to='operation.ticket'),
        ),
    ]

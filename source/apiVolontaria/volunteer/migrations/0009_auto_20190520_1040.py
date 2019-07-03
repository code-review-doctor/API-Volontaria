# Generated by Django 2.1.5 on 2019-07-03 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0008_cell_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='task_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='volunteer.TaskType', verbose_name='Task type'),
        ),
    ]
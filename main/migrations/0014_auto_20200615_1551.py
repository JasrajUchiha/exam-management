# Generated by Django 3.0.5 on 2020-06-15 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200612_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='student_group',
            field=models.ManyToManyField(related_name='exam', to='main.Special_Students'),
        ),
    ]

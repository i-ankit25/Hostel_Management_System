# Generated by Django 2.1.2 on 2020-05-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0004_auto_20200514_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='course',
            field=models.ManyToManyField(blank=True, default=None, related_name='hostels', to='selection.Course'),
        ),
    ]

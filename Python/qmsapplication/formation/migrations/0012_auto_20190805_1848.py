# Generated by Django 2.2 on 2019-08-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0011_meetingminuts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingminuts',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

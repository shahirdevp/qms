# Generated by Django 2.2 on 2019-04-30 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mr', '0003_auto_20190430_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internal_external',
            name='doc_name',
            field=models.CharField(max_length=100),
        ),
    ]

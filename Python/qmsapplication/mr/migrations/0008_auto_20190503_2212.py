# Generated by Django 2.2 on 2019-05-03 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mr', '0007_auto_20190503_2203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internal_audit_report',
            old_name='areaofaudit',
            new_name='area_of_audit',
        ),
    ]
# Generated by Django 2.2 on 2019-05-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mr', '0005_auto_20190430_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internal_external',
            name='doc_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='internal_external',
            name='rev_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
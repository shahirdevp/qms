# Generated by Django 2.2 on 2019-04-30 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mr', '0002_doc_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internal_external',
            name='doc_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mr.doc_type'),
        ),
    ]

# Generated by Django 2.2 on 2019-04-26 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marketing', '0008_auto_20190417_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtk_enquiry_register',
            name='contact',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mtk_enquiry_register',
            name='contryCode',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mtk_enquiry_register',
            name='creadedOn',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='mtk_enquiry_register',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='mtk_enquiry_register',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mtk_enquiry_register',
            name='drawingNumber',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='mtk_enquiry_register',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mtk_enquiry_register',
            name='partNumber',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='mtk_enquiry_register',
            name='poNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mtk_enquiry_register',
            name='prodeliverDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mtk_enquiry_register',
            name='qty',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mtk_enquiry_register',
            name='quotationRef',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='mtk_enquiry_register',
            name='status',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'No')], max_length=1, null=True),
        ),
    ]

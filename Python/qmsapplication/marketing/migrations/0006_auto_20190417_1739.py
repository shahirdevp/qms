# Generated by Django 2.2 on 2019-04-17 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0005_auto_20190417_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mtk_enquiry_register',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
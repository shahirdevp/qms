# Generated by Django 2.2 on 2019-04-17 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0003_auto_20190417_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mtk_enquiry_register',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
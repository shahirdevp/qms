# Generated by Django 2.2 on 2019-04-26 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='internal_audit_plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_of_audit', models.CharField(max_length=100)),
                ('auditee', models.CharField(blank=True, max_length=100, null=True)),
                ('auditor', models.CharField(blank=True, max_length=100, null=True)),
                ('as_clauses', models.CharField(blank=True, max_length=150, null=True)),
                ('year', models.CharField(blank=True, max_length=10, null=True)),
                ('month', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('p', 'Plan'), ('c', 'Completed')], max_length=1)),
                ('creadedOn', models.DateField(auto_now=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='non_conf_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ncr_no', models.CharField(blank=True, max_length=100, null=True)),
                ('nc_statement', models.TextField(blank=True)),
                ('objective_evidence', models.CharField(blank=True, max_length=250, null=True)),
                ('root_cause', models.CharField(blank=True, max_length=250, null=True)),
                ('containment_action', models.TextField(blank=True)),
                ('correction', models.CharField(blank=True, max_length=250, null=True)),
                ('correction_action', models.CharField(blank=True, max_length=250, null=True)),
                ('creadedOn', models.DateField(auto_now=True, null=True)),
                ('area_of_audit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr.internal_audit_plan')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='internal_external',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_number', models.CharField(max_length=100)),
                ('doc_name', models.CharField(max_length=100)),
                ('doc_type', models.CharField(max_length=100)),
                ('rev_no', models.IntegerField()),
                ('date', models.DateField(auto_now=True, null=True)),
                ('doc_status', models.CharField(choices=[('Active', 'Active'), ('Obsolete', 'Obsolete')], max_length=10)),
                ('creadedOn', models.DateField(auto_now=True, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='internal_audit_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audit_check_point', models.TextField(blank=True)),
                ('observations', models.TextField(blank=True)),
                ('creadedOn', models.DateField(auto_now=True, null=True)),
                ('area_of_audit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mr.internal_audit_plan')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
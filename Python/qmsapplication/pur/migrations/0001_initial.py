# Generated by Django 2.2 on 2019-06-11 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_no', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('doc_ref', models.CharField(blank=True, max_length=255)),
                ('detail', models.TextField(blank=True)),
                ('recipt', models.CharField(blank=True, max_length=255)),
                ('issue', models.TextField(blank=True)),
                ('balance', models.IntegerField(blank=True)),
                ('date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(max_length=75)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('street', models.CharField(blank=True, max_length=100)),
                ('pin', models.IntegerField(blank=True)),
                ('phone', models.IntegerField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=75)),
                ('website', models.URLField(blank=True, max_length=100)),
                ('createdOn', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='pur_supplier_purchase_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=150)),
                ('unit', models.CharField(blank=True, max_length=75)),
                ('supplier_ref_no', models.CharField(blank=True, max_length=75)),
                ('qty', models.CharField(blank=True, max_length=75)),
                ('po_no', models.CharField(blank=True, max_length=150)),
                ('po_date', models.DateField(blank=True)),
                ('requested_date', models.DateField(blank=True)),
                ('supplier', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pur.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='pur_goods_receipt_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grrno', models.CharField(blank=True, max_length=255, null=True)),
                ('dc_ref', models.CharField(blank=True, max_length=255, null=True)),
                ('po_ref', models.CharField(blank=True, max_length=255, null=True)),
                ('part', models.CharField(blank=True, max_length=255, null=True)),
                ('inward_qty', models.CharField(blank=True, max_length=255, null=True)),
                ('sup_test_report', models.TextField(blank=True, null=True)),
                ('heat_lot_no', models.CharField(blank=True, max_length=255, null=True)),
                ('lenght', models.IntegerField(blank=True, null=True)),
                ('Hieght', models.IntegerField(blank=True, null=True)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('diameter', models.CharField(blank=True, max_length=255, null=True)),
                ('accepted_qty', models.IntegerField(blank=True, null=True)),
                ('rej_qty', models.IntegerField(blank=True, null=True)),
                ('return_dc', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(auto_now=True, null=True)),
                ('supplier', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pur.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='pur_approved_supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_entered', models.DateField(auto_now=True)),
                ('scope', models.CharField(blank=True, max_length=150)),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Under Evaluation', 'Under Evaluation'), ('Restricted', 'Restricted'), ('Disapproved', 'Disapproved')], default=1, max_length=50)),
                ('next_approved_date', models.DateField(blank=True)),
                ('supplier', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='pur.supplier')),
            ],
        ),
    ]

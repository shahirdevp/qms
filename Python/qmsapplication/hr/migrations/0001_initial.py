# Generated by Django 2.2 on 2019-06-11 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='annual_trainnig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026')], max_length=1)),
                ('topic', models.CharField(max_length=10)),
                ('department_or_person', models.CharField(max_length=50)),
                ('jan', models.CharField(blank=True, max_length=20)),
                ('feb', models.CharField(blank=True, max_length=20)),
                ('mar', models.CharField(blank=True, max_length=20)),
                ('apr', models.CharField(blank=True, max_length=20)),
                ('may', models.CharField(blank=True, max_length=20)),
                ('jun', models.CharField(blank=True, max_length=20)),
                ('jul', models.CharField(blank=True, max_length=20)),
                ('aug', models.CharField(blank=True, max_length=20)),
                ('sep', models.CharField(blank=True, max_length=20)),
                ('Oct', models.CharField(blank=True, max_length=20)),
                ('nov', models.CharField(blank=True, max_length=20)),
                ('dec', models.CharField(blank=True, max_length=20)),
                ('remarks', models.CharField(max_length=250)),
                ('legend', models.CharField(blank=True, max_length=250)),
                ('prepard_By', models.CharField(max_length=250)),
                ('approved_By', models.CharField(blank=True, max_length=250)),
                ('created_On', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='competency_Matrix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=75)),
                ('education_Background', models.CharField(max_length=150)),
                ('experience', models.IntegerField()),
                ('competency_Requirement', models.CharField(max_length=250)),
                ('created_On', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='employe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_Employee', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=500)),
                ('employee_ID', models.CharField(max_length=25)),
                ('fathers_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('qualification', models.CharField(max_length=75)),
                ('date_of_join', models.DateField()),
                ('languages_known', models.CharField(max_length=250)),
                ('position', models.CharField(max_length=50)),
                ('created_On', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employe_id', models.CharField(max_length=25)),
                ('organization', models.CharField(max_length=75)),
                ('no_of_years_served', models.IntegerField()),
                ('work_experience', models.IntegerField()),
                ('created_On', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='hr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hr_required_deg', models.CharField(max_length=100)),
                ('requestedby', models.CharField(max_length=50)),
                ('reson_new_hire', models.CharField(max_length=500)),
                ('remarks', models.CharField(max_length=250)),
                ('preparedBy', models.CharField(max_length=50)),
                ('arrovedBy', models.CharField(max_length=50)),
                ('createdOn', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='skillmatrix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depaertment', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=100)),
                ('empId', models.CharField(blank=True, max_length=50)),
                ('empName', models.CharField(blank=True, max_length=75)),
                ('drawing_studying_skills', models.CharField(blank=True, max_length=75)),
                ('usage_of_general_gauges', models.CharField(blank=True, max_length=75)),
                ('usage_of_general_instruments', models.CharField(blank=True, max_length=75)),
                ('usage_of_product_specific_gauges', models.CharField(blank=True, max_length=75)),
                ('quality_documentation', models.CharField(blank=True, max_length=75)),
                ('cmm_operating', models.CharField(blank=True, max_length=75)),
                ('pp_operating', models.CharField(blank=True, max_length=75)),
                ('operating_surface_roughness_tester', models.CharField(blank=True, max_length=75)),
                ('basic_machining_knowledge', models.CharField(blank=True, max_length=75)),
                ('microscope_handeling', models.CharField(blank=True, max_length=75)),
                ('internal_verification_skills', models.CharField(blank=True, max_length=75)),
                ('inspection_skill', models.CharField(blank=True, max_length=75)),
                ('visual_inspection_skill', models.CharField(blank=True, max_length=75)),
                ('d_height_gauge_operating', models.CharField(blank=True, max_length=75)),
                ('scoring_crieteria', models.CharField(blank=True, max_length=75)),
                ('prepredBy', models.CharField(blank=True, max_length=75)),
                ('approvedBy', models.CharField(blank=True, max_length=75)),
                ('created_On', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='training_evalution_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trg_no', models.IntegerField()),
                ('training_topic', models.CharField(max_length=50)),
                ('date_of_trainig', models.DateField(auto_now_add=True)),
                ('date_of_join', models.DateField(auto_now_add=True)),
                ('faculty', models.CharField(max_length=50)),
                ('venue', models.CharField(max_length=50)),
                ('name_of_participant', models.CharField(max_length=50)),
                ('score', models.CharField(choices=[('3', 'understood , Implemented , can train  others '), ('2', 'Undestood implemented '), ('1', 'undrestood'), ('0', 'Not Understood Require retraining .')], max_length=1)),
                ('evaluation_criteria', models.TextField(max_length=300)),
                ('Effectiveness_of_Training', models.TextField(max_length=300)),
                ('evaluated_By', models.CharField(max_length=50)),
                ('created_On', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='training_Request_Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_Required', models.CharField(max_length=150)),
                ('training_to', models.CharField(max_length=50)),
                ('training_Suggested_by', models.CharField(max_length=150)),
                ('reason_for_Training', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('remarks', models.CharField(max_length=250)),
                ('prepared_By', models.CharField(max_length=50)),
                ('approved_By', models.CharField(max_length=50)),
                ('created_On', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

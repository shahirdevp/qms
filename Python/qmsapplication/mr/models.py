from django.db import models
from django.contrib.auth.models import User


class doc_type(models.Model):
    doc_type_name =  models.CharField(max_length = 100, unique=True)
    creadedOn = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
            return self.doc_type_name


class internal_external(models.Model):
    DOC_STATUS = (('Active','Active'),('Obsolete','Obsolete'))
    doc_number = models.CharField(max_length = 100)
    doc_name = models.CharField(max_length = 100)
    doc_type = models.CharField(max_length = 100)
    rev_no  = models.CharField(max_length = 100, blank=True, null=True)
    date    = models.DateField(auto_now=True, blank=True, null=True)
    doc_status = models.CharField(max_length=100,blank=True, null=True)
    owner = models.ForeignKey(User,  blank=True, null=True, on_delete=models.CASCADE)
    creadedOn = models.DateField(auto_now=True, blank=True, null=True)


    def __str__(self):
        return self.doc_name

class internal_audit_plan(models.Model):
    PLAN_STATUS = (('p','Plan'),('c','Completed'))
    area_of_audit = models.CharField(max_length = 100)
    auditee = models.CharField(max_length = 100, blank=True, null=True)
    auditor = models.CharField(max_length=100, blank=True, null=True)
    as_clauses = models.CharField(blank=True, null=True, max_length=150)
    year = models.CharField(blank=True, null=True, max_length=10)
    month = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=1, choices=PLAN_STATUS)
    owner = models.ForeignKey(User,  blank=True, null=True, on_delete=models.CASCADE)
    creadedOn = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.area_of_audit

class internal_audit_report(models.Model):
    area_of_audit =  models.ForeignKey(internal_audit_plan,  on_delete=models.CASCADE)
    audit_check_point = models.TextField(blank=True)
    observations = models.TextField(blank=True)
    owner = models.ForeignKey(User,  blank=True, null=True, on_delete=models.CASCADE)
    creadedOn = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.area_of_audit

class non_conf_report(models.Model):
    area_of_audit =  models.ForeignKey(internal_audit_plan,  on_delete=models.CASCADE)
    ncr_no = models.CharField(max_length=100, blank=True, null=True)
    nc_statement = models.TextField(blank=True)
    objective_evidence = models.CharField(max_length=250, blank=True, null=True)
    root_cause = models.CharField(max_length=250, blank=True, null=True)
    containment_action = models.TextField(blank=True)
    correction = models.CharField(max_length=250, blank=True, null=True)
    correction_action = models.CharField(max_length=250, blank=True, null=True)
    owner = models.ForeignKey(User,  blank=True, null=True, on_delete=models.CASCADE)
    creadedOn = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.area_of_audit

  
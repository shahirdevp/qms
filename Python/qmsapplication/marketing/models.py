from django.db import models
from django.contrib.auth.models import User


class mtk_enquiry_register(models.Model):
    STATUS_LIST= (('1', 'Yes'),('0', 'No'))
    customer = models.CharField(max_length = 100)
    date = models.DateField(auto_now=True, blank=True, null=True)
    prodeliverDate = models.DateField(auto_now=False, blank=True, null=True)
    contact  = models.IntegerField(blank=True,null=True)
    contryCode = models.SmallIntegerField( blank=True ,null=True)
    line_number  =   models.CharField(max_length = 60, blank=True)
    partNumber  =   models.CharField(max_length = 60, blank=True)
    description = models.TextField(blank=True)
    drawingNumber = models.CharField(max_length = 60, blank=True)
    qty = models.IntegerField(blank=True, null=True)
    quotationRef = models.CharField(max_length=150, blank=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    poNumber = models.CharField(max_length=100, blank=True ,null=True)
    creadedOn = models.DateField(auto_now=True, blank=True, null=True)
    owner = models.ForeignKey(User,  blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer


class  quality_feasibility(models.Model):
    STATUS_LIST= (('1', 'Yes'),('0', 'No'))
    cusomer = models.ForeignKey(mtk_enquiry_register,  on_delete=models.CASCADE)
    owner = models.ForeignKey(User,  on_delete=models.CASCADE, blank=True)
    inst	= models.CharField(max_length=1, choices=STATUS_LIST)
    gauge	= models.CharField(max_length=1, choices=STATUS_LIST)
    can_aql_be_achived	= models.CharField(max_length=1, choices=STATUS_LIST)
    is_fai_required	= models.CharField(max_length=1, choices=STATUS_LIST)
    key_chare	= models.CharField(max_length=1, choices=STATUS_LIST)
    ispection_as_per 	= models.CharField(max_length=1, choices=STATUS_LIST)
    creadedOn = models.DateField(auto_now=True,blank=True, null=True)

    def __str__(self):
        return self.cusomer

class  tech_feasibility(models.Model):
    STATUS_LIST= (('1', 'Yes'),('0', 'No'))
    cusomer = models.ForeignKey(mtk_enquiry_register,  on_delete=models.CASCADE)
    owner = models.ForeignKey(User,  on_delete=models.CASCADE, blank=True)
    creadedOn = models.DateField(auto_now=True, blank=True, null=True)
    r_mtrl	= models.CharField(max_length=1, choices=STATUS_LIST)
    m_c = models.CharField(max_length=1, choices=STATUS_LIST)
    tools = models.CharField(max_length=1, choices=STATUS_LIST)
    Spl_process	= models.CharField(max_length=1, choices=STATUS_LIST)
    any_cad_req	= models.CharField(max_length=1, choices=STATUS_LIST)
    out_source	= models.CharField(max_length=1, choices=STATUS_LIST)
    

    def __str__(self):
        return self.cusomer

class marketing_feasibility(models.Model):
    STATUS_LIST= (('1', 'Yes'),('0', 'No'))
    cusomer = models.ForeignKey(mtk_enquiry_register,  on_delete=models.CASCADE)
    owner = models.ForeignKey(User,  on_delete=models.CASCADE, blank=True)
    is_statuatory_regulatory	= models.CharField(max_length=1, choices=STATUS_LIST)
    is_delivery_feasibility	= models.CharField(max_length=1, choices=STATUS_LIST)
    is_nre_applicable	= models.CharField(max_length=1, choices=STATUS_LIST)
    creadedOn = models.DateField(auto_now=True,blank=True, null=True)
     
    def __str__(self):
        return self.cusomer

class reviewer(models.Model):
    STATUS_LIST= (('1', 'Yes'),('0', 'No'))
    cusomer = models.ForeignKey(mtk_enquiry_register,  on_delete=models.CASCADE)
    owner = models.ForeignKey(User,  on_delete=models.CASCADE, blank=True)
    mkt	= models.CharField(max_length=1, choices=STATUS_LIST)
    qcd	= models.CharField(max_length=1, choices=STATUS_LIST)
    pur	= models.CharField(max_length=1, choices=STATUS_LIST)
    prd	= models.CharField(max_length=1, choices=STATUS_LIST)
    creadedOn = models.DateField(auto_now=True,blank=True, null=True)
     
    def __str__(self):
        return self.cusomer


class configuration_management_report(models.Model):
    cusomer = models.ForeignKey(mtk_enquiry_register,  on_delete=models.CASCADE)
    owner = models.ForeignKey(User,  on_delete=models.CASCADE, blank=True)
    creadedOn = models.DateField(auto_now=True,blank=True, null=True)
    customer_order = models.CharField(max_length = 300, blank=True)
    route_card_no = models.CharField(max_length = 100, blank=True)
    internal_job_order = models.CharField(max_length = 300, blank=True)
    rev_no = models.CharField(max_length = 100, blank=True)
    invoice_no = models.CharField(max_length = 100, blank=True)


    def __str__(self):
        return self.cusomer
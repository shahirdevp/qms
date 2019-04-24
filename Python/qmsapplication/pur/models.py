from django.db import models


class supplier(models.Model):
    supplier = models.CharField(max_length=75)
    country  = models.CharField(max_length=100, blank=True)
    state    = models.CharField(max_length=100, blank=True)
    city     = models.CharField(max_length=100, blank=True)
    street   = models.CharField(max_length=100, blank=True)
    pin      = models.IntegerField(blank=True)
    phone    = models.IntegerField(blank=True)
    email    = models.EmailField(blank=True, max_length=75)
    website  = models.URLField(blank=True, max_length=100)
    createdOn= models.DateField(auto_now=True)

    def __str__(self):
        return self.supplier



class pur_approved_supplier(models.Model):
    STATUS_CHOICE = (
        ('1', 'Approved'),
        ('2', 'Under Evaluation'),
        ('3', 'Restricted'),
        ('4', 'Disapproved'),
    )
    date_entered       = models.DateField(auto_now=True)
    supplier 	       = models.ForeignKey(supplier,blank=True, on_delete=models.CASCADE)
    scope   	       = models.CharField(max_length=150, blank=True)
    status  	       = models.CharField(max_length=1, choices=STATUS_CHOICE, default=1)
    next_approved_date = models.DateField(auto_now=False, blank=True)

    def __str__(self):
        return self.supplier


class pur_supplier_purchase_order(models.Model):
    supplier 	    = models.ForeignKey(supplier,blank=True, on_delete=models.CASCADE)
    product         = models.CharField(max_length=150, blank=True)    
    unit            = models.CharField(blank=True, max_length=75)
    supplier_ref_no =  models.CharField(blank=True, max_length=75)    
    qty             = models.CharField(blank=True, max_length=75)
    po_no           = models.CharField(max_length=150, blank=True)    
    po_date         = models.DateField(auto_now=False, blank=True)
    requested_date  = models.DateField(auto_now=False, blank=True)


    def __str__(self):
        return self.supplier


class pur_goods_receipt_register(models.Model):
    grrno           = models.CharField(blank=True, max_length=255)
    date            = models.DateField(auto_now=False, blank=True)
    supplier        = models.ForeignKey(supplier,blank=True, on_delete=models.CASCADE)
    dc_ref          = models.CharField(blank=True, max_length=255)
    po_ref          = models.CharField(blank=True, max_length=255)
    part            = models.CharField(blank=True, max_length=255)
    inward_qty      = models.CharField(blank=True, max_length=255)
    sup_test_report = models.TextField(blank=True)
    heat_lot_no     =  models.CharField(blank=True, max_length=255)
    lenght          =  models.IntegerField(blank=True)
    Hieght          =  models.IntegerField(blank=True)
    width           =  models.IntegerField(blank=True)
    diameter        =  models.CharField(blank=True, max_length=255)
    accepted_qty    =  models.IntegerField(blank=True)
    rej_qty         =  models.IntegerField(blank=True)
    return_dc       =  models.CharField(blank=True, max_length=255)
    date            =  models.DateField(auto_now=True)

    def __str__(self):
            return self.supplier


class stock_register(models.Model):
    part_no     = models.CharField(blank=True, max_length=255)
    description = models.TextField(blank=True)
    doc_ref     = models.CharField(blank=True, max_length=255)
    detail      = models.TextField(blank=True)
    recipt      = models.CharField(blank=True, max_length=255)
    issue       = models.TextField(blank=True)
    balance     = models.IntegerField(blank=True) 
    date        = models.DateField(auto_now=False, blank=True)

    def __str__(self):
            return self.part_no
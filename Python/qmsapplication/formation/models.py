from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

class Cmp_formation(models.Model):

    CmpName  = models.CharField(max_length=100)
    scope  = models.TextField(blank=True, null=True)
    policy = models.FileField(upload_to='doc/', blank=True, null=True)
    app_domain = models.URLField(max_length=200, blank=True, null=True)
    SupUser =  models.ForeignKey(User,  on_delete=models.CASCADE, blank=True, null=True)
    Cunique = get_random_string(length=64)
    created_on = models.DateField(auto_now_add=True)
    modify_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.CmpName

class Process(models.Model):
    CmpName = models.ForeignKey(Cmp_formation, on_delete=models.CASCADE)
    PrcName = models.CharField(max_length=100)

    def __str__(self):
        return self.CmpName

class OrgChart(models.Model):
    CmpName = models.ForeignKey(Cmp_formation,  on_delete=models.CASCADE)
    desgnations = models.CharField(max_length=100)
    created_at =  models.ForeignKey(User,  on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    modify_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.CmpName


class RolesAuthorised(models.Model):
    CmpName = models.ForeignKey(Cmp_formation,  on_delete=models.CASCADE)
    responsiblity  = models.TextField(blank=True, null=True)
    Authorised = models.ForeignKey(OrgChart,  on_delete=models.CASCADE)
    created_at =  models.ForeignKey(User,  on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    modify_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.CmpName






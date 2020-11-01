from django.db import models
# Create your models here.

class InData(models.Model):
    #category_options= [('sta','Stationary'),('elec','Electronics'),('acc','Accessories')]
    #category = models.CharField(max_length=1,choices=category_options)
    category = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    priceperpiece = models.CharField(max_length=50)
    totalprice = models.CharField(max_length=50, blank=True)
    qty = models.CharField(max_length=50)
    dname = models.CharField(max_length=50)
    dloc = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class OutData(models.Model):
    #category_options= [('sta','Stationary'),('elec','Electronics'),('acc','Accessories')]
    #category = models.CharField(max_length=1,choices=category_options)
    category = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50)
    priceperpiece = models.CharField(max_length=50)
    totalprice = models.CharField(max_length=50, blank=True)
    qty = models.CharField(max_length=50, blank=True)
    cname = models.CharField(max_length=50)
    cloc = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
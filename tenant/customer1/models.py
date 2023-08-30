from django.db import models

# Create your models here.
class Tenant(models.Model):
    name=models.CharField(max_length=255)
    subdomain=models.CharField(max_length=255)

class TenantAwareModels(models.Model):
    tenant=models.ForeignKey(Tenant,on_delete=models.CASCADE)    


class Organisation(TenantAwareModels):
    name=models.CharField(max_length=255)    
    
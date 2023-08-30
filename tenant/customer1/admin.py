from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Tenant)
admin.site.register(Organisation)
admin.site.register(TenantAwareModels)
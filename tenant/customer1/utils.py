from .models import *

def retrieve_hostname(request):
    return request.get_host().split(':')[0].lower()



def geting_tenant(request):
    hostname=retrieve_hostname(request)
    subdomain=hostname.split('.')[0]
    print(hostname,subdomain)

    return Tenant.objects.filter(subdomain=subdomain).first()
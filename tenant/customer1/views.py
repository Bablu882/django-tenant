from django.shortcuts import render

# Create your views here.
from .utils import geting_tenant
from .models import Organisation

def my_team(request):
    tanent=geting_tenant(request)
    team=Organisation.objects.filter(tenant=tanent)
    return render(request,'customer1/team.html',{'tenant':tanent,'organisation':team})
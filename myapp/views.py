from django.shortcuts import render
from .models import Country,State,District
# Create your views here.
def index(request):
    countryid = request.GET.get('country',None)
    stateid = request.GET.get('state',None)
    state = None
    district = None

    if countryid:
        getcountry = Country.objects.get(id=countryid)
        state = State.objects.filter(country=getcountry)

    if stateid:
        getstate = State.objects.get(id=stateid)
        district = District.objects.filter(State=getstate)

    country =Country.objects.all()
    return render(request,'index.html',locals())
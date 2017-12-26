from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request,'home.html',context)

def aboutus(request):
    context = {}
    return render(request,'about-us.html',context)

def contactus(request):
    context = {}
    return render(request,'contact-us.html',context)

def services(request):
    context = {}
    return render(request,'services.html',context)

def portfolio(request):
    context = {}
    return render(request,'portfolio.html',context)
    
def clients(request):
    context={}
    return render(request,'client.html',context)

# Services views
def digitization(request):
    context = {}
    return render(request,'digitization.html',context)

def Architechture(request):
    context={}
    return render(request,'architechture.html',context)

def land_surveys(request):
    context = {}
    return render(request,'land_surveys.html',context)

def topographical_surveys(request):
    context = {}
    return render(request,'topographical_surveys.html',context)

def physical_surveys(request):
    context = {}
    return render(request,'physical_surveys.html',context)

def alignment_surveys(request):
    context = {}
    return render(request,'alignment_surveys.html',context)

def building_surveys(request):
    context = {}
    return render(request,'building_surveys.html',context)

def quantity_surveys(request):
    context = {}
    return render(request,'quantity_surveys.html',context)

def demarcation_surveys(request):
    context = {}
    return render(request,'demarcation_surveys.html',context)

def road_surveys(request):
    context = {}
    return render(request,'road_surveys.html',context)

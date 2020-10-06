from django.shortcuts import render
from .models import A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17,A18
# Create your views here.
def a1(request):
    obj1 = A1.objects.all()
    return render(request,'1.html',{'obj1':obj1})

def home(request):
    return render(request,'index.html')
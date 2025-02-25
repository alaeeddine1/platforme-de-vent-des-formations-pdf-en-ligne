from django.shortcuts import render
from .models import formation
# Create your views here.
def unformation(request):
     return render(request,'formation/formation.html')

def formations(request):
     return render(request,'formation/formations.html',{'xdf':formation.objects.all()})
    
from django.shortcuts import render
from .models import formation
# Create your views here.
def unformation(request):
     return render(request,'formation/formation.html')

def formations(request):
      if request.method == 'GET':
        print("il ya une choix ")
        ch=request.GET.get('choix')
        if ch != None:
           return render(request,'formation/formations.html',{'xdf':formation.objects.filter(nom=ch)})
        else :
          return render(request,'formation/formations.html',{'xdf':formation.objects.all()}) 
      
    
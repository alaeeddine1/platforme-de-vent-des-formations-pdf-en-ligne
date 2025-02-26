from django.shortcuts import render
from django.http import HttpResponse
from .models import compte_cree
from .models import reservation
from formation.models import formation
from decimal import Decimal
from decimal import  ROUND_HALF_UP
from django.shortcuts import get_object_or_404, render



# Create your views here.
def home(request):
    return render(request,'pages/home.html')


def client(request):
    xuser = request.session.get('users')  
    data = {
        'name': xuser,
        'form': formation.objects.all(),
    }
    
    if request.method == 'GET':
        print("Il y a une choix")
        ch = request.GET.get('choix')
        
        if ch is not None:
            dataa = {
             'name': xuser,
             'form': formation.objects.filter(nom=ch),
             }
            return render(request, 'pages/client.html', dataa)
        else:
            # If no choice is made, render the client page with the data
            return render(request, 'pages/client.html', data)
     


#CREATION DU COMPTE
def Compte(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')
        nom = request.POST.get('name')
        prenom = request.POST.get('fname')
        email = request.POST.get('email')
        ville = request.POST.get('city')
        
        
        if username and password:
            
            new_login = compte_cree(username=username, password=password,nom=nom,prenom=prenom,email=email,ville=ville)
            new_login.save()
            
          
            dataa={
             'name':username,
             'form':formation.objects.all(),
             }
                          
                    
                 
            request.session['users'] = username
            return render(request, 'pages/client.html',dataa)
        else:
            
            
            return render(request, 'pages/client.html')
    else:
        return render(request, 'pages/compte.html')





# login
def login(request):
    
    if request.method == 'GET':
        xuser = request.GET.get('userl')
        xpass = request.GET.get('passwordl')
        sit=1
        x=compte_cree.objects.filter(username=xuser).first()
       
        if x is  None : 
            
            print("utilisateut introuvable")
            message="utilisateut introuvable"
            if not xuser and not xpass:
                 message="."
            return render(request,'pages/login.html',{'msg':message})
        elif  xpass !=x.password: 
             print("mot de pass incorrect")
             message="mot de pass incorrect"
             return render(request,'pages/login.html',{'msg':message})
        else:
            data={
                'name':x.username,
                'form':formation.objects.all(),
                }
            
            request.session['users'] = x.username
            message="Conexion avec succes"
            return render(request,'pages/client.html',data)





#panier
def panier(request):
    xuser  = request.session.get('users')  
    client=compte_cree.objects.filter(username=xuser).first()
    
    if request.method == 'POST':
        fonc=request.POST.get('fon')
        print(fonc)
        #nnnnnnnnnn
        x=client.formations_panier.all()
        coun=0
        for i in x:
          
          coun += 1
        #nnnnnnnn
        if coun  < 3:
           if fonc =="a":
              formaclique = request.POST.get('nom')
              formajoute=formation.objects.filter(nom=formaclique).first()
              client.formations_panier.add(formajoute)
              client.save()




        if fonc == "s":
            formaclique = request.POST.get('nom')
            formajoute=formation.objects.filter(nom=formaclique).first()
            client.formations_panier.remove(formajoute)
            client.save()


    
        
            

           
          



    data={
        'formpanier':client.formations_panier.all()
         }
    
    return render(request, 'pages/panier.html',data)
  
    

     
def reservations(request):
     xuser  = request.session.get('users')  
     client=compte_cree.objects.filter(username=xuser).first()
     datar={
                
            'res':reservation.objects.filter(username_client=xuser)
            
         }

     if request.method == 'POST': 
         fonct=request.POST.get('fon')
         print('helloo') 
         print(fonct)
         if fonct == "r":
           counter=0
           prix=0
           x=client.formations_panier.all()
           for i in x:
             
             prix += i.prix
             counter += 1
            

           print(prix)
           print(counter)
           nvr= reservation(username_client=client.username ,nom_client=client.nom, prenom_client=client.prenom , email_client=client.email ,nombre_formations=Decimal(counter), prix=Decimal(prix) )
           nvr.save()



           for i in x:
            nvr.formations_reservees.add(i)
            nvr.save()


     return render(request,'pages/reservation.html',datar)




def telecharger(request):
     
     if request.method == 'POST':
        idr=request.POST.get('idres')
     data={
        'res':reservation.objects.filter(id = idr).first()
     }

     return render(request, 'pages/telecharger.html',data)



def telecharger_pdf(request, formation_id):
    # Utilisez get_object_or_404 avec le modèle 'formation' pour récupérer l'objet de formation par ID
    formation_obj = get_object_or_404(formation, id=formation_id)

    if formation_obj.pdf:
        pdf_path = formation_obj.pdf.path
        pdf_filename = formation_obj.pdf.name.split('/')[-1]

        with open(pdf_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{pdf_filename}"'
            return response
    else:
        return HttpResponse("Aucun fichier PDF trouvé.")



def paiment (request):

    return render(request, 'pages/paiment.html')   
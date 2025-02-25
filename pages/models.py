from django.db import models
from formation.models import formation
# Create your models here.
class compte_cree(models.Model):
     
      nom=models.CharField(max_length=50,null=True,blank=True)
      prenom=models.CharField(max_length=50,null=True,blank=True)
      ville=models.CharField(max_length=50,null=True,blank=True)
      username = models.CharField(max_length=50)
      password = models.CharField(max_length=50)
      email=models.CharField(max_length=50,null=True,blank=True)
      formations_panier = models.ManyToManyField(formation, related_name='clients')
      def __str__(self):
            return self.username


class reservation(models.Model):
     
      nombre_formations=models.DecimalField(max_digits=10,decimal_places=2,default=2)
      nom_client=models.CharField(max_length=50,null=True,blank=True,default=2)
      username_client=models.CharField(max_length=50,null=True,blank=True,default=2)
      prenom_client=models.CharField(max_length=50,null=True,blank=True,default=2)
      email_client=models.CharField(max_length=50,null=True,blank=True,default=2)
      prix=models.DecimalField(max_digits=10,decimal_places=2)
      nom_client=models.CharField(max_length=50,null=True,blank=True)
      formations_reservees = models.ManyToManyField(formation, related_name='reservatons')
      
   
      def __str__(self):
            return self.nom_client
          



from django.db import models


# Create your models here.
class formation(models.Model):
      x=[
      ('informatique','informatique'),
      ('industrielle','industrielle'),
      ('automatisme','automatisme'),
      ]
      nom = models.CharField(max_length=100)
      prix=models.DecimalField(max_digits=4,decimal_places=2)
      date=models.DateField(null=True)
      heure=models.TimeField(null=True)
      image=models.ImageField(upload_to= 'photo/%y/%m/%j')
      description=models.TextField(null=True)
      active=models.BooleanField(null=True)
      categorie=models.CharField(max_length=50,choices=x,null=True,blank=True)
      pdf = models.FileField(upload_to='pdfs/%Y/%m/%d', null=True, blank=True)
      
      def __str__(self):
            return self.nom
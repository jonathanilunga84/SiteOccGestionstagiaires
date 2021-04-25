from django.db import models
 
# Create your models here.
class Direction(models.Model):
    nom_direction = models.CharField(max_length=100)
    def __str__(self):
        return self.nom_direction

class Encadreur(models.Model):
    nom_encad = models.CharField(max_length=20)
    postnom_encad = models.CharField(max_length=20)
    prenom_encad = models.CharField(max_length=20)
    sexe_encad = models.CharField(max_length=10)
    def __str__(self):
        return self.nom_encad +' '+ self.prenom_encad #, self.prenom_encad, self.sexe_encad

class Stagiaire(models.Model):
    nom_stagiaire = models.CharField(max_length=20)
    postnom_stagiaire = models.CharField(max_length=20)
    prenom_stagiaire = models.CharField(max_length=20)
    sexe_stagiaire = models.CharField(max_length=10)
    email_stagiaire = models.EmailField(max_length=200)
    adresse_stagiaire = models.CharField(max_length=200)
    telephone_stagiaire = models.CharField(max_length=15)
    type_stage = models.CharField(max_length=20)
    promotion_stagiaire = models.CharField(max_length=20)
    direction = models.ForeignKey(Direction, related_name='directions', on_delete=models.CASCADE)
    encadreur = models.ForeignKey(Encadreur, related_name='encadreurs', on_delete=models.CASCADE )
    #date_debut = models.DateTimeField(null=True)
    #date_debut = models.DateTimeField(auto_now_add=True)
    #date_fin = models.DateTimeField(null=True) #'date published' 2021-03-22 20:58:58.608605

    def __str__(self):
        return self.nom_stagiaire +" - "+self.postnom_stagiaire #, #prenom_stagiaire, sexe_stagiaire 

class ContactMessage(models.Model):
    nom = models.CharField(max_length=25)
    Email = models.EmailField(max_length=200)
    msg = models.CharField(max_length=200)
    #date_post = models.DateTimeField(auto_now_add=True)
    def __str__(self):
      return self.nom
    #  23/Mar/2021 23:01:55


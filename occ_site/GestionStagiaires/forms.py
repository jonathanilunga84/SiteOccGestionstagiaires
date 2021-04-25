from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactMessage, Stagiaire, Encadreur, Direction

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('Email','nom','msg')  
        labels = {
            'Email':'Entrez votre mail',
            'nom':'Entrez nom complet',
            'msg':'Ecrire votre message'
        }
        #widgets = {
        #    'msg': textarea()
        #}
    #def __init__(self, *args, **kwargs):
        #super(ContactMessageForm,self).__init__(*args, **kwargs)
        #self.fields['nom'].empty_label = "votre nom"

class EncadreurForm(forms.ModelForm):
    class Meta:
        model = Encadreur
        fields = ('nom_encad','postnom_encad','prenom_encad','sexe_encad')
        labels = {
            'nom_encad': 'Nom',
            'postnom_encad':'Postnom',
            'prenom_encad': 'Prenom',
            'sexe_encad':'Sexe'
        }
        

    #def __init__(self, *args, **kwargs):
    #    super(EncadreurForm,self).__init__(*args,  **kwargs)
    #    self.fields['nom_encad'].

class StagiaireForm(forms.ModelForm):
    class Meta: 
        model = Stagiaire
        fields = ('nom_stagiaire','postnom_stagiaire','prenom_stagiaire','sexe_stagiaire','email_stagiaire','adresse_stagiaire','telephone_stagiaire','type_stage','promotion_stagiaire','direction','encadreur') #'__all__'
        labels = {
            'nom_stagiaire': 'Nom',
            'postnom_stagiaire':'Postnom',
            'prenom_stagiaire':'Prenom',
            'sexe_stagiaire':'Sexe',
            'email_stagiaire':'Email',
            'adresse_stagiaire':'Adresse',
            'telephone_stagiaire':'Telephone',
            'type_stage':'Type de Stage',
            'promotion_stagiaire':'Promotion Stagiaire',
            #'direction':'Direction De Stagiaire',
            #'encadreur':'Encadreur De Stage'
        } 
        widgets = {
            'direction':forms.Select(attrs={'class':'listDirection'})
        }

    def __init__ (self, *args, **kwargs):
        super(StagiaireForm,self).__init__(*args,**kwargs)
        self.fields['direction'].empty_label = "Select Direction"
        self.fields['encadreur'].empty_label = "Select Encadreur"

class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = ('nom_direction',) #'__all__'
        labels = {
            'nom_direction': 'NOM DIRECTION'
        }
        widgets = {
            'nom_direction':forms.TextInput(attrs={'class':'form-control', 'id':'NomDirection'})
        }
        
    def __init__(self, *args, **kwargs):
        super(DirectionForm,self).__init__(*args,**kwargs)
        self.fields['nom_direction'].empty_label = "Select"

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
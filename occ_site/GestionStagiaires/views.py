from django.shortcuts import render, redirect
from .forms import ContactMessageForm, StagiaireForm, EncadreurForm, DirectionForm, CreateUserForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import ContactMessage, Stagiaire, Encadreur, Direction
from django.contrib.auth.forms import UserCreationForm
#from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def contactMessage(request):
    mail = request.POST['mail']
    nom = request.POST['nom']
    msg = request.POST['msg']
    return HttpResponse("Hello form %s "% msg) 

def index(request, id=0):
    #return HttpResponse("Hello M.si-pro")  https://docs.djangoproject.com/fr/3.1/topics/forms/https://docs.djangoproject.com/fr/3.1/topics/forms/
    # j'importe le form de la class forms.py
    if request.method =="GET":
        if id == 0:
            form = aff_form()
        else:
            ctm = ContactMessage.objects.get(pk=id)
            form = ContactMessageForm(instance=ctm)
        return render(request, 'GestionStagiaires/index.html',{'form':form}) 
    else: 
        form = ContactMessageForm(request.POST)
        if form.is_valid(): 
            form.save() 
        return redirect('/GestionStagiaires/resultMessage')

def createStagiaire(request,id=0):  
    if request.method == "GET":
        if id==0:
            context = {
                'stagiaireForm' :StagiaireForm(),
                'form' : ContactMessageForm(),
                'directionForm':DirectionForm(),
                'EncadreurForm': EncadreurForm()
            }
            return render(request,'GestionStagiaires/Etudiant/createStagiaire.html', context)
        else:
            #recuperation d'un seul stagiaire
            stagiaire = Stagiaire.objects.get(pk=id)
            #stagiaireForm = StagiaireForm(instance=stagiaire)
            context = {
                'stagiaireForm' :StagiaireForm(instance=stagiaire),
                'form' : ContactMessageForm(),
                'directionForm':DirectionForm(),
                'EncadreurForm': EncadreurForm()
            }
        return render(request,'GestionStagiaires/Etudiant/createStagiaire.html', context)
    else:
        if id==0:
            stagiaireForm = StagiaireForm(request.POST)
            if stagiaireForm.is_valid():
                stagiaireForm.save()
                context = {
                    'Messages': 'Enregistrement Effectué avec succes'
                }
                return render(request, 'GestionStagiaires/Etudiant/stagiaireConfirmEnregistrement.html', context)
            else :
                context = {
                    'Messages': 'Echec Enregistrement'
                } 
                return render(request, 'GestionStagiaires/Etudiant/stagiaireConfirmEnregistrement.html', context)
        else:
            stagiaire = Stagiaire.objects.get(pk=id)
            stagiaireForm = StagiaireForm(request.POST,instance=stagiaire)
            if stagiaireForm.is_valid():
                stagiaireForm.save()
                context = {'Messages': 'Modification Stagiaire Effectué avec Success',}
                return render(request, 'GestionStagiaires/Etudiant/stagiaireConfirmEnregistrement.html', context) 
            else:
                context = {'Messages': 'Modification Stagiaire a Echoué',}
                return render(request, 'GestionStagiaires/Etudiant/stagiaireConfirmEnregistrement.html', context) 
   
def deleteStagiaire(request, pk):
    stagiaire = Stagiaire.objects.get(id=pk)
    context = {
        'Stagiaires_liste': Stagiaire.objects.all(),
        'form':ContactMessageForm(),
        'stagiaireForm' :stagiaire
    }
    if request.method == "POST":
        stagiaire.delete()
        return render(request, 'GestionStagiaires/Etudiant/listeStagiaires.html', context)
    return render(request, 'GestionStagiaires/Etudiant/deleteStagiaire.html', context)

def stagiaireConfirmEnregistrement(request):
    return render(request, 'GestionStagiaires/Etudiant/stagiaireConfirmEnregistrement.html')


def listeStagiaires(request):
    context = {
        'Stagiaires_liste': Stagiaire.objects.all(),
        'form':ContactMessageForm()
    }
    return render(request, 'GestionStagiaires/Etudiant/listeStagiaires.html', context)

def resultMessage(request):
    form = aff_form() 
    context = {
        'ContactMessage_list':ContactMessage.objects.all(),
        'form':form
    }
    return render(request, 'GestionStagiaires/resultMessage.html', context)

def annoce(request):
    return HttpResponse("Hello M.si-pro") 

def aff_form():
    return ContactMessageForm() 


def CreateEncadreur(request, id=0):
    if request.method == "GET":
        if id==0:            
            context = {
                'EncadreurForm': EncadreurForm(),
                'form':ContactMessageForm()
            }
            return render(request, 'GestionStagiaires/Encadreur/AddEncadreur.html', context)
        else:            
            encadreurForm = Encadreur.objects.get(pk=id)
            context = {
                'EncadreurForm': EncadreurForm(instance=encadreurForm),
                'form':ContactMessageForm()
            }
            return render(request, 'GestionStagiaires/Encadreur/AddEncadreur.html', context)
    elif request.method == "POST":
        if id == 0:
            encadreur = EncadreurForm(request.POST)
            if encadreur.is_valid():
                encadreur.save()
                context = { 'Messages': "Enregistrement ENCADREUR Effectué avec success"}
                return render(request, 'GestionStagiaires/Encadreur/EncadreurConfirmMessage.html', context)
            else:
                context = { 'Messages': "Echec d'Enregistrement"}
            return render(request, 'GestionStagiaires/Encadreur/EncadreurConfirmMessage.html', context)
        else:
            encadreurForm = Encadreur.objects.get(pk=id)
            encadreur = EncadreurForm(request.POST,instance=encadreurForm)
            if encadreur.is_valid():
                encadreur.save()
                context = { 'Messages': "Mise ajour Encadreur Effectué avec Success"} 
                return render(request, 'GestionStagiaires/Encadreur/EncadreurConfirmMessage.html', context)
            else:
                context = { 'Messages': "Echec de Mise ajour"}
                return render(request, 'GestionStagiaires/Encadreur/EncadreurConfirmMessage.html', context)
    else:
        context = {
            'EncadreurForm': EncadreurForm(),
            'form':ContactMessageForm()
        }
        return render(request, 'GestionStagiaires/Encadreur/AddEncadreur.html', context)

def listesEncadreur(request):
    context = {
        'Encadreur_listes': Encadreur.objects.all(),
        'form':ContactMessageForm()
    }
    return render(request, 'GestionStagiaires/Encadreur/listesEncadreurs.html', context)

def deleteEncadreur(request, id):
    encadreur = Encadreur.objects.get(pk=id)
    context = {
        'Encadreur_listes': Encadreur.objects.all(),
        'form':ContactMessageForm(),
        'encadreur':Encadreur.objects.get(pk=id)
    }
    if request.method == "POST":
        encadreur.delete()
        return render(request, 'GestionStagiaires/Encadreur/listesEncadreurs.html', context)
    return render(request,'GestionStagiaires/Encadreur/DeleteEncadreur.html', context)

def CreateDirection(request,id=0):
    if request.method == "GET":
        if id==0:
            context = {'form':ContactMessageForm(),'directionForm':DirectionForm()
            }
            return render(request,'GestionStagiaires/Direction/AddDirection.html',context)
        else:
            direction = Direction.objects.get(pk=id)
            context = { 'form':ContactMessageForm(),'directionForm':DirectionForm(instance=direction)}
        return render(request, 'GestionStagiaires/Direction/AddDirection.html',context) 

    elif request.method == "POST":
        if id==0:
            direction = DirectionForm(request.POST)
            if direction.is_valid():
                direction.save()
                context = { 'Messages': "Enregistrement DIRECTION Effectué avec success"}
                return render(request, 'GestionStagiaires/Direction/DirectionConfirmMessage.html', context)
            else:
                context = { 'Messages': "Echec d'Enregistrement DIRECTION"}
            return render(request, 'GestionStagiaires/Encadreur/EncadreurConfirmMessage.html', context)
        else:
            directionForm = Direction.objects.get(pk=id)
            direction = DirectionForm(request.POST,instance=directionForm)
            if direction.is_valid():
                direction.save()
                context = { 'Messages': "Modification DIRECTION Effectué avec success"}
                return render(request, 'GestionStagiaires/Direction/DirectionConfirmMessage.html', context)
            else:
                context = { 'Messages': "Echec Modification DIRECTION"}
            return render(request, 'GestionStagiaires/Direction/DirectionConfirmMessage.html', context)
    else:
        return HttpResponse('Create Direct')

def deleteDirection(request, id):
    direction = get_object_or_404(Direction, pk=id) #Direction.objects.get(pk=id)
    context = {
        'direction_list': Direction.objects.all(),
        'form':ContactMessageForm(),
        'direction':get_object_or_404(Direction, pk=id)
    }
    if request.method == "POST":
        direction.delete()
        return render(request, 'GestionStagiaires/Direction/listeDirections.html', context)
    return render(request,'GestionStagiaires/Direction/deleteDirection.html', context)

def listeDirections(request):
    context = {
        'form':ContactMessageForm(),
        'direction_list': Direction.objects.all()
    }
    return render(request, 'GestionStagiaires/Direction/listeDirections.html', context)

#@csrf_exempt
def CreateDirectionAjax(request,id=0):
    if request.method == "GET":
        if id==0:      
            return HttpResponse('Id Direction 0 fait retour')
        else:
            direct = Direction.objects.values() #get_object_or_404(Direction, pk=id)
            direction_data = list(direct)
            return JsonResponse({'status':'recup', 'direction_data':direction_data})
    elif request.method == "POST":
        print(request.POST)
        direction = DirectionForm(request.POST)
        if direction.is_valid():
            nom_directs = request.POST['nom_direction']
            dirc = Direction(nom_direction =  nom_directs)
            dirc.save()
            direct = Direction.objects.values() #Direction.objects.all()
            print(direct)
            direction_data = list(direct)
            return JsonResponse({'status':'Save', 'direction_data':direction_data})
        else:
            return JsonResponse({'status':0})

def CreateEncadreurAjax(request):
    if request.method == "GET":
        idDirection = request.POST['id_direction']
        print(idDirection)
        return JsonResponse({'status':'recup', 'id_Dir':idDirection})
    elif request.method == "POST":
        print(request.POST)
        encadreur = EncadreurForm(request.POST)
        if encadreur.is_valid():
            nom = request.POST['nom_encad']
            postnomd = request.POST['postnom_encad']
            prenom = request.POST['prenom_encad']
            sexe = request.POST['sexe_encad']
            encad = Encadreur(nom_encad = nom, postnom_encad = postnomd,prenom_encad = prenom, sexe_encad = sexe )
            encad.save()
            encad = Encadreur.objects.values() #Direction.objects.all()
            print(encad)
            encad_data = list(encad)
            return JsonResponse({'status':'Save', 'direction_data':encad_data})
        else:
            return JsonResponse({'status':0})

def registerCount(request):
    formRegister = UserCreationForm()
    if request.method == "POST":
        formRegister = CreateUserForm(request.POST) 
        if formRegister.is_valid():
            #formRegister.save()
            user = formRegister.cleaned_data.get('username')
            messages.success((request), 'Account was created for ' + user)
            return redirect("/login")
            #print(request.POST)
        #else:
            #print(request.POST)
            #return HttpResponse('Echec Save Login Exist')
    context = {
        'formRegister':formRegister
    }
    return render(request, 'GestionStagiaires/Accounts/register.html', context)

def loginConnect(request):

    if request.method == 'POST':
        userName = request.POST.get('username')
        passWord = request.POST.get('password')
        user = authenticate('request', username=userName, password=passWord)

        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.info(request, "Username OR password is incorrect")
    return render(request, 'GestionStagiaires/Accounts/login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')
@login_required(login_url='/login')
def dashBoard(request):
    return render(request,'GestionStagiaires/Accounts/dashboader.html')

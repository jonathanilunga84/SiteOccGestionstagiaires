from django.urls import path
from . import views

app_name = 'GestionStagiaires' 
urlpatterns = [  
    #path('', views.admins, name='admins'),
    #ex: /GestionStagiaires/
    path('', views.index, name='index'),
    #ex: /GestionStagiaires/createStagiaire 
    path('createStagiaire/', views.createStagiaire, name='createStagiaire'), 
    #ex: /GestionStagiaires/StagiaireUPDATE/id/
    path('StagiaireUPDATE/<int:id>/',views.createStagiaire, name='StagiaireUPDATE'),
    #ex: /GestionStagiaires/stagiaireConfirmEnregistrement
    path('stagiaireConfirmEnregistrement',views.stagiaireConfirmEnregistrement, name='stagiaireConfirmEnregistrement'),   
    #ex: /GestionStagiaires/listeStagiaires 
    path('listeStagiaires/', views.listeStagiaires, name='listeStagiaires'), 
    #ex: /GestionStagiaires/deleteStagiaire/id/ 
    path('deleteStagiaire/<str:pk>/', views.deleteStagiaire, name='deleteStagiaire'),  

    #ex: /GestionStagiaires/annoce
    path('annoce/', views.annoce, name='annoce'),
    #ex: /GestionStagiaires/contactMassage/
    path('contactMessage/', views.contactMessage, name='contactMessage'), 
    #ex: /GestionStagiaires/resultMessage/
    path('resultMessage/', views.resultMessage, name='resultMessage'),  
    path('<int:id>/', views.index, name='stagiaire_update'),  

    #Encadreur
    #ex: /GestionStagiaires/CreateEncadreur/
    path('CreateEncadreur/', views.CreateEncadreur, name='CreateEncadreur'),
    #ex: /GestionStagiaires/CreateEncadreurAjax/
    path('CreateEncadreurAjax/', views.CreateEncadreurAjax, name='CreateEncadreurAjax'),
    #ex: /GestionStagiaires/UpdateEncadreur/
    path('UpdateEncadreur/<int:id>/', views.CreateEncadreur, name='UpdateEncadreur'),
    #ex: /GestionStagiaires/listesEncadreur/
    path('listesEncadreur/', views.listesEncadreur, name='listesEncadreur'),
    #ex: /GestionStagiaires/deleteEncadreur/
    path('deleteEncadreur/<int:id>/', views.deleteEncadreur, name='deleteEncadreur'),

    #Direction
    #ex: /GestionStagiaires/CreateDirection/
    path('CreateDirection/', views.CreateDirection, name='CreateDirection'),
    #ex: /GestionStagiaires/CreateDirectionAjax/
    path('CreateDirectionAjax/', views.CreateDirectionAjax, name='CreateDirectionAjax'),
    path('CreateDirectionAjaxs/<str:id>/', views.CreateDirectionAjax, name='CreateDirectionAjaxs'),

    #ex: /GestionStagiaires/UpdateDirection/id/
    path('UpdateDirection/<int:id>/', views.CreateDirection, name='UpdateDirection'),
    #ex: /GestionStagiaires/deleteDirection/id/
    path('deleteDirection/<int:id>/', views.deleteDirection, name='deleteDirection'),
    #ex: /GestionStagiaires/listeDirections/
    path('listeDirections/', views.listeDirections, name='listeDirections'),

    #Register Count
    #ex: /GestionStagiaires/register/
    path('register/', views.registerCount, name='registerCount'),
    #ex: /GestionStagiaires/login/
    path('login/', views.loginConnect, name='login'),
    #ex: /GestionStagiaires/login/
    path('logout/', views.logoutUser, name='logout'),
    #ex: /GestionStagiaires/Dashboard/
    path('dashboard/', views.dashBoard, name='dashbord'),
]
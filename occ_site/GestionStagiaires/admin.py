from django.contrib import admin
from .models import ContactMessage, Direction, Encadreur,  Stagiaire

# Register your models here.
admin.site.register(ContactMessage)
admin.site.register(Direction)
admin.site.register(Encadreur)
admin.site.register(Stagiaire)
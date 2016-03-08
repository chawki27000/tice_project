from django.contrib import admin

# Register your models here.
from gestion.models import Administrateur, Formateur, Categorie, Formation, Apprenant
from gestion.models import Regroupement, Cours, Chapitre, Ressource, Animer, Test

admin.site.register(Administrateur)
admin.site.register(Formateur)
admin.site.register(Categorie)
admin.site.register(Formation)
admin.site.register(Apprenant)
admin.site.register(Regroupement)
admin.site.register(Cours)
admin.site.register(Chapitre)
admin.site.register(Ressource)
admin.site.register(Animer)
admin.site.register(Test)

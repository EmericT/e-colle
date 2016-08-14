#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views

urlpatterns = [
url(r'^$', views.connec,name="login_admin"),
url(r'^action$', views.action,name="action_admin"),
url(r'^action/config$', views.config,name="config"),
url(r'^action/configconfirm$', views.configconfirm,name="configconfirm"),
url(r'^action/classe$', views.classe,name="gestion_classe"),
url(r'^action/classe/modifier/(\d+)$', views.classemodif,name="modif_classe"),
url(r'^action/classe/supprimer/(\d+)$', views.classesuppr,name="suppr_classe"),
url(r'^action/matiere$', views.matiere,name="gestion_matiere"),
url(r'^action/matiere/modifier/(\d+)$', views.matieremodif,name="modif_matiere"),
url(r'^action/matiere/supprimer/(\d+)$', views.matieresuppr,name="suppr_matiere"),
url(r'^action/etab$', views.etab,name="gestion_etab"),
url(r'^action/etab/modifier/(\d+)$', views.etabmodif,name="modif_etab"),
url(r'^action/etab/supprimer/(\d+)$', views.etabsuppr,name="suppr_etab"),
url(r'^action/semaine$', views.semaine,name="gestion_semaine"),
url(r'^action/semaine/modifier/(\d+)$', views.semainemodif,name="modif_semaine"),
url(r'^action/semaine/supprimer/(\d+)$', views.semainesuppr,name="suppr_semaine"),
url(r'^action/eleve$', views.eleve,name="gestion_eleve"),
url(r'^action/eleve/modifier/(\d+(?:-\d+)*)$', views.elevemodif,name="modif_eleve"),
url(r'^action/eleve/supprimer/(\d+)$', views.elevesuppr,name="suppr_eleve"),
url(r'^action/eleve/ajouter$', views.eleveajout,name="ajout_eleve"),
url(r'^action/eleve/csv$', views.elevecsv,name="csv_eleve"),
url(r'^action/colleur$', views.colleur,name="gestion_colleur"),
url(r'^action/colleur/modifier/(\d+(?:-\d+)*)$', views.colleurmodif,name="modif_colleur"),
url(r'^action/colleur/supprimer/(\d+)$', views.colleursuppr,name="suppr_colleur"),
url(r'^action/colleur/ajouter$', views.colleurajout,name="ajout_colleur"),
url(r'^action/prof$', views.prof,name="gestion_prof"),
url(r'^action/prof/modifier/(\d+)$', views.profmodif,name="modif_prof"),
url(r'^action/ferie$', views.ferie,name="gestion_ferie"),
url(r'^action/ferie/modifier/(\d+)$', views.feriemodif,name="modif_ferie"),
url(r'^action/ferie/supprimer/(\d+)$', views.feriesuppr,name="suppr_ferie")
]
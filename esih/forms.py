#-*- coding: utf-8 -*-

from django import forms
from esih.models import Programme, Cours

choixprog=[('','..........')]

choixcours=[('','..........')]

for p in Programme.objects.all():
    choixprog.append((p,p))

for c in Cours.objects.all():
    choixcours.append((c.Code,c.Code))

choixgrade = (('','.........'),
              ('prepa','Propedeutique'),
              ('L1','1ère Année'),
              ('L2','2ème Année'),
              ('L3','3ème Année'),
              )

choixsemestre = (('','.........'),
                 ('S1','session1'),
                 ('S2','session2'),
                 ('Y','Année Entière'),
                 )

choixdomaine = (('','.........'),
                ('S&T','Sces et Technologie'),
                ('E&G','Economie et Gestion'),
                )

choixmention = (('','.........'),
                ('SI','Sce Informatique'),
                ('E&G','Economie et Gestion'),
                )

choixspecialite = (('','.........'),
                   ('TEL','Telecom'),
                   ('BDD','Base de donnees'),
                   ('ONE','Org. Net Economie'),
                   ('SdE',"Sce de l'entreprise"),
                   ('SC','Sce Comptable'),
                   )

choixtype = (('','.........'),
             ('Ob','Obligatoire'),
             ('Op','Optionnel'),
             )

choixlangue = (('','.........'),
               ('Fr','Francais'),
               ('Ang','Anglais'),
               ('Esp','Espagnol'),
               )

choixcible = (('','.........'),
              ('Etudiants','Etudiants'),
              ('Professeurs','Professeurs'),
              ('Autres','Autres'),
              )

choixdroit = (('','.........'),
              ('Guest','Guest'),
              ('Prof','Professeurs'),
              ('Admin','Administration'),
              )

choixcredit = (('','.........'),
              ('1','1'),
              ('2','2'),
              ('3','3'),
              ('4','4'),
              ('5','5'),
              ('6','6'),
              )

class formcodecours(forms.Form):
    Etablissement = forms.CharField(max_length=100)
    Grade = forms.ChoiceField(choixgrade)
    Semestre = forms.ChoiceField(choixsemestre)
    NomCours = forms.CharField(max_length=100)
    TypeCours = forms.ChoiceField(choixtype)
    Credit = forms.ChoiceField(choixcredit)
    Langue = forms.ChoiceField(choixlangue)
    Cible = forms.ChoiceField(choixcible)
    Objectif = forms.CharField(widget=forms.Textarea)
    Progcours = forms.ChoiceField(choixprog)


class formcodeprog(forms.Form):
    Domaine = forms.ChoiceField(choixdomaine)
    Mention = forms.ChoiceField(choixmention)
    Specialite = forms.ChoiceField(choixspecialite)
    #NomProg = forms.CharField(max_length=100)


class formcodeprof(forms.Form):
    NomProf = forms.CharField(max_length=100)
    PrenomProf = forms.CharField(max_length=100)
    TelProf = forms.IntegerField(label=u"Telephone   +")
    Email = forms.EmailField(label= u"Votre adresse mail")
    #CoursProf = forms.ChoiceField(choixcours)
    #CvProf = models.FileField(upload_to="fichier/")

from models import DescriptifCours
class formcodedesc(forms.ModelForm):
    class Meta:
        model = DescriptifCours
        exclude = ('ProfCours',)

class formlogin(forms.Form):
    Nom = forms.CharField(max_length=20)
    Prenom = forms.CharField(max_length=20)
    UserName = forms.CharField(max_length=20)
    Password = forms.CharField(widget=forms.PasswordInput)
    Droit = forms.ChoiceField(choixdroit)

class formlog(forms.Form):
    Utilisateur = forms.CharField(max_length=20)
    MotdePasse = forms.CharField(widget=forms.PasswordInput)


"""
#from django import forms
from models import Programme, Cours, Professeurs, DescriptifCours


class formcodeprog(forms.ModelForm):
    class Meta:
        model = Programme
        exclude = ('NomProg',)

class formcodecours(forms.ModelForm):
    class Meta:
        model = Cours
        exclude = ('Code','ProgCours',)

class formcodeprof(forms.ModelForm):
    class Meta:
        model = Professeurs
        exclude = ('CoursProf','CvProf')
"""

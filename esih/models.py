from django.db import models

# Create your models here.
class Programme (models.Model):
    Domaine = models.CharField(max_length=50)
    Mention =models.CharField(max_length=50)
    Specialite = models.CharField(max_length=50)
    NomProg = models.CharField(max_length=100)

    def __unicode__(self):
        return self.NomProg

class Cours (models.Model):
    Etablissement = models.CharField(max_length=50)
    Grade = models.CharField(max_length=20)
    Semestre = models.CharField(max_length=20)
    NomCours = models.CharField(max_length=20)
    TypeCours = models.CharField(max_length=20)
    Credit = models.IntegerField(max_length=5)
    Langue = models.CharField(max_length=20)
    Cible = models.CharField(max_length=20)
    Objectif = models.TextField()
    Code = models.CharField(max_length=100)
    ProgCours = models.ForeignKey(Programme)

    def __unicode__(self):
        return self.Code

class Professeurs (models.Model):
    NomProf = models.CharField(max_length=50)
    PrenomProf = models.CharField(max_length=50)
    TelProf = models.IntegerField(max_length=20)
    CvProf = models.URLField()
    Email = models.EmailField(max_length=70)

    def __unicode__(self):
        return "{0} {1}".format(self.NomProf, self.PrenomProf)

class DescriptifCours (models.Model):
    DescriptionCours = models.TextField()
    PlanCours = models.TextField()
    FormatCours = models.CharField(max_length=100)
    Ressources = models.TextField()
    PreRequis = models.URLField()
    Evaluation = models.TextField()
    ProfCours = models.ManyToManyField(Professeurs)
    Cour = models.ForeignKey(Cours,unique=True)

    def __unicode__(self):
        return self.Cour

class Login(models.Model):
    Nom = models.CharField(max_length=20)
    Prenom = models.CharField(max_length=20)
    UserName = models.CharField(max_length=20)#supposer Unique unique=True
    Password = models.CharField(max_length=20)
    Droit = models.CharField(max_length=20)

    def __unicode__(self):
        return self.UserName

"""
class DescriptionCours (models.Model):
     CrediEcts = models.CharField(max_length=10)
     Etablissement = models.CharField(max_length=20)
     CvProfesseur = models.CharField(max_length=50)
     PublicCible = models.CharField(max_length=20)
     PreRequis = models.CharField(max_length=100)
     Objectif = models.CharField(max_length=100)
     Description = models.CharField(max_length=50)
     PlanCours = models.CharField(max_length=200)
     Format = models.CharField(max_length=50)
     Ressource = models.CharField(max_length=50)
     Evalution = models.CharField(max_length=50)
     cours = models.ForeignKey('Cours')



class Appartenir (models.Model):
    TypeCours = models.CharField(max_length=20)
    CoursApp = models.ForeignKey(Cours)
    ProgApp = models.ForeignKey(Programme)

    def __unicode__(self):
        return "{0} appartient a {1}".format(self.CoursApp, self.ProgApp)

class Dispenser (models.Model):
    CoursDisp = models.ForeignKey(Cours)
    ProfDisp = models.ForeignKey(Professeurs)

    def __unicode__(self):
        return "{0} dispense {1}".format(self.ProfDisp, self.CoursDisp)

class DescriptifCours (models.Model):
    DescriptionCours = models.TextField()
    PlanCours = models.TextField()
    FormatCours = models.CharField(max_length=100)
    Ressources = models.TextField()
    Evaluation = models.TextField()
    Cour = models.OneToOneField(Cours)
    ProfCours = models.ManyToManyField(Professeurs, through='Dispenser')

"""


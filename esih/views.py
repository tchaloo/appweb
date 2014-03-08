from django.shortcuts import render, redirect
from esih.forms import formcodecours, formcodeprof, formcodeprog, formcodedesc, formlogin, formlog
from esih.models import Cours, Programme, Professeurs, Login

from django.http import HttpResponse

# Create your views here.

#Vue pour le formulaire de code_cours:

def foncaccueil(request):
    return render(request, 'esih/accueil.html', locals())

def foncformcodecours(request):
    if 'idsession' not in request.session:
        return redirect("/login/")
    else:
        login=Login.objects.get(UserName=request.session['idsession']).Droit
        if (login!='Admin'):
            nondroit=True
            return render(request, 'esih/nondroit.html', locals())

    if request.method == 'POST':
        form = formcodecours(request.POST)
        if form.is_valid():
            etablissement = form.cleaned_data['Etablissement']
            grade = form.cleaned_data['Grade']
            semestre = form.cleaned_data['Semestre']
            nomcours = form.cleaned_data['NomCours']
            credit = form.cleaned_data['Credit']
            langue = form.cleaned_data['Langue']
            cible = form.cleaned_data['Cible']
            objectif = form.cleaned_data['Objectif']
            programme = form.cleaned_data['Progcours']
            typecours = form.cleaned_data['TypeCours']
            codecours = etablissement + '-' + grade + semestre + '-' + nomcours
            codeattachement = programme + '-' + typecours + '-' + langue

            for p in Programme.objects.all():
                if (p.NomProg == programme):
                    prog=p

            cours=Cours.objects.create(Etablissement=etablissement, Grade=grade, Semestre=semestre, NomCours=nomcours,
                                       Credit=credit, Langue=langue, Cible=cible, Objectif=objectif, Code=codecours, ProgCours=prog)

            form=formcodecours()
            envoicodecours = True
    else:
        form = formcodecours()
    return render(request, 'esih/formcodecours.html', locals())

#Vue pour le formulaire de code_Programme:

def foncformcodeprog(request):
    if 'idsession' not in request.session:
        return redirect("/login/")
    else:
        login=Login.objects.get(UserName=request.session['idsession']).Droit
        if (login!='Admin'):
            nondroit=True
            return render(request, 'esih/nondroit.html', locals())

    if request.method == 'POST':
        form = formcodeprog(request.POST)
        if form.is_valid():
            domaine = form.cleaned_data['Domaine']
            mention = form.cleaned_data['Mention']
            specialite = form.cleaned_data['Specialite']
            nomprog = domaine +'-' + mention + '-' + specialite

            prog=Programme.objects.create(Domaine=domaine, Mention=mention, Specialite=specialite, NomProg=nomprog)

            form = formcodeprog()
            envoicodeprog = True
    else:
        form = formcodeprog()
    return render(request, 'esih/formcodeprog.html', locals())

#Vue pour le formulaire de code_Professeur:

def foncformcodeprof(request):
    if 'idsession' not in request.session:
        return redirect("/login/")
    else:
        login=Login.objects.get(UserName=request.session['idsession']).Droit
        if (login!='Admin' and login!='Prof'):
            nondroit=True
            return render(request, 'esih/nondroit.html', locals())

    if request.method == 'POST':
        form = formcodeprof(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['NomProf']
            prenom = form.cleaned_data['PrenomProf']
            telephone = form.cleaned_data['TelProf']
            email = form.cleaned_data['Email']
            #cvprof = form.cleaned_data['CvProf']
            #cours = form.cleaned_data['CoursProf']
            professeur = nom + ' ' + prenom

            #for c in Cours.objects.all():
             #   if (c.Code == cours):
              #      cours=c

            prof=Professeurs.objects.create(NomProf=nom, PrenomProf=prenom, TelProf=telephone, Email=email)


            form=formcodeprof()
            envoicodeprof = True
    else:
        form = formcodeprof()
    return render(request, 'esih/formcodeprof.html', locals())

def foncformcodedesc(request):
    if 'idsession' not in request.session:
        return redirect("/login/")
    else:
        login=Login.objects.get(UserName=request.session['idsession']).Droit
        if (login!='Admin' and login!='Prof'):
            nondroit=True
            return render(request, 'esih/nondroit.html', locals())

    if request.method == 'POST':
        form = formcodedesc(request.POST)
        if form.is_valid():
            descriptioncours = form.cleaned_data['DescriptionCours']
            plancours = form.cleaned_data['PlanCours']
            formatcours = form.cleaned_data['FormatCours']
            ressources = form.cleaned_data['Ressources']
            evaluation = form.cleaned_data['Evaluation']
            cour = form.cleaned_data['Cour']

            from esih.models import DescriptifCours


            desc=DescriptifCours.objects.create(DescriptionCours=descriptioncours, PlanCours=plancours, FormatCours=formatcours,
                                       Ressources=ressources, Evaluation=evaluation, Cour=cour,)

            form=formcodedesc()
            envoicodedesc = True
    else:
        form = formcodedesc()
    return render(request, 'esih/formcodedesc.html', locals())


def fonclistercours(request):
    if 'idsession' not in request.session:
        return redirect("/login/")
    else:
        login=Login.objects.get(UserName=request.session['idsession']).Droit
        if (login!='Admin' and login!='Prof' and login!='Guest'):
            nondroit=True
            return render(request, 'esih/nondroit.html', locals())

    listecours = Cours.objects.all()
    return render(request, 'esih/listercours.html', {'listecours':listecours})

def fonclisterprog(request):
    if 'idsession' not in request.session:
        return redirect("/login/")
    else:
        login=Login.objects.get(UserName=request.session['idsession']).Droit
        if (login!='Admin' and login!='Prof' and login!='Guest'):
            nondroit=True
            return render(request, 'esih/nondroit.html', locals())

    listeprog = Programme.objects.all()
    return render(request, 'esih/listerprog.html', {'listeprogs':listeprog})

def fonclisterprof(request):
    if 'idsession' not in request.session:
        return redirect("/login/")
    else:
        login=Login.objects.get(UserName=request.session['idsession']).Droit
        if (login!='Admin' and login!='Prof' and login!='Guest'):
            nondroit=True
            return render(request, 'esih/nondroit.html', locals())

    listeprof = Professeurs.objects.all()
    return render(request, 'esih/listerprof.html', {'listeprofs':listeprof})


def supprimerprog(request, id):
    if 'idsession' not in request.session:
        return redirect("/login/")
    else:
        login=Login.objects.get(UserName=request.session['idsession']).Droit
        if (login!='Admin'):
            nondroit=True
            return render(request, 'esih/nondroit.html', locals())

    prog = Programme.objects.get(id=id)
    prog.delete()
    return redirect("/../listeprog/")

def supprimercours(request, id):
    if 'idsession' not in request.session:
        return redirect("/login/")
    else:
        login=Login.objects.get(UserName=request.session['idsession']).Droit
        if (login!='Admin'):
            nondroit=True
            return render(request, 'esih/nondroit.html', locals())

    cours = Cours.objects.get(id=id)
    cours.delete()
    return redirect("/../listecours/")

def supprimerprof(request, id):
    if 'idsession' not in request.session:
        return redirect("/login/")
    else:
        login=Login.objects.get(UserName=request.session['idsession']).Droit
        if (login!='Admin' and login!='Prof'):
            nondroit=True
            return render(request, 'esih/nondroit.html', locals())

    prof = Professeurs.objects.get(id=id)
    prof.delete()
    return redirect("/../listeprof/")


def modifierprog(request, id):
    if 'idsession' not in request.session:
        return redirect("/login/")
    else:
        login=Login.objects.get(UserName=request.session['idsession']).Droit
        if (login!='Admin'):
            nondroit=True
            return render(request, 'esih/nondroit.html', locals())

    prog = Programme.objects.get(id=id)
    form = formcodeprog({'Domaine':prog.Domaine, 'Mention':prog.Mention, 'Specialite':prog.Specialite})

    return render(request, 'esih/modifierprog.html', locals())

def modifiercours(request, id):
    if 'idsession' not in request.session:
        return redirect("/login/")
    else:
        login=Login.objects.get(UserName=request.session['idsession']).Droit
        if (login!='Admin'):
            nondroit=True
            return render(request, 'esih/nondroit.html', locals())

    cours = Cours.objects.get(id=id)
    form = formcodecours({'Etablissement':cours.Etablissement, 'Grade':cours.Grade, 'Semestre':cours.Semestre,
                         'NomCours':cours.NomCours, 'Credit':cours.Credit, 'Langue':cours.Langue, 'Cible':cours.Cible,
                         'Objectif':cours.Objectif, 'TypeCours':cours.TypeCours, 'Progcours':cours.ProgCours,})

    return render(request, 'esih/modifiercours.html', locals())

def modifierprof(request, id):
    if 'idsession' not in request.session:
        return redirect("/login/")
    else:
        login=Login.objects.get(UserName=request.session['idsession']).Droit
        if (login!='Admin' and login!='Prof'):
            nondroit=True
            return render(request, 'esih/nondroit.html', locals())

    prof = Professeurs.objects.get(id=id)
    form = formcodeprof({'NomProf':prof.NomProf, 'PrenomProf':prof.PrenomProf, 'TelProf':prof.TelProf, 'Email':prof.Email})
    return render(request, 'esih/modifierprof.html', locals())

def modifierprog2(request, id):
    if 'idsession' not in request.session:
        return redirect("/login/")
    else:
        login=Login.objects.get(UserName=request.session['idsession']).Droit
        if (login!='Admin'):
            nondroit=True
            return render(request, 'esih/nondroit.html', locals())

    prog = Programme.objects.get(id=id)
    if request.method == 'POST':
        form = formcodeprog(request.POST)
        if form.is_valid():
            domaine= form.cleaned_data['Domaine']
            mention= form.cleaned_data['Mention']
            specialite= form.cleaned_data['Specialite']

            nomprog = domaine +'-' + mention + '-' + specialite

            prog.Domaine=domaine
            prog.Mention=mention
            prog.Specialite=specialite
            prog.NomProg=nomprog
            prog.save()

            form = formcodeprog()
            modifprog = True
    else:
        form = formcodeprog()
    return render(request, 'esih/modifierprog2.html', locals())


def modifierprof2(request, id):
    if 'idsession' not in request.session:
        return redirect("/login/")
    else:
        login=Login.objects.get(UserName=request.session['idsession']).Droit
        if (login!='Admin' and login!='Prof'):
            nondroit=True
            return render(request, 'esih/nondroit.html', locals())

    prof = Professeurs.objects.get(id=id)
    if request.method == 'POST':
        form = formcodeprof(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['NomProf']
            prenom = form.cleaned_data['PrenomProf']
            telephone = form.cleaned_data['TelProf']
            email = form.cleaned_data['Email']
            #cvprof = form.cleaned_data['CvProf']
            #cours = form.cleaned_data['CoursProf']

            professeur = nom + ' ' + prenom

            prof.NomProf=nom
            prof.PrenomProf=prenom
            prof.TelProf=telephone
            prof.Email=email
            prof.save()

            form = formcodeprof()
            modifprof = True
    else:
        form = formcodeprof()
    return render(request, 'esih/modifierprof2.html', locals())

def modifiercours2(request, id):
    if 'idsession' not in request.session:
        return redirect("/login/")
    else:
        login=Login.objects.get(UserName=request.session['idsession']).Droit
        if (login!='Admin'):
            nondroit=True
            return render(request, 'esih/nondroit.html', locals())

    cours = Cours.objects.get(id=id)
    if request.method == 'POST':
        form = formcodecours(request.POST)
        if form.is_valid():
            etablissement = form.cleaned_data['Etablissement']
            grade = form.cleaned_data['Grade']
            semestre = form.cleaned_data['Semestre']
            nomcours = form.cleaned_data['NomCours']
            credit = form.cleaned_data['Credit']
            langue = form.cleaned_data['Langue']
            cible = form.cleaned_data['Cible']
            objectif = form.cleaned_data['Objectif']

            programme = form.cleaned_data['Progcours']
            typecours = form.cleaned_data['TypeCours']

            codecours = etablissement + '-' + grade + semestre + '-' + nomcours
            codeattachement = programme + '-' + typecours + '-' + langue

            cours.Etablissement=etablissement
            cours.Grade=grade
            cours.Semestre=semestre
            cours.NomCours=nomcours
            cours.Credit=credit
            cours.Langue=langue
            cours.Cible=cible
            cours.Objectif=objectif
            cours.TypeCours=typecours
            cours.Code=codecours

            for p in Programme.objects.all():
                if (p.NomProg == programme):
                    prog=p

            cours.ProgCours=prog
            cours.save()

            form = formcodecours()
            modifcours = True
    else:
        form = formcodecours()
    return render(request, 'esih/modifiercours2.html', locals())


def fonclogin(request):
    if 'idsession' not in request.session:
        return redirect("/login/")
    else:
        login=Login.objects.get(UserName=request.session['idsession']).Droit
        if (login!='Admin'):
            nondroit=True
            return render(request, 'esih/nondroit.html', locals())

    if request.method == 'POST':
        form = formlogin(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['Nom']
            prenom = form.cleaned_data['Prenom']
            username = form.cleaned_data['UserName']
            password = form.cleaned_data['Password']
            droit = form.cleaned_data['Droit']

            log=Login.objects.create(Nom=nom, Prenom=prenom, UserName = username, Droit=droit, Password=password)

            form = formlogin()
            envoilogin = True
    else:
        form = formlogin()
    return render(request, 'esih/formlogin.html', locals())

def fonclog(request):
    if request.method == 'POST':
        form = formlog(request.POST)
        if form.is_valid():
            utilisateur = form.cleaned_data['Utilisateur']
            motdepasse = form.cleaned_data['MotdePasse']
            try:
                login = Login.objects.get(UserName=utilisateur)
                if login.Password == motdepasse:
                    request.session['idsession']=login.UserName
                    return redirect("/../")
            except:
                pass


            form = formlog()
    else:
        form = formlog()
    return render(request, 'esih/formlog.html', locals())


def fonclogout(request):
    del request.session['idsession']
    return redirect("/../")
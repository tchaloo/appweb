#-*- coding: utf-8 -*-

from django import forms

choix = (('1','Propedeutique'), ('2','L1'), ('3','L2'), ('4','L3'))
class Formulaire(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    liste = forms.ChoiceField(widget=forms.Select, choices=choix)
    envoyeur = forms.EmailField(label= u"Votre adresse mail")
    renvoi = forms.BooleanField(help_text= u"Cochez si vous souhaitez obtenir une copie du mail envoyé.",
            required=False)

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'appweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),

### Les URLS de l'application exo:
        # url(r'^accueilexo/$', 'exo.views.home'),
        # url(r'^$', 'exo.views.fonctiontpl'),
        # url(r'^essai/$', 'exo.views.fonctionessai'),
        # #url(r'^addition(?p<nombre1\d+>)/(?p<nombre2>\d+)/$', 'exo.views.fonctionadd'),
        # url(r'^formulaire/$', 'exo.views.fonctionform'),

### Les URLS de l'application esih
        url(r'^$', 'esih.views.foncaccueil'),
        url(r'^formcours/$', 'esih.views.foncformcodecours'),
        url(r'^formprog/$', 'esih.views.foncformcodeprog'),
        url(r'^formprof/$', 'esih.views.foncformcodeprof'),
        url(r'^formdescriptif/$', 'esih.views.foncformcodedesc'),
        url(r'^listecours/$', 'esih.views.fonclistercours'),
        url(r'^listeprog/$', 'esih.views.fonclisterprog'),
        url(r'^listeprof/$', 'esih.views.fonclisterprof'),
        url(r'^modifierprog/(?P<id>\d+)$', 'esih.views.modifierprog'),
        url(r'^modifiercours/(?P<id>\d+)$', 'esih.views.modifiercours'),
        url(r'^modifierprof/(?P<id>\d+)$', 'esih.views.modifierprof'),
        url(r'^modifierprog2/(?P<id>\d+)/$', 'esih.views.modifierprog2'),
        url(r'^modifierprof2/(?P<id>\d+)/$', 'esih.views.modifierprof2'),
        url(r'^modifiercours2/(?P<id>\d+)/$', 'esih.views.modifiercours2'),
        url(r'^supprimerprog/(?P<id>\d+)$', 'esih.views.supprimerprog'),
        url(r'^supprimercours/(?P<id>\d+)$', 'esih.views.supprimercours'),
        url(r'^supprimerprof/(?P<id>\d+)$', 'esih.views.supprimerprof'),
        url(r'^inscription/$', 'esih.views.fonclogin'),
        url(r'^login/$', 'esih.views.fonclog'),
        url(r'^logout/$', 'esih.views.fonclogout'),


        #url(r'^modifcours/(\d+)/$', 'esih.views.foncformcodeprof'),

)

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^create/$','main.views.create',name='create'),
    url(r'^oth/(?P<oth_id>[a-zA-Z0-9]+)','main.views.view_oth',name='view_oth'),
    url(r'^oth/(?P<oth_id>[a-zA-Z0-9]+/q/(?P<question_id>[a-zA-Z0-9]+))',
    'main.views.view_oth_question',name='view_oth_question'),


  
]

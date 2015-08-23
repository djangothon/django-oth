from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^create/$','main.views.create',name='create'),
    url(r'^add_question/(?P<oth_id>[a-zA-Z0-9]+)$','main.views.add_question_to_oth',
    	name='add_question_to_oth'),
    url(r'^oth/(?P<oth_id>[a-zA-Z0-9]+)','main.views.view_oth',name='view_oth'),
    url(r'^oth/(?P<oth_id>[a-zA-Z0-9]+/q/(?P<question_id>[a-zA-Z0-9]+))',
    	'main.views.view_oth_question',name='view_oth_question'),
    url(r'^leaderboard/(?P<oth_id>[a-zA-Z0-9]+)','main.views.leaderboard',
    	name='leaderboard')
  
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT})
        ]
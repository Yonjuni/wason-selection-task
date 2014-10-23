from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^loadQuestions$', 'selectionTask.views.load_questions', name='load_questions'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*', 'selectionTask.views.home', name='home'),
)

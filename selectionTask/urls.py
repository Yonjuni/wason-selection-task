from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^assign$', 'selectionTask.views.assign', name='assign'),
    url(r'^submit', 'selectionTask.views.submit', name='submit'),
)


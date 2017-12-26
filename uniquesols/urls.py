from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
admin.autodiscover()


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG}),
    url(r'', include('unique.urls')),

]

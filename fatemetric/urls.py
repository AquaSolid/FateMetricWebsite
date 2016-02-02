"""fatemetric URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include, patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from main.views import blog_sitemap, custom_404, custom_500
from django.http import HttpResponse

from django.conf.urls import handler404, handler500
sitemaps = {
    'blogs': blog_sitemap
}

urlpatterns = [
    # Django URLs
    url(r'^admin/', admin.site.urls),
    # Django Registration 2.0.4
    url(r'^accounts/', include('registration.backends.hmac.urls')),

    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow:", content_type="text/plain")),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # FateMetric URLs
    url(r'^', include('main.urls')),
    url(r'^blog/', include('blog.urls')),
    #url(r'^', include('chat.urls')),
    #url(r'^', include('games.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG is False:   #if DEBUG is True it will be served automatically
    urlpatterns += patterns('',
            url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

handler404 = 'main.views.custom_404'

handler500 = 'main.views.custom_500'
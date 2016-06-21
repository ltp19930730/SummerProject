"""CourseYelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url , include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),
    # url(r'^contact/', include('SearchCourse.urls')),

    url(r'^home/$','Homepage.views.home', name = 'home'),
    url(r'^about/$','Homepage.views.about', name = 'about'),
    url(r'^team/$','Homepage.views.team', name = 'team'),
    url(r'^contact/$','Homepage.views.contact', name = 'contact'),
    url(r'^rating/', include('Rates.urls')),
    url(r'^course/', include('SearchCourse.urls'),name = 'course'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

from django.conf.urls import url , include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', 'SearchCourse.views.archives'),
    url(r'^search/$','SearchCourse.views.web_search'),
    url(r'^detail/$', 'SearchCourse.views.course_detail'),
]

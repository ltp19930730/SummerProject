from django.contrib import admin

# Register your models here.
from .models import CourseData,Tag
#
#
admin.site.register(CourseData)
admin.site.register(Tag)

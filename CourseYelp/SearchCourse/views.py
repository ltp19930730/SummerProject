from django.shortcuts import render
from django.http import HttpResponse
from SearchCourse.models import CourseData
# Create your views here.

def result(request):
    post_list = CourseData.objects.all()
    return render(request, 'result.html', {'post_list' : post_list})

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from SearchCourse.models import CourseData
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.




def archives(request) :
    try:
        course_list = CourseData.objects.all().order_by('course_name')
        paginator = Paginator(course_list,8)
        page = request.GET.get('page')
        try:
            course_list = paginator.page(page)
        except PageNotAnInteger:
            course_list = paginator.page(1)
        except EmptyPage:
            course_list = paginator.paginator(paginator.num_pages)
    except CourseData.DoesNotExist :
        raise Http404
    return render(request, 'searchresult.html', {'course_list' : course_list,
                                            'error' : False})

def web_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'searchsection.html')
        else:
            course_list = CourseData.objects.filter(course_name__icontains = s)
            if len(course_list) == 0 :
                return render(request,'searchresult.html',{'course_list':course_list,
                                                    'error' : True})
            else :
                return render(request,'searchresult.html',{'course_list':course_list,
                                                    'error' : False})
    return redirect('/')

def course_detail(request,id):
    instance = get_object_or_404(CourseData,id = id)
    context = {
        "title":instance.course_name,
        "instance":instance,
    }
    return render(request,'course_detail.html',context)

def search_tag(request,tag) :
    try:
        course_list = CourseData.objects.filter(tags__name__startswith=tag) #contains
    except CourseData.DoesNotExist :
        raise Http404
    return render(request, 'searchresult.html', {'course_list' : course_list})

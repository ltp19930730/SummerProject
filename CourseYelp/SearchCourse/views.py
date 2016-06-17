from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from SearchCourse.models import CourseData
# Create your views here.




def archives(request) :
    try:
        post_list = CourseData.objects.all().order_by('course_name')
    except CourseData.DoesNotExist :
        raise Http404
    return render(request, 'searchresult.html', {'post_list' : post_list,
                                            'error' : False})

def web_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'searchsection.html')
        else:
            post_list = CourseData.objects.filter(course_name__icontains = s)
            if len(post_list) == 0 :
                return render(request,'searchresult.html',{'post_list':post_list,
                                                    'error' : True})
            else :
                return render(request,'searchresult.html',{'post_list':post_list,
                                                    'error' : False})
    return redirect('/')

def course_detail(request,id):
    instance = get_object_or_404(CourseData,id = id)
    context = {
        "title":instance.course_name,
        "instance":instance,
    }
    return render(request,'course_detail.html',context)

from django.shortcuts import render
from django.http import HttpResponse
from SearchCourse.models import CourseData
# Create your views here.




def archives(request) :
    try:
        post_list = CourseData.objects.all()
    except CourseData.DoesNotExist :
        raise Http404
    return render(request, 'searchresult.html', {'post_list' : post_list,
                                            'error' : False})
def web_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'base.html')
        else:
            post_list = CourseData.objects.filter(course_name__icontains = s)
            if len(post_list) == 0 :
                return render(request,'searchresult.html',{'post_list':post_list,
                                                    'error' : True})
            else :
                return render(request,'searchresult.html',{'post_list':post_list,
                                                    'error' : False})
    return redirect('/')

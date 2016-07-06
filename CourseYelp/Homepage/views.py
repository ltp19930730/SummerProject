from django.shortcuts import render
from .forms import ContactForm,SignUpForm
from django.core.mail import send_mail
from django.conf import settings
from SearchCourse.models import Tag
# Create your views here.

def home(request):
    tags_list = Tag.objects.all().order_by('name')

    context = {
            "tags_list":tags_list,
    }
    return render(request, 'home.html', context)


def contact(request):
    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key in form.cleaned_data:
        #     print (key)
        #     print (form.cleaned_data.get(key))
        # in python 2.x it is iteritems() but in 3.x it is just items()
        for key,value in form.cleaned_data.items():
            print (key,value)
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        # print email, message, full_name
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email,'tluo4@stevens.edu']
        contact_message ="%s:%s via %s"%(
                    form_full_name,
                    form_message,
                    form_email)
        some_html_message = """
        <h1> hello you are welcome</h1>
        """
        send_mail(subject,
                 contact_message,
                 from_email,
                 to_email,
                 html_message = some_html_message,
                 fail_silently = False)

    context = {
        "title": title,
        "form": form,
    }
    return render(request,"forms.html",context)


def about(request):
    return render(request,"about.html",{})

def search(request):
    return render(request,"searchsection.html",{})

def team(request):
    return render(request,"team.html",{})

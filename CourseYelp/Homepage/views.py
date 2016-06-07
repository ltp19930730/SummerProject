from django.shortcuts import render
from .forms import ContactForm,SignUpForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    title = 'Welcome'
    # if request.user.is_authenticated():
    #     title = "My Title %s" %(request.user)

    #add a form
    # if request.method == "POST":
    #     print (request.POST)
    form = SignUpForm(request.POST or None)

    context = {
        "title" : title,
        "form" : form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        #print (request.POST['email'])
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        instance.save()

        context = {
            "title" : "Thank you"
        }
    return render(request,"base.html",context)

def contact(request):
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
        "form": form,
    }
    return render(request,"forms.html",context)

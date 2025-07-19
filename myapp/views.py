from django.shortcuts import render
from .models import Notice
from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages

SCHOOL_NAME = "Children Growth Public School"
Mobile_number="09839086105"
address='Moti Nagar, Gujju Purwa, Jajmau, Kanpur, Uttar Pradesh 208010'
map_embed_code ='''<iframe src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3572.623273091606!2d80.393295!3d26.4356312!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x399c41d96700341d%3A0xef5325533db51d3e!2sChildren%20Growth%20Public%20School-%20Best%20Pre%20School!5e0!3m2!1sen!2sin!4v1752945945459!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'''

hindi_name ='राम लखन भट्ट इंटरनेशनल स्कूल'

# notices='Admission open for 2024-25 ||  Download Prospectus from website ||  Scholarship form available till 31st July ||  For help, contact office at 01234-567890'
# notices='Admission open for 2024-25'

def home(request):
    notices = Notice.objects.order_by('-created_at')[:10]  # latest 10 notices
    return render(request, 'index.html', 
            {'notices': notices,
             'school_name': SCHOOL_NAME ,
             'hindi_name':hindi_name,
    'Mobile_number':Mobile_number,
    'address':address})

def about(request):
    return render(request,'about.html',
            {'school_name': SCHOOL_NAME ,
            'hindi_name':hindi_name,
            'Mobile_number':Mobile_number,
            'address':address})

def principal(request):
    return render(request,'principal.html',
            {'school_name': SCHOOL_NAME ,
            'hindi_name':hindi_name,
            'Mobile_number':Mobile_number,
            'address':address})

def admission(request):
    return render(request,'admission.html',
    {'school_name': SCHOOL_NAME ,
            'hindi_name':hindi_name,
            'Mobile_number':Mobile_number,
            'address':address})

def gallery(request):
    return render(request,'gallery.html',
    {'school_name': SCHOOL_NAME ,
            'hindi_name':hindi_name,
            'Mobile_number':Mobile_number,
            'address':address})
def event(request):
    return render(request,'event.html',
    {'school_name': SCHOOL_NAME ,
            'hindi_name':hindi_name,
            'Mobile_number':Mobile_number,
            'address':address})



def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject", "")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')  # Replace with your actual contact page route name

    return render(request, "contact.html",
    {'school_name': SCHOOL_NAME ,
            'hindi_name':hindi_name,
            'Mobile_number':Mobile_number,
            'address':address})  # Replace with your actual template name


def mission(request):
    return render(request, "missoion-vission.html",
    {'school_name': SCHOOL_NAME ,
            'hindi_name':hindi_name,
            'Mobile_number':Mobile_number,
            'address':address})

def department(request):
    return render(request, "department.html",
    {'school_name': SCHOOL_NAME ,
            'hindi_name':hindi_name,
            'Mobile_number':Mobile_number,
            'address':address})
def admission(request):
    return render(request, "admission.html",
    {'school_name': SCHOOL_NAME ,
            'hindi_name':hindi_name,
            'Mobile_number':Mobile_number,
            'address':address})

def course(request):
    return render(request, "course.html",
    {'school_name': SCHOOL_NAME ,
            'hindi_name':hindi_name,
            'Mobile_number':Mobile_number,
            'address':address})

def extra_curricular(request):
    return render(request, "extra-curricular.html",
    {'school_name': SCHOOL_NAME ,
            'hindi_name':hindi_name,
            'Mobile_number':Mobile_number,
            'address':address})

def study_material(request):
    return render(request, "study-material.html",
    {'school_name': SCHOOL_NAME ,
            'hindi_name':hindi_name,
            'Mobile_number':Mobile_number,
            'address':address})



# admin=saurabh =same 

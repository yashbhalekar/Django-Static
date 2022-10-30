
from django.http import HttpResponse
from django.shortcuts import render
from course.models import CourseDetail

def home(request):
    return render(request ,"home.html")

def about(request):
    return render(request, "about.html")

def courses(request):
    serviceData = CourseDetail.objects.all()
    language_courses={
        'servicesData': serviceData
    }

    
    return render(request, "courses.html", language_courses )

def contact(request):
    return render(request, "contact.html")
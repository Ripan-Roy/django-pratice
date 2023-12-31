from django.http import HttpResponse
from django.shortcuts import render


def homePage(request):
    data = {
        'title': 'Home Page',
        'bdata': 'This is the body data',
        'clist': ['Python', 'Java', 'C++', 'C#', 'PHP', 'JavaScript', 'Ruby', 'Go', 'Swift', 'Kotlin'],
        'student_details' : [
            {'name':'Ripan', 'age': 20, 'city':'Kolkata'},
            {'name':'Rahul', 'age': 21, 'city':'Delhi'}
        ]
    }
    return render(request, "index.html", data)


def aboutUs(request):
    return HttpResponse("You're at the about us page")


def course(request):
    return HttpResponse("You're at the course page.")


def courseDetail(request, courseId):
    return HttpResponse(courseId)

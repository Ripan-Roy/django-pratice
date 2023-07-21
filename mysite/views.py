from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("You're at the about us page")

def course(request):
    return HttpResponse("You're at the course page.")

def courseDetail(request, courseId):
    return HttpResponse(courseId)
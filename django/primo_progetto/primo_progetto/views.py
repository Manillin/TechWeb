from django.http import HttpResponse


def homepage(request):
    response = "Hello\n"
    return HttpResponse(response)

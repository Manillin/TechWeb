from django.http import HttpResponse

# Contiene il codice di backend -> detto "business logic"


def homepage(request):
    response = "Hello\n"
    # print("REQUEST: ", str(request))
    # print(str(dir(request)))

    return HttpResponse(response)


def elenca_params(request):
    response = ""
    for k in request.GET:
        response += request.GET[k] + ""
    return HttpResponse(response)

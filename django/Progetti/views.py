from django.http import HttpResponse

# Contiene il codice di backend -> detto "business logic"


def homepage(request):
    response = "Hello <br>, New Line"
    # print("REQUEST: ", str(request))
    # print(str(dir(request)))

    return HttpResponse(response)


def elenca_params(request):
    response = ""
    for k in request.GET:
        response += request.GET[k] + ""
    return HttpResponse(response)

# Es 1


def pari_dispari(request):
    if 'num' not in request.GET:
        return HttpResponse("Non hai inserito un numero")
    numero = int(request.GET['num'])
    if numero % 2 == 0:
        return HttpResponse(f"Il numero {request.GET['num']} è PARI")
    else:
        return HttpResponse(f"Il numero {request.GET['num']} è DISPARI")

# Es 3


def greet_user(request):
    welcome_msg = '/welcome_'
    stringa = str(request.path)
    response = stringa[len(welcome_msg):-1]
    return HttpResponse("Welcome user -> " + response)

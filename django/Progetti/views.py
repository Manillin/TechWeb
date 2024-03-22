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

# Es 1
# def pari_dispari(request):
#     if 'num' not in request.GET:
#         return HttpResponse("Non hai inserito un numero")
#     numero = int(request.GET['num'])
#     if numero % 2 == 0:
#         return HttpResponse(f"Il numero {request.GET['num']} è PARI")
#     else:
#         return HttpResponse(f"Il numero {request.GET['num']} è DISPARI")

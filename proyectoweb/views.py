from django.http import HttpRequest
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola!")
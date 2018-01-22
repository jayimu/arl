from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world ! ")
def your(request):
    return HttpResponse('your')
def product(request):
    return HttpResponse('product')
def country(request):
    return HttpResponse('country')
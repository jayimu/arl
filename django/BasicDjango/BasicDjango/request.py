from django.http import HttpResponse


def myRequest(request):

    response = 'scheme:' + request.scheme + '<br>'
    response += 'path:' + request.path + '<br>'
    response += 'method:' + request.method + '<br>'
    response += 'HTTP_ACCEPT:' + request.META['HTTP_ACCEPT'] + '<br>'
    response += 'HTTP_USER_AGENT:' + request.META['HTTP_USER_AGENT'] + '<br>'
    response += 'REMOTE_ADDR:' + request.META['REMOTE_ADDR'] + '<br>'
    response += 'QUERY_STRING:' + request.META['QUERY_STRING'] + '<br>'
    response += 'name:' + str(request.GET['name'])+ '<br>'
    response += 'age:' + str(request.GET.get('age')) + '<br>'

    return HttpResponse(response)

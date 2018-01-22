from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def myPost(request):
    user = str(request.POST.get('user'))
    age = str(request.POST.get('age'))
    result = '<h2>name:<font color="red">' + user + '</font></h2>'
    result += '<h2>age:<font color="blue">' + age + '</font></h2>'
    return HttpResponse(result)
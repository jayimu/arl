from django.http import HttpResponse
def index(request):
    user = request.session.get('user')
    result = ''
    if user:
        result = 'user：%s' % user
    else:
        result = 'Not logged in'
    return HttpResponse(result)

def login(request):
    user = request.GET.get('user')
    result = ''
    if user:
        request.session['user'] = user
        result = 'login success'
    else:
        result = 'login failed'

    return HttpResponse(result)


def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
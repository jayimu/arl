from django.shortcuts import render

def myCondition(request):
    values = {}
    values['condition1'] = True
    values['condition2'] = False
    return render(request, 'condition.html', values)
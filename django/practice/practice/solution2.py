from django.shortcuts import render
class MyClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
def solution2(request):
    values = {'values':[MyClass('Bill',20),MyClass('Mike',30),MyClass('John',12)]}
    return render(request, 'for.html', values)
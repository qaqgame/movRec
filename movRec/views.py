from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world!")


def haha(request):
    context = {}
    context['haha'] = 'Hello World!!!!!'
    return render(request, 'helloWorld.html', context)


def dake(request):
    name = request.methodw
    print(name)
    name = request.GET.get("name")
    return HttpResponse('姓名:{}'.format(name))


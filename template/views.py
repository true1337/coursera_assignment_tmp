from django.shortcuts import render
from django.http import HttpResponse

def echo(request):
    return render(request, 'echo.html', context={
        'params':getattr(request, request.method),
        'header':request.META.get('X-Print-Statement')
    })


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })

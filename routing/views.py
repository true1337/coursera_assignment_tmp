from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.views.decorators.http import require_GET, require_POST

def simple_route(request):
    if request.method == 'GET':
        return HttpResponse(content='')
    else:
        return HttpResponseNotAllowed('')

@require_GET
def slug_route(request, slug):
    return HttpResponse(content=slug)

@require_GET
def sum_route(request, number_1, number_2):
    if number_1.isnumeric() and number_2.isnumeric():
        return HttpResponse(content=int(number_1) + int(number_2))
    else:
        return HttpResponseNotFound('')

@require_GET
def sum_get_method(request):
    if ('a' in request.GET
        and 'b' in request.GET
        and request.GET['a'].lstrip('-').isnumeric()
        and request.GET['b'].lstrip('-').isnumeric()):
        res = int(request.GET['a']) + int(request.GET['b'])
        return HttpResponse(content=res)
    else:
        return HttpResponseNotFound('')

@require_POST
def sum_post_method(request):
    if ('a' in request.POST 
        and 'b' in request.POST 
        and request.POST['a'].lstrip('-').isnumeric() 
        and request.POST['b'].lstrip('-').isnumeric()):
        res = int(request.POST['a']) + int(request.POST['b'])
        return HttpResponse(content=res)
    else:
        return HttpResponseNotFound('')

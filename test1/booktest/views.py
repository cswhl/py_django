from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader,RequestContext

def index(request):
    # return HttpResponse("欢迎光临!")
    template = loader.get_template('booktest/index.html')
    context = RequestContext(request,{'title':'图书列表', 'list':range(10)})
    return HttpResponse(template.render(context))

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader,RequestContext
from django.shortcuts import render
from booktest.models import BookInfo

def index(request):
    # return HttpResponse("欢迎光临!")
    #template = loader.get_template('booktest/index.html')
    #context = RequestContext(request,{'title':'图书列表', 'list':range(10)})
    #return HttpResponse(template.render(context))
    return render(request, 'booktest/index.html', {'title':'图书列表', 'list':range(10)})

def detail(request, bid):
#     根据图书id获得图书
    book = BookInfo.object



BookInfo.object
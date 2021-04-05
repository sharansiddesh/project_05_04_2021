from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page1(request):
    return HttpResponse('<h1>wellcome to page1 of app1</h1>')

def page2(request):
    return render(request,"app1.html")



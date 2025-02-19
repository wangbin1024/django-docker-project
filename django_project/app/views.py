from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print("go to index")
    return render(request, "index.html")

def page(request, name):
    print(name)
    print(type(name))
    return HttpResponse(f"<h1>This is the {name} page.</h1>")

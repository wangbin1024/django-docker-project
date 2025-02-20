from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print("go to index")
    return render(request, "index.html")


def page(request, name):
    param = ["a", "b", "c"]
    value = {"age": 20, "job": "student"}
    print(value["age"])
    print(type(int(value["age"])))
    return render(request, "page.html", {"name": name, "value": value, "param": param})

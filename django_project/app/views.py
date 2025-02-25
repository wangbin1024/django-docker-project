from django.shortcuts import render
from django.http import HttpResponse


# member class
class Member:
    age = 0
    name = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age


def index(request):
    print("go to index")
    return render(request, "index.html")


def page(request, name):
    member = Member(name, 20)
    print("go to page")
    return render(request, "page.html", {"member": member})

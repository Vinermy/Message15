from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.

def main_page(request: HttpRequest):
    return render(request, "base.html")

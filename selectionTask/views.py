from django.shortcuts import render
from django.http import HttpResponse
import os


def home(request):
    with open(os.path.join(os.path.dirname(__file__), "../static/index.html"), 'r') as index_html_file:
        return HttpResponse(index_html_file.read(), content_type='text/html')


def assign(request):
    pass


def submit(request):
    pass
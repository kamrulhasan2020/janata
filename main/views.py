import json
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'stock_market_data.json')

with open(file_path, "r") as read_it:
     data = json.load(read_it)


def home(request):
    context = {
        'data': data,
    }
    return render(request,'main/home.html', context, content_type="text/html")

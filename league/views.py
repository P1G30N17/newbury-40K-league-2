from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to the Newbury 40K League</h1>")

def about(request):
    return HttpResponse("<h1>This is a local warhammer 40K league based out of Newbury, Berkshire</h1>")
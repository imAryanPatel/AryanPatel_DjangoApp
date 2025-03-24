from django.shortcuts import render

def home(request):
    return render(request, 'app1/home.html')

def app1_page(request):
    return render(request, 'app1/page.html')

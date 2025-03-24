from django.shortcuts import render

def app2_page(request):
    return render(request, 'app2/page.html')

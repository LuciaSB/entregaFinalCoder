from django.shortcuts import render

def inicio(request):
    return render(request, "App_Components/index.html")

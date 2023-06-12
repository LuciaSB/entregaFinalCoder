from django.shortcuts import render
from App_Components.models import Blog
from App_Components.models import Profile

from App_Components.models import User

def inicio(request):
    return render(request, "App_Components/index.html")

def formulario(request):
      if request.method == 'POST':
      
            usuario =  User(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
 
            usuario.save()
 
            return render(request, "App_Components/index.html")
 
      return render(request,"App_Components/formulario.html")

def profile_form(request):
      if request.method == 'POST':
      
            profile =  Profile(name=request.POST['name'], surname=request.POST['surname'], description=request.POST['description'])
 
            profile.save()
 
            return render(request, "App_Components/index.html")
 
      return render(request,"App_Components/profile_form.html")

def blog_form(request):
      if request.method == 'POST':
      
            blog =  Blog(title=request.POST['title'], content=request.POST['content'])
 
            blog.save()
 
            return render(request, "App_Components/index.html")
 
      return render(request,"App_Components/blog_form.html")

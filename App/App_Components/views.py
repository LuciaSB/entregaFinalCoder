from django.shortcuts import render
from App_Components import models
from App_Components.forms import BlogForm, BuscarUsuarioForm, ProfileForm, UsuarioForm
from App_Components.models import Blog
from App_Components.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordChangeView, LogoutView
from django.shortcuts import get_object_or_404
from .models import Message
from .forms import MessageForm
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, "App_Components/index.html")

def registro_usuario(request):
      if request.method == 'POST':
            form = UsuarioForm(data=request.POST)
            if form.is_valid():
                  form.save()
                  return render(request, "App_Components/index.html",{"miFormulario": UsuarioForm()})
            else:
                 return render(request, "App_Components/formulario.html", {"miFormulario": form})
      form = UsuarioForm()
      return render(request, "App_Components/formulario.html", {"miFormulario": form})


def profile_form(request):
      usuario = request.user
      modelo_perfil, _ = Profile.objects.get_or_create(usuario=usuario)
      if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                  data = form.cleaned_data
                  if data.get('name'):
                     modelo_perfil.name = data.get('name')
                  if data.get('surname'):
                     modelo_perfil.surname = data.get('surname')
                  if data.get('description'):
                     modelo_perfil.description = data.get('description')
                  if data.get('website'):
                     modelo_perfil.website = data.get('website')
                  if data.get('image'):
                     modelo_perfil.image = data.get('image')
                  else:
                     modelo_perfil.image

                  modelo_perfil.save()
                  usuario.save()
                  return render(request, "App_Components/index.html",{"miFormulario": ProfileForm()})
            else:
                 return render(request, "App_Components/profile_form.html", {"miFormulario": form})
      form = ProfileForm(
           initial={
            'name':modelo_perfil.name,
            'surname':modelo_perfil.surname,
            'description':modelo_perfil.description,
            'website':modelo_perfil.website,
        }
      )
      return render(request, "App_Components/profile_form.html", {"miFormulario": form})


def profile_view(request):
    profile = Profile.objects.get(usuario=request.user)
    return render(request, "App_Components/profile_data.html", {"profile": profile})

def blog_form(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.usuario = request.user

            if 'image' in request.FILES:
                blog.image = request.FILES['image']

            blog.save()
            return render(request, "App_Components/index.html", {"miFormulario": BlogForm()})
        else:
            return render(request, "App_Components/blog_form.html", {"miFormulario": form})
    else:
        form = BlogForm()
    return render(request, "App_Components/blog_form.html", {"miFormulario": form})



def buscar_usuario(request):
    if request.method == 'POST':
        busca_usuario = BuscarUsuarioForm(request.POST)

        if busca_usuario.is_valid():
            info = busca_usuario.cleaned_data
            usuarios = User.objects.filter(username=info["username"])
            return render (request, "App_Components/user_list.html", {"usuarios": usuarios})
    else:
        busca_usuario = BuscarUsuarioForm()
        return render(request, "App_Components/search_user.html", {"miFormulario": busca_usuario})
    
    
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                django_login(request, user)
                return redirect('Inicio')
            else:
                return render(request, "App_Components/iniciar_sesion.html", {"mensaje":"Datos incorrectos"})

    form = AuthenticationForm()
    return render(request, 'App_Components/iniciar_sesion.html', {'formulario':form})

def blog_list(request):
        forms = Blog.objects.all()
        return render(request, 'App_Components/blog_list.html', {'forms': forms})


def blog_delete(request, form_id):
    form = get_object_or_404(Blog, id=form_id)
    form.delete()
    return render(request, "App_Components/index.html")

def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('title'):
                blog.title = data.get('title')
            if data.get('content'):
                blog.content = data.get('content')
            if data.get('image'):
                blog.image = data.get('image')
            
            blog.save()
            return render(request, "App_Components/index.html")
        else:
            return render(request, "App_Components/blog_form.html", {"miFormulario": form})
    form = BlogForm(
           initial={
            'title':blog.title,
            'content':blog.content,
            'image':blog.image,
        }
      )
    return render(request, "App_Components/blog_form.html", {'miFormulario': form})

def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    
    return render(request, "App_Components/view_blog.html", {'blog': blog})

class Logout(LogoutView):
    template_name = 'App_Components/logout_account.html'

@login_required
def messages(request):
    user = request.user
    received_messages = Message.objects.filter(recipient=user)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = user
            message.recipient = User.objects.get(username=form.cleaned_data['recipient'])
            message.save()
            return redirect('messages')
    else:
        form = MessageForm()
    
    return render(request, 'App_Components/messages.html', {'messages': received_messages, 'form': form})
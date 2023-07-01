"""
URL configuration for Clases_Coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from App_Components import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('signup/', views.registro_usuario, name="Formulario"), #agrega usuario a la base de datos
    path('profile_form/', views.profile_form, name="Profile_Form"), #agrega un perfil a la base de datos
    path('blog_form/', views.blog_form, name="Blog_Form"), #agrega un blog a la base de datos
    path('buscar_usuario/', views.buscar_usuario, name="Search_User"), #busca un usuario previamente cargado en la base de datos
    path('login/', views.login_request, name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('profile/', views.profile_view, name='my_profile'),
    path('blog_list', views.blog_list, name='blog_list'),
    path('blog_delete/<int:form_id>/', views.blog_delete, name='blog_delete'),
    path('edit-blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('view_blog/<int:blog_id>/', views.view_blog, name='view_blog'),
    path('messages/', views.messages, name='messages'),
]
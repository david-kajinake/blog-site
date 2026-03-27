"""
URL configuration for blog_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the i sncl ude ()  fun cti on:  fr om  dja ngo .ur ls  imp ort  in clu de,  pa th
      2.  Ad d a  UR L t o u rlp att ern s:   pa th( 'bl og/ ',  inc lud e(' blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
    path("greet/" , include("greet.urls")),
    path("tasks/" , include("tasks.urls")),
]

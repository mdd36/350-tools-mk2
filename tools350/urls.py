"""tools350 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import tools350.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('assembler/', views.assembler, name='assembler'),
    path('im2mif/', views.wip, name='im2mif'),
    path('feedback/', views.bugs_features, name='feedback'),
    path('about/', views.wip, name='about'),
    path('assemble/', views.assemble, name='assemble'),
    path('help/', views.help, name='help'),
    path('mifify/', views.mifify, name='mifify'),
    path('testim2mif/', views.im2mif, name='im2mif-test')
]

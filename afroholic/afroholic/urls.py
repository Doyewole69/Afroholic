"""
URL configuration for afroholic project.

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
from django.contrib import admin
from django.urls import path
from afroholichome import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.subscribe, name='subscribe'),
    path('success/', views.success, name='success'),
    path('artistes/', views.artistes, name='artistes'),
    path('artistes/olusegun', views.olusegun, name='olusegun-music'),
    path('artistes/vennessa', views.vennessa, name='vennessa-music'),
    path('artistes/leo9ice', views.leo9ice, name='leo9ice-music'),
    path('artistes/lin', views.lin, name='lin-music'),
    path('artistes/skeffi', views.skeffi, name='skeffi-music'),
]
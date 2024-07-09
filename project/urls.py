"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

handler400 = ""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('program1.urls')),
    path('', include('program2.urls')),
    path('', include('program3.urls')),
    path('', include('program4.urls')),
    path('', include('program5.urls')),
    path('p6/', include('program6.urls')),
    path('', include('scratch.urls')),
    path('',include('scratch4.urls')),
    path('p7/', include('program7.urls')),
    path('p8/', include('program8.urls'))
]

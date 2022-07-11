"""Mingstargram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from content.views import Main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.as_view()),  # sub 클래스를 뷰로 사용
    path('content/', include('content.urls')),  # upload 불러때
    path('user/', include('user.urls'))  # upload 불러때
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
URL configuration for PlayStore project.

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
from task1.views import sign_up_by_html, sign_up_by_django,main_page,  game_store_page, cart_page, news_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('games/', game_store_page),
    path('cart/', cart_page),
    path('platform/news/', news_page),
    path('html_sign_up/', sign_up_by_html),
    path('django_sign_up/', sign_up_by_django)
]

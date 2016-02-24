"""jcole_fanpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from jcole_app.views import index_views, aboutme_views, concerts_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_views, name='index'),
    url(r'^aboutme/', aboutme_views, name='aboutme'),
    url(r'^concerts/', concerts_views, name='concerts')
]

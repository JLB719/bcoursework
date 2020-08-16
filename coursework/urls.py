"""coursework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from cvbuilder import views as cvviews
from blog import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('cv/', cvviews.home_page, name='home'),
    url('', views.post_list, name='post_list'),
    url('post/<int:pk>/', views.post_detail, name='post_detail'),
    url('post/new/', views.post_new, name='post_new'),
    url('post/<int:pk>/edit/', views.post_edit, name='post_edit')

]

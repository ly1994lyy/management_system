"""ClassMange URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from students import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('edit/<int:stu_pk>', views.edit_stu, name='edit_stu'),
    path('students/', views.student_list, name='student_list'),
    path('delete/<int:stu_pk>', views.stu_del, name='stu_del'),
    path('add_stu', views.add_stu, name='add_stu'),
    path('score/', views.score_list, name='score_list'),
]

"""Intership_Rec_Sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from Student.views import *
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Student/',include('Student.urls')),
    path('Bole/',include('Bole.urls')),
    path('',views.home,name='home'),
    #用于登陆处理
    path('index/',include('Student.urls')),
    #跳转到学生注册
    path(r'stu_register/',views.stu_reg),
    #登陆页的跳转
    path('main_page/',views.main_page),
    #登陆页跳转到伯乐注册
    path(r'bole_register/',views.bole_reg),
    #跳转到学生注册
    path('jump_stu_reg/',views.jump_stu_reg),
    # 跳转到伯乐注册
    path('jump_bole_reg/',views.jump_stu_reg),
    #跳转到登录
    path('stu_register/jump_login/',views.jump_login),
    #跳转到登录
    path('login_page/',views.login_page),
    #加载电话号码
    path('personal_account/',views.load_phone),
    #跳转到个人主页
    path('stu_personal_page/',views.stu_personal_page),
    #详情页面
    path('job_detail/<JobName>/',views.job_detail_page),
    # path('job_detail/',views.job_detail_page),
    #推荐系统信息填写表单
    path('recommend_data_form/',views.recommend_data_form),
    #推荐系统页面
    path('recommend_page/',views.recommend_page),
]+ static("/",document_root = "./templates")
urlpatterns += staticfiles_urlpatterns()
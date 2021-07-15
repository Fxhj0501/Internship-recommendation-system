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
    path('main_page.html/',views.main_page),
    #登陆页跳转到伯乐注册
    path(r'bole_register/',views.bole_reg),
    #跳转到学生注册
    path('jump_stu_reg/',views.jump_stu_reg),
    # 跳转到伯乐注册
    path('jump_bole_reg/',views.jump_stu_reg),
    #加载伯乐主页--csq
    path('bole_main_page/',views.bole_main_page),
    #加载内推码提交页--csq
    path('postCode/',views.postCode),
    #加载我的岗位--csq
    path('myJob/',views.myJob),
    #加载伯乐个人主页
    path('bole_personal_page/',views.bole_personal_page),
    #加载添加岗位信息--csq
    path('addJob/',views.addJob),
    #加载岗位信息搜索--csq
    path('search/',views.search),
    #重载岗位信息搜索--csq
    path('reload_search/',views.reload_search),

    #伯乐主页跳转到内推码提交页
    path('bole_main_page/jump_main/',views.jump_postCode),
    #伯乐主页跳转到我的岗位
    path('bole_main_page/jump_myJob/',views.jump_myJob),
    #伯乐主页跳转到个人主页
    path('bole_main_page/jump_bole_personal/',views.jump_bole_personal),

    #提交内推码跳转到伯乐主页
    path('postCode/jump_bole_main/',views.jump_bole_main),
    #提交内推码跳转到我的岗位
    path('postCode/jump_myJob/',views.jump_myJob),

    #我的岗位跳转到伯乐主页
    path('myJob/jump_bole_main/',views.jump_bole_main),
    #我的岗位跳转到发布内推码
    path('myJob/jump_main/',views.jump_postCode),

    #提交内推码
    path('postCode/submit_code/',views.submit_code),

    #详情页面
    path('job_detail/<JobName>/',views.job_detail_page),
    #修改岗位信息
    path('revise_job/<JobName>/',views.revise_job),
    #提交修改岗位信息
    path('revise_job/<JobName>/change_job_info/',views.change_job_info),
    #删除岗位信息
    path('myJob/delete_job/',views.jump_delete_job),
    #提交添加岗位信息
    path('addJob/add_job_info/',views.add_job_info),

    #提交搜索信息
    path('search/submit_search/',views.submit_search),
]+ static("/",document_root = "./templates")
urlpatterns += staticfiles_urlpatterns()
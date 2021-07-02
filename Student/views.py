from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

# 跳转
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import reverse
# from common.models import student_info
# # 查询登陆是否在学生的数据库记录信息内
# def check_stu_info(request):
#     qs = student_info.objects.values()
#     retStr = ''
#     for each_stu in qs:
#         for name,password in each_stu.items():
#             retStr
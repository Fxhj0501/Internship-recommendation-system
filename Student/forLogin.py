from django.http import JsonResponse
import json
from common.models import student_info
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

# 登录处理
def check_info( request):
    # 从 HTTP GET 请求中获取用户名、密码参数
    if request.method == "POST":
        phone = request.POST.get("phone")
        pwd = request.POST.get("pwd")
        response = {"msg":None}
       #user = authenticate(request,username=username,password = pwd)
        # user = student_info.objects.get(username=username)
        # if user.password == pwd:
        #     login(request, user)  # request.user== 当前登录对象
        #     response["usr"] = "duij"
        #     return JsonResponse(response)
        # else:
        #     response["msg"] = '账号错了'
        #     return JsonResponse(response)
        try:
            phone = student_info.objects.get(phone_num=phone)
        except:
            response['msg'] = '用户名或密码错误'
            return JsonResponse(response)
        if phone.password == pwd:
            response['msg'] = '成功登陆'
            return JsonResponse(response)


# 登出处理
def signout( request):
    # 使用登出方法
    logout(request)
    return JsonResponse({'ret': 0})



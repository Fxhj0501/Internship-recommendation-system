from django.http import JsonResponse
import json
from common.models import student_info
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout

# 登录处理
def check_info( request):
    # 从 HTTP GET 请求中获取用户名、密码参数
    username = request.POST.get('username')
    password = request.POST.get('pwd')
    sertype = request.POST.get('sertype')
    response = {"usr":None,"msg":None}
    valid_code = request.POST.get("vali")
    user = authenticate(username=username,password = password)
    if sertype == '学生':
        if user:
            login(request,user)
            response["usr"] = user.username
        else:
            response['msg'] = "username or password error!"
    else :
        if user:
            login(request,user)
            response["usr"] = user.username
        else:
            response['msg'] = "username or password error!"

    return JsonResponse(response)



# 登出处理
def signout( request):
    # 使用登出方法
    logout(request)
    return JsonResponse({'ret': 0})
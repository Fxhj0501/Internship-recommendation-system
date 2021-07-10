from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
from django.template import Context


def home(request):
    print("login")
    return render(request,'login.html', {"name":"cwc"})

def Login_view(request):
    u = request.GET.get('username','')
    p = request.GET.get('password','')
    type = request.GET.get('sertype','')
    if u and p and type:
        if(type == "学生"):
            return render(request,'bole_register.html')
        else:
            return
    else:
        return render(request,'login.html')

def main_page(request):
    print("hit")
    test1 = { "name":"giao岗", "salary" : "1个亿"}
    test2 = {"name": "蚌埠住了", "salary": "2个亿"}
    list = [test1,test2]
    return render(request,'main_page.html', {"items": list, "pho_num":"111111"})

def bole_reg(request):
    return render(request,'bole_register.html')

def stu_reg(request):
    return render(request,'stu_register.html')

def jump_stu_reg(request):
    response = {'msg':None}
    response['msg'] = 'jump'
    return JsonResponse(response)

def jump_bole_reg(request):
    response = {'msg':None}
    response['msg'] = 'jump'
    return JsonResponse(response)

def jump_login(request):
    response = {'msg':None}
    response['msg'] = 'jump'
    return JsonResponse(response)

def login_page(request):
    return render(request,'login.html')

def load_phone(request):
    response = {'msg': None}
    response['msg'] = '13810874508'
    return JsonResponse(response)
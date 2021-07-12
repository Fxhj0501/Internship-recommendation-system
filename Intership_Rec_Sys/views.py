from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
from django.template import Context
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage



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
    #print("hit")

    test1 = { "name":"giao岗", "salary" : "1个亿","pic" : "C++.jpg"}
    test2 = {"name": "蚌埠住了", "salary": "2个亿","pic" : "product_manager.jpg"}
    test3 = {"name": "giao岗", "salary": "1个亿", "pic": "C++.jpg"}
    test4 = {"name": "蚌埠住了", "salary": "2个亿", "pic": "product_manager.jpg"}
    test5 = {"name": "giao岗", "salary": "1个亿", "pic": "C++.jpg"}
    test6 = {"name": "蚌埠住了", "salary": "2个亿", "pic": "product_manager.jpg"}
    test7 = {"name": "giao岗", "salary": "1个亿", "pic": "C++.jpg"}
    test8 = {"name": "蚌埠住了", "salary": "2个亿", "pic": "product_manager.jpg"}
    test9 = {"name": "giao岗", "salary": "1个亿", "pic": "C++.jpg"}
    test10 = {"name": "蚌埠住了", "salary": "2个亿", "pic": "product_manager.jpg"}
    test11 = {"name": "giao岗", "salary": "1个亿", "pic": "C++.jpg"}
    test12 = {"name": "蚌埠住了", "salary": "2个亿", "pic": "product_manager.jpg"}
    test13 = {"name": "giao岗", "salary": "1个亿", "pic": "C++.jpg"}
    test14 = {"name": "蚌埠住了", "salary": "2个亿", "pic": "product_manager.jpg"}

    list = [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10,test11,test12,test13,test14,]
    #test=[1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
    paginator = Paginator(list, 12)

    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            l = paginator.page(page)
        # todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            l = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            l = paginator.page(paginator.num_pages)

    return render(request,'main_page.html', {"items": l, "pho_num":"111111"})

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
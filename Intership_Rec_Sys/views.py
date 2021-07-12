from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
def home(request):
    return render(request,'login.html')

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
    return render(request,'main_page.html')

def bole_main_page(request):
    print("hit")
    test1 = { "name":"giao岗", "salary" : "1个亿"}
    test2 = {"name": "蚌埠住了", "salary": "2个亿"}
    test3 = { "name":"giao岗", "salary" : "1个亿"}
    test4 = {"name": "蚌埠住了", "salary": "2个亿"}
    test5 = {"name": "蚌埠住了", "salary": "2个亿"}
    list = [test1,test2,test3,test4,test5]
    return render(request,'bole_main_page.html', {"items": list, "pho_num":"123456"})

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

def jump_bole_main(request):
    response = {'msg':None}
    response['msg'] = 'jump'
    return JsonResponse(response)    

def jump_postCode(request):
    response = {'msg':None}
    response['msg'] = 'jump'
    return JsonResponse(response)

def jump_myJob(request):
    response = {'msg':None}
    response['msg'] = 'jump'
    return JsonResponse(response)  

def postCode(request):
    print("heat")
    return render(request,'postCode.html',{"pho_num":"1234567"})

def myJob(request):
    print("this is myjob")
    return render(request,'myJob.html',{"pho_num":"12345678"}) 

def submit_code(request):
    code=request.POST.get("code")
    response = {'msg':None}
    response['msg'] = code
    return JsonResponse(response) 


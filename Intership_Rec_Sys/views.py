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

    test1 = { "JobName":"字节跳动 C++岗", "Salary" : "100","Company" : "C++"}
    test2 = {"JobName": "字节跳动 产品经理", "Salary": "200","Company" : "product_manager"}
    test3 = {"JobName": "字节跳动 C++岗", "Salary": "100", "Company": "C++"}
    test4 = {"JobName": "字节跳动 产品经理", "Salary": "200", "Company": "product_manager"}
    test5 = {"JobName": "字节跳动 C++岗", "Salary": "100", "Company": "C++"}
    test6 = {"JobName": "字节跳动 产品经理", "Salary": "200", "Company": "product_manager"}
    test7 = {"JobName": "字节跳动 C++岗", "Salary": "100", "Company": "C++"}
    test8 = {"JobName": "字节跳动 产品经理", "Salary": "200", "Company": "product_manager"}
    test9 = {"JobName": "字节跳动 C++岗", "Salary": "100", "Company": "C++"}
    test10 = {"JobName": "字节跳动 产品经理", "Salary": "200", "Company": "product_manager"}
    test11 = {"JobName": "字节跳动 C++岗", "Salary": "100", "Company": "C++"}
    test12 = {"JobName": "字节跳动 产品经理", "Salary": "200", "Company": "product_manager"}
    test13 = {"JobName": "字节跳动 C++岗", "Salary": "100", "Company": "C++"}
    test14 = {"JobName": "字节跳动 产品经理", "Salary": "200", "Company": "product_manager"}
    test = "f\nf"

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

    return render(request,'main_page.html', {"items": l, "pho_num":"13810874508", "test":test})

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

def stu_personal_page(request):
    student = {"PhoneNum":"13810874508","Password":"123456","SchoolInfo":"北京工业大学","Skills":"C++,Python","InternshipJob":"爸爸"}
    return render(request,'stu_personal_page.html',{"item":student})

def job_detail_page(request,JobName):
    job = {"id":"1","JobName":"阿里云JAVA后台实习","JobInfo":"第一行\n第二行\n第三行","Company":"C++","Skills":"111\n222\n333\n444\n555\n666",
           "ContactInfo":"13810874508","Adress":"北京.朝阳区.望京","Salary":"400","RecCode":"12345"}
    print(JobName)


    return render(request,'job_detail.html',{"item":job})

def recommend_data_form(request):
    student = {"skills":"C++,JAVA"}
    return render(request,'recommend_data_form.html',{"item":student})

def recommend_page(request):
    job1 = {"jobName": "阿里云JAVA后台实习", "jobInfo": "第一行\n第二行\n第三行", "company": "JAVA",
           "skills": "111\n222\n333\n444\n555\n666",
           "contactInfo": "13810874508", "adress": "北京.朝阳区.望京", "salary": "400", "recCode": "12345"}
    job2 = {"jobName": "阿里云C++后台实习", "jobInfo": "第一行\n第二行\n第三行", "company": "C++",
           "skills": "111\n222\n333\n444\n555\n666",
           "contactInfo": "13810874508", "adress": "北京.朝阳区.望京", "salary": "500", "recCode": "12345"}
    job3 = {"jobName": "阿里云python后台实习", "jobInfo": "第一行\n第二行\n第三行", "company": "Python",
           "skills": "111\n222\n333\n444\n555\n666",
           "contactInfo": "13810874508", "adress": "北京.朝阳区.望京", "salary": "600", "recCode": "12345"}
    list = [job1,job2,job3]
    return render(request,'recommend_page.html',{"items":list})

def stu_search_page(request):
    return render(request,'stu_search_page.html',{"pho_num":"111111"})


def submit_search(request):
    search_info=request.POST.get("search_info")
    response = {'msg':None}
    response['msg'] = "提交成功"
    return JsonResponse(response)

def reload_search(request):

    test1 = { "JobName":"字节跳动 C++岗", "Salary" : "100","Company" : "C++"}
    test2 = {"JobName": "字节跳动 产品经理", "Salary": "200","Company" : "product_manager"}
    test3 = {"JobName": "字节跳动 C++岗", "Salary": "100", "Company": "C++"}


    test = "f\nf"

    list = [test1,test2,test3,]
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

    return render(request,'stu_search_page.html', {"items": l, "pho_num":"111111", "test":test})
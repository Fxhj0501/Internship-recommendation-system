from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from common.models import Job_info
from django.forms.models import model_to_dict
from common.models import student_info
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
    all_jobs  = Job_info.objects.values()
    # job_list = []
    # for item in all_jobs:
    #     item = model_to_dict(item)
    #     job_list.append(item)
    job_list = list(all_jobs)
    paginator = Paginator(job_list, 12)
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
    phone = request.session.get('phone',default = '123123')
    return render(request,'main_page.html', {"items":l, "pho_num":phone})
    # response = {'msg':None}
    # response['msg'] = job_list[0]
    # return JsonResponse(response)

def bole_reg(request):
    all_jobs  = Job_info.objects.values()
    # job_list = []
    # for item in all_jobs:
    #     #item = model_to_dict(item)
    #     job_list.append(item)
    job_list = list(all_jobs)
    response = {'msg':None}
    response['msg'] = job_list[0]
    return JsonResponse(response)

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
    phone = request.session.get('phone',default = '123123')
    response['msg'] = '13810874508'
    return JsonResponse(response)
def job_detail_page(request,JobName):
    job = {"id":"1","JobName":"阿里云JAVA后台实习","JobInfo":"第一行\n第二行\n第三行","Company":"C++","Skills":"111\n222\n333\n444\n555\n666",
           "ContactInfo":"13810874508","Adress":"北京.朝阳区.望京","Salary":"400","RecCode":"12345"}
    print(JobName)
    return render(request,'job_detail.html',{"item":job})

def stu_personal_page(request):
    stu_info = student_info.objects.values()
    phone = request.session.get('phone')
    phone = str(phone)
    try:
        student = stu_info.filter(phoneNum = phone)
        student = list(student)
        student = student[0]
    except:
        student = {"phoneNum":None,"password":None,"schoolInfo":None,"skills":None,"internshipJob":None}
    return render(request,'stu_personal_page.html',{"item":student})

def stu_fix_info(request):
    skills = request.POST.get('Skills')
    job = request.POST.get("InternshipJob")
    school = request.POST.get("SchoolInfo")
    phone = request.session.get('phone')
    phone = str(phone)
    response  = {'msg':None}
    try:
        stu = student_info.objects.get(phoneNum = phone)
    except:
        response['msg'] = "该用户不存在"
        return JsonResponse(response)
    if skills != None:
        stu.skills = skills
    if job != None:
        stu.internshipJob = job
    if school != None:
        stu.schoolInfo = school
    stu.save()
    response['msg'] ="修改信息成功"
    return JsonResponse(response)

def stu_reset_pwd(request):
    oldpwd = request.POST.get('Password')
    newpwd = request.POST.get("NewPassord")
    confirmpwd = request.POST.get("ConfirmPassword")
    phone = request.session.get('phone')
    phone = str(phone)
    response  = {'msg':None}
    try:
        stu = student_info.objects.get(phoneNum = phone)
    except:
        response['msg'] = "该用户不存在"
        return JsonResponse(response)
    if stu.password != oldpwd:
        response['msg'] = "密码错误"
        return JsonResponse(response)
    elif newpwd != confirmpwd:
        response['msg'] = "两次密码输入不一致"
        return JsonResponse(response)
    elif newpwd == "" or confirmpwd == "":
        response['msg'] = "密码不能为空"
        return JsonResponse(response)
    else:
        stu.password = newpwd
    stu.save()
    response['msg'] ="修改密码成功"
    return JsonResponse(response)


from django.shortcuts import render
import json
from django.http import JsonResponse,HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from common.models import Job_info
from django.forms.models import model_to_dict
from common.models import student_info
from common.models import bole as Bole
import numpy as np
import xlrd
from django.shortcuts import redirect
def home(request):
    request.session['phone'] = None
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
    print(request.session.get('phone'))
    if request.session.get('phone') == None:
        return redirect('/')
    else :
        all_jobs  = Job_info.objects.values()
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
    phone = request.session.get('phone',default = '123123')
    response['msg'] = '13810874508'
    return JsonResponse(response)
def job_detail_page(request,JobName):
    JobName = str(JobName)
    print(JobName)
    job_list = Job_info.objects.values()
    try:
        job = job_list.filter(jobName = JobName)
        job = list(job)
        job = job[0]
        print(job)
    except:
        return render(request,'main_page.html')
    jobinfo = job['jobInfo']
    jobinfo = jobinfo.split("；")
    jobinfo[0] = jobinfo[0] +'\n'
    for i in range(1,len(jobinfo)):
        jobinfo[i] = jobinfo[i] + '\n'
        jobinfo[0] = jobinfo[0] + jobinfo[i]
    job['jobInfo'] = jobinfo[0]
    jobreq = job['skills']
    jobreq = jobreq.split('；')
    jobreq[0] = jobreq[0] + '\n'
    for i in range(1,len(jobreq)):
        jobreq[i] = jobreq[i]+'\n'
        jobreq[0] = jobreq[0]+jobreq[i]
    job['skills'] = jobreq[0]
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
    response  = {'msg':'aaaa'}
    try:
        print(phone)
        stu = student_info.objects.get(phoneNum = phone)
        if skills != None:
            stu.skills = skills
        if job != None:
            stu.internshipJob = job
        if school != None:
            stu.schoolInfo = school
        stu.save()
        response['msg'] ="修改信息成功"
        return JsonResponse(response)
    except:
        response['msg'] = "该用户不存在"
        print('aaaa')
        return JsonResponse(response)
    # if skills != None:
    #     stu.skills = skills
    # if job != None:
    #     stu.internshipJob = job
    # if school != None:
    #     stu.schoolInfo = school
    # stu.save()

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

def recommend_data_form(request):
    skills = request.POST.get('skills')
    adress = request.POST.get('adress')
    citys = ["东城区","西城区","朝阳区","丰台区","石景山区","海淀区","顺义区","通州区","大兴区","房山区","门头沟区","昌平区","平谷区","密云区","怀柔区","延庆区"]
    adress = str(adress)
    for i in range(0,len(citys)):
        if adress == citys[i]:
            adress = i+1
            break
    excelFile = "/Users/fengzijian/PycharmProjects/Intership_Rec_Sys/static/data.xls"
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    score = []
    salary = request.POST.get('salary')
    salary = float(salary)/100
    skill1,skill2,skill3 = skills.split(',')
    skill1 = skill1.lower()
    skill2 = skill2.lower()
    skill3 = skill3.lower()
    period = request.POST.get("period")
    period = int(period)
    person = [salary,3,period,adress]
    j = 0
    for rowNum in range(table.nrows):
        temp = []
        rowVale = table.row_values(rowNum)
        sk_num = 0
        for i in range(3,6):
            if skill1 == rowVale[i].lower():
                sk_num += 1
                break
        for i in range(3,6):
            if skill2 == rowVale[i].lower():
                sk_num += 1
                break
        for i in range(3,6):
            if skill3 == rowVale[i].lower():
                sk_num += 1
                break
        person[1] = sk_num
        vector_a = np.mat(person)
        temp.append(rowVale[2]/100)
        temp.append(sk_num)
        temp.append(rowVale[6])
        temp.append(rowVale[7])
        vector_b = np.mat(temp)
        num = float(vector_a * vector_b.T)
        denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
        cos = num / denom
        sim = 0.5 + 0.5 * cos
        score.append({'id':j,'score':sim})
        j += 1
    score.sort(key=lambda x:(x['score']),reverse=True)
    N = 3
    for i in range(0,N):
        print(table.row_values((score[i]['id']))[0]+table.row_values((score[i]['id']))[1])
        request.session[i] = table.row_values((score[i]['id']))[0]+table.row_values((score[i]['id']))[1]
    response = {'msg':'推荐成功'}
    return JsonResponse(response)

def recommend_page(request):
    job1 = request.session.get('0')
    job2 = request.session.get('1')
    job3 = request.session.get('2')
    job1 = str(job1)
    job2 = str(job2)
    job3 = str(job3)
    print(job1)
    print(job2)
    print(job3)
    try:
        job = Job_info.objects.get(jobName = job1)
        job1 = model_to_dict(job)
    except:
        return render(request,'recommend_data_form.html')
    try:
        job = Job_info.objects.get(jobName = job2)
        job2 = model_to_dict(job)
    except:
        return render(request,'recommend_data_form.html')
    try:
        job = Job_info.objects.get(jobName = job3)
        job3 = model_to_dict(job)
    except:
        return render(request,'recommend_data_form.html')
    # except:
    #     return render(request,'main_page.html')
    list = [job1,job2,job3]
    return render(request,'recommend_page.html',{"items":list})

def load_rec_form(request):
    phone = str(request.session.get('phone'))
    stu = student_info.objects.get(phoneNum = phone)
    print(stu.skills)
    return render(request,'recommend_data_form.html',{"item":stu})

def bole_main_page(request):
    all_jobs  = Job_info.objects.values()
    job_list = list(all_jobs)
    paginator = Paginator(job_list, 12)
    print('aaaaa')
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
    return render(request,'bole_main_page.html', {"items":l, "pho_num":phone})

def bole_personal_page(request):
    bole_info = Bole.objects.values()
    phone = request.session.get('phone')
    phone = str(phone)
    try:
        bole = bole_info.filter(phoneNum = phone)
        bole = list(bole)
        bole = bole[0]
        print(bole)
    except:
       bole = {"phoneNum":None,"password":None,"jobName":None,"recCode":None}
    return render(request,'bole_personal_page.html',{"item":bole})

def bole_fix_info(request):
    recCode = request.POST.get('recCode')
    job = request.POST.get("jobName")
    job = str(job)
    phone = request.session.get('phone')
    phone = str(phone)
    response  = {'msg':None}
    print(job)
    try:
        bole = Bole.objects.get(phoneNum = phone)
    except:
        response['msg'] = "该用户不存在"
        return JsonResponse(response)
    if job != None:
        bole.jobName = job
    if recCode != None:
        bole.recCode = recCode
    bole.save()
    #同时还要改岗位信息的内推码
    try:
        jobinfo = Job_info.objects.get(jobName = job)
    except:
        response['msg'] = "公司不存在"
        return JsonResponse(response)
    jobinfo.recCode = recCode
    jobinfo.save()
    response['msg'] ="修改信息成功"
    return JsonResponse(response)

def bole_reset_pwd(request):
    oldpwd = request.POST.get('Password')
    newpwd = request.POST.get("NewPassord")
    confirmpwd = request.POST.get("ConfirmPassword")
    phone = request.session.get('phone')
    phone = str(phone)
    response  = {'msg':None}
    try:
        bole = Bole.objects.get(phoneNum = phone)
    except:
        response['msg'] = "该用户不存在"
        return JsonResponse(response)
    if bole.password != oldpwd:
        response['msg'] = "密码错误"
        return JsonResponse(response)
    elif newpwd != confirmpwd:
        response['msg'] = "两次密码输入不一致"
        return JsonResponse(response)
    elif newpwd == "" or confirmpwd == "":
        response['msg'] = "密码不能为空"
        return JsonResponse(response)
    else:
        bole.password = newpwd
    bole.save()
    response['msg'] ="修改密码成功"
    return JsonResponse(response)

def postCode(request):
    phone = str(request.session.get('phone'))
    recCode = request.POST.get('code')
    response = {'msg':None}
    try:
        bole = Bole.objects.get(phoneNum = phone)
        temp = str(bole.jobName)
        job = Job_info.objects.get(jobName = temp)
    except:
        response['msg'] = "该用户不存在"
        return JsonResponse(response)
    job.recCode = recCode
    return render(request,'postCode.html',{"pho_num":phone})

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

def jump_bole_personal(request):
    response = {'msg':None}
    response['msg'] = 'jump'
    return JsonResponse(response)

def postCode(request):
    phone = str(request.session.get('phone'))
    return render(request,'postCode.html',{"pho_num":phone})

def myJob(request):
    phone = str(request.session.get('phone'))
    bole = Bole.objects.get(phoneNum = phone)
    jobinfo = str(bole.jobName)
    response = {'msg':None}
    try:
        job = Job_info.objects.get(jobName = jobinfo)
    except:
        response['msg'] = 'Contact us your job info'
        return JsonResponse(response)
    print(job.jobName)
    job = [job]
    return render(request,'myJob.html', {"items": job, "pho_num":phone})

def submit_code(request):
    code=request.POST.get("code")
    phone = str(request.session.get('phone'))
    bole = Bole.objects.get(phoneNum = phone)
    jobinfo = str(bole.jobName)
    job = Job_info.objects.get(jobName = jobinfo)
    job.recCode = code
    job.save()
    response = {'msg':None}
    response['msg'] = '提交成功'
    return JsonResponse(response)

# def bole_personal_page(request):
#     phone = str(request.session.get('phone'))
#     bole = Bole.objects.get('phoneNum = phone')
#     return render(request,'bole_personal_page.html',{"item":bole,"PhoneNum":phone})


def revise_job(request,JobName):
    phone = str(request.session.get('phone'))
    bole = Bole.objects.get(phoneNum = phone)
    jobinfo = str(bole.jobName)
    job = Job_info.objects.get(jobName = jobinfo)

    return render(request,'revise_job.html',{"item":job})

def change_job_info(request,JobName):
    JobName = str(JobName)
    name=request.POST.get("JobName")
    Company=request.POST.get("Company")
    Address=request.POST.get("Address")
    Salary=request.POST.get("Salary")
    JobInfo=request.POST.get("JobInfo")
    Skills=request.POST.get("Skills")
    RecCode=request.POST.get("RecCode")
    print(RecCode)
    print(JobName)
    contact = request.POST.get("contact")
    job = Job_info.objects.get(jobName = JobName)
    job.jobName = name
    job.company = Company
    job.jobInfo = JobInfo
    job.skills = Skills
    job.contactInfo = contact
    job.adress = Address
    job.salary = Salary
    job.recCode = RecCode
    job.save()
    response = {'msg':None}
    response['msg'] = "修改成功"
    return JsonResponse(response)

def delete_job(request):

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

    return render(request,'myJob.html', {"items": l, "pho_num":"111111", "test":test})

def jump_delete_job(request):
    name=request.POST.get("JobName")
    response = {'msg':None}
    response['msg'] = name
    return JsonResponse(response)

def addJob(request):
    jobName = request.POST.get('JobName')
    jobName = request.POST.get('Company')
    jobName = request.POST.get('Address')
    jobName = request.POST.get('JobName')
    jobName = request.POST.get('JobName')
    jobName = request.POST.get('JobName')
    jobName = request.POST.get('JobName')
    return render(request,'addJob.html')

def add_job_info(request):
    name=str(request.POST.get("JobName"))
    Company=str(request.POST.get("Company"))
    Address=str(request.POST.get("Address"))
    Salary=str(request.POST.get("Salary"))
    JobInfo=str(request.POST.get("JobInfo"))
    Skills=str(request.POST.get("Skills"))
    RecCode=str(request.POST.get("RecCode"))
    Contact = str(request.POST.get("Contact"))
    record = Job_info.objects.create(jobName = name,
                                    jobInfo = JobInfo,
                                    company = Company,
                                    skills = Skills,
                                    contactInfo = Contact,
                                    adress = Address,
                                    salary = Salary,
                                    recCode = RecCode)
    response = {'msg':None}
    response['msg'] = "修改成功"
    return JsonResponse(response)

def search(request):
    phone = str(request.session.get('phone'))
    return render(request,'search.html',{"pho_num":phone})

def stu_search(request):
    if request.method == "GET":
        phone = str(request.session.get('phone'))
        return render(request,'stu_search_page.html',{"pho_num":phone})
    if request.method == "POST":
        phone = str(request.session.get('phone'))
        search_info = request.GET.get("search_info")
        # search_info = str(request.session.get('search_info'))
        job = Job_info.objects.get(jobName = search_info)
        job = model_to_dict(job)
        job = [job]
        phone = str(request.session.get('phone'))
        return render(request,'search.html', {"items": job, "pho_num":phone})


def submit_search(request):

    search_info=request.POST.get("search_info")
    response = {'msg':None}
    print(search_info)
    try:
        job = Job_info.objects.get(jobName = search_info)
        print(job.jobName)
        request.session['search_info'] = job.jobName
        request.session['search_company'] = 0
    except:
        response['msg'] = '您找的岗位不存在，请重新查找'
        return JsonResponse(response)

    response['msg'] = "提交成功"
    return JsonResponse(response)

def stu_submit_search(request):
    search_info=request.POST.get("search_info")
    response = {'msg':None}
    print(search_info)
    try:
        job = Job_info.objects.get(jobName = search_info)
        print(job.jobName)
        request.session['search_info'] = job.jobName
        request.session['search_company'] = 0
    except:
        response['msg'] = '您找的岗位不存在，请重新查找'
        return JsonResponse(response)

    response['msg'] = "提交成功"
    return JsonResponse(response)

def reload_search(request):
    if str(request.session.get('search_info')) != None:
        search_info = str(request.session.get('search_info'))
        job = Job_info.objects.get(jobName = search_info)
        job = model_to_dict(job)
        job = [job]
        phone = str(request.session.get('phone'))
        return render(request,'search.html', {"items": job, "pho_num":phone})

def stu_reload_search(request):
    if str(request.session.get('search_info')) != None:
        search_info = str(request.session.get('search_info'))
        job = Job_info.objects.get(jobName = search_info)
        job = model_to_dict(job)
        job = [job]
        phone = str(request.session.get('phone'))
        return render(request,'stu_search_page.html', {"items": job, "pho_num":phone})

def bole_job_detail_page(request,JobName):
    JobName = str(JobName)
    print(JobName)
    job_list = Job_info.objects.values()
    try:
        job = job_list.filter(jobName = JobName)
        job = list(job)
        job = job[0]
        print(job)
    except:
        return render(request,'main_page.html')
    jobinfo = job['jobInfo']
    jobinfo = jobinfo.split("；")
    jobinfo[0] = jobinfo[0] +'\n'
    for i in range(1,len(jobinfo)):
        jobinfo[i] = jobinfo[i] + '\n'
        jobinfo[0] = jobinfo[0] + jobinfo[i]
    job['jobInfo'] = jobinfo[0]
    jobreq = job['skills']
    jobreq = jobreq.split('；')
    jobreq[0] = jobreq[0] + '\n'
    for i in range(1,len(jobreq)):
        jobreq[i] = jobreq[i]+'\n'
        jobreq[0] = jobreq[0]+jobreq[i]
    job['skills'] = jobreq[0]
    return render(request,'bole_main_job_detail.html',{"item":job})

def bole_search_job_detail_page(request,JobName):
    JobName = str(JobName)
    print(JobName)
    job_list = Job_info.objects.values()
    try:
        job = job_list.filter(jobName = JobName)
        job = list(job)
        job = job[0]
        print(job)
    except:
        return render(request,'main_page.html')
    jobinfo = job['jobInfo']
    jobinfo = jobinfo.split("；")
    jobinfo[0] = jobinfo[0] +'\n'
    for i in range(1,len(jobinfo)):
        jobinfo[i] = jobinfo[i] + '\n'
        jobinfo[0] = jobinfo[0] + jobinfo[i]
    job['jobInfo'] = jobinfo[0]
    jobreq = job['skills']
    jobreq = jobreq.split('；')
    jobreq[0] = jobreq[0] + '\n'
    for i in range(1,len(jobreq)):
        jobreq[i] = jobreq[i]+'\n'
        jobreq[0] = jobreq[0]+jobreq[i]
    job['skills'] = jobreq[0]
    return render(request,'bole_main_job_detail.html',{"item":job})

def bole_search_job_detail_page(request,JobName):
    JobName = str(JobName)
    print(JobName)
    job_list = Job_info.objects.values()
    try:
        job = job_list.filter(jobName = JobName)
        job = list(job)
        job = job[0]
        print(job)
    except:
        return render(request,'main_page.html')
    jobinfo = job['jobInfo']
    jobinfo = jobinfo.split("；")
    jobinfo[0] = jobinfo[0] +'\n'
    for i in range(1,len(jobinfo)):
        jobinfo[i] = jobinfo[i] + '\n'
        jobinfo[0] = jobinfo[0] + jobinfo[i]
    job['jobInfo'] = jobinfo[0]
    jobreq = job['skills']
    jobreq = jobreq.split('；')
    jobreq[0] = jobreq[0] + '\n'
    for i in range(1,len(jobreq)):
        jobreq[i] = jobreq[i]+'\n'
        jobreq[0] = jobreq[0]+jobreq[i]
    job['skills'] = jobreq[0]
    return render(request,'bole_search_job_detail.html',{"item":job})

def stu_job_detail_page(request,JobName):
    obName = str(JobName)
    print(JobName)
    job_list = Job_info.objects.values()
    try:
        job = job_list.filter(jobName = JobName)
        job = list(job)
        job = job[0]
        print(job)
    except:
        return render(request,'main_page.html')
    jobinfo = job['jobInfo']
    jobinfo = jobinfo.split("；")
    jobinfo[0] = jobinfo[0] +'\n'
    for i in range(1,len(jobinfo)):
        jobinfo[i] = jobinfo[i] + '\n'
        jobinfo[0] = jobinfo[0] + jobinfo[i]
    job['jobInfo'] = jobinfo[0]
    jobreq = job['skills']
    jobreq = jobreq.split('；')
    jobreq[0] = jobreq[0] + '\n'
    for i in range(1,len(jobreq)):
        jobreq[i] = jobreq[i]+'\n'
        jobreq[0] = jobreq[0]+jobreq[i]
    job['skills'] = jobreq[0]
    return render(request,'stu_job_detail.html',{"item":job})
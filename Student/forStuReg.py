from common.models import student_info
from django.http import request
from django.http import JsonResponse
def stu_reg(request):
    phone = request.POST.get("phone")
    password = request.POST.get('pwd')
    conf_password = request.POST.get("confirm_pwd")
    school = request.POST.get("school")
    response  = {'msg':None}
    if password !=conf_password:
        response['msg'] = '两次密码不一致，请重新输入'
        return JsonResponse(response)
    else :
        record = student_info.objects.create(phone_num = phone,
                                         password = password,
                                         school_info = school)
        response['msg'] = '注册成功，请登陆'
        return JsonResponse(response)
from common.models import bole
from django.http import request
from django.http import JsonResponse
def bole_reg(request):
    phone = request.POST.get("phone")
    password = request.POST.get('pwd')
    conf_password = request.POST.get("confirm_pwd")
    job_name = request.POST.get("job")
    response  = {'msg':None}
    if password !=conf_password:
        response['msg'] = '两次密码不一致，请重新输入'
        return JsonResponse(response)
    else :
        record = bole.objects.create(phone_num = phone,
                                     job_name = job_name,
                                     password = password,
                                     )
        response['msg'] = '注册成功，请登陆'
        return JsonResponse(response)
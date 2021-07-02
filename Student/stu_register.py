from common import models
from django.http import JsonResponse
def addcustomer(request):

    info = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = models.student_info.objects.create(username=info['username'] ,
                                     phone_num=info['phone'] ,
                                     password=info['password'],
                                     school_info =info['school']
                                                )
    return JsonResponse({'ret': 0, 'id':record.id})
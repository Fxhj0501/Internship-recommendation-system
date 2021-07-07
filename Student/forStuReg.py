from common import models
from django.http import request
def stu_reg(request):
    username = request.POST.get("username")
    password = request.POST.get('password')

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# 查询登陆是否合理
def student_login(request):
    return render(request,'login.html')
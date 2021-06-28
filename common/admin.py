from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import student_info,bole,Job_info
# 超级管理员可以修改学生，伯乐以及岗位信息
admin.site.register(student_info)
admin.site.register(bole)
admin.site.register(Job_info)
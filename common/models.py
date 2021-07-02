from django.db import models

# Create your models here.
from django.db import models

# 学生数据库
class student_info(models.Model):
    # 用户名
    username = models.CharField(max_length=20)
    # 手机号
    phone_num = models.CharField(primary_key=True,max_length=11)
    # 登陆密码
    password = models.CharField(max_length=20)
    # 学校
    school_info = models.CharField(max_length=25)

    class Meta:
        db_table = 'student'

# 伯乐数据库
class bole(models.Model):
    # 用户名
    username = models.CharField(max_length=20)
    # 手机号
    phone_num = models.CharField(primary_key=True,max_length=11)
    # 入职单位
    job = models.CharField(max_length=20)
    # 登陆密码
    password = models.CharField(max_length=20)
    # rec_code推荐码
    rec_code = models.CharField(max_length=50)
    class Meta:
        db_table = 'Bole'

class Job_info(models.Model):
    # 单位
    company = models.CharField(max_length=20,primary_key=True)
    # 入职条件
    requiremnt = models.CharField(max_length=200)
    # 地址
    adress = models.CharField(max_length=50)
    # 待遇
    salary = models.FloatField(max_length=10)
    # 入职日期
    begin_day = models.CharField(max_length=20)
    class Meta:
        db_table = 'Company'
from django.db import models

# Create your models here.
from django.db import models

# 学生数据库
class student_info(models.Model):
    # 手机号
    phone_num = models.CharField(primary_key=True,max_length=11)
    # 登陆密码
    password = models.CharField(max_length=20)
    # 学校
    school_info = models.CharField(max_length=25)
    #技能
    skills = models.CharField(max_length=200)
    #最新实习的岗位
    internship_job = models.CharField(max_length=50)

    class Meta:
        db_table = 'student'

# 伯乐数据库
class bole(models.Model):
    # 手机号
    phone_num = models.CharField(primary_key=True,max_length=11)
    # 入职单位
    job_name = models.CharField(max_length=50)
    # 登陆密码
    password = models.CharField(max_length=20)
    # rec_code推荐码
    rec_code = models.CharField(max_length=50)
    class Meta:
        db_table = 'Bole'

class Job_info(models.Model):
    # 单位
    job_name = models.CharField(max_length=50,primary_key=True)
    #岗位描述
    job_info = models.CharField(max_length=500)
    #所属单位
    company = models.CharField(max_length=50)
    # 入职条件,及所需技能
    skills = models.CharField(max_length=200)
    #联系方式
    contact_info = models.CharField(max_length=100)
    # 地址
    adress = models.CharField(max_length=50)
    # 待遇
    salary = models.FloatField(max_length=10)
    # 内推码
    rec_code = models.CharField(max_length=50)
    class Meta:
        db_table = 'Company'
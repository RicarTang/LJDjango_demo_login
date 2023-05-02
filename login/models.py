from django.db import models

# Create your models here.
class UserInfo(models.Model):  # 继承这个类，固定格式

    user = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    def __str__(self):
        return self.user  # 重写__str__方法，显示字段

class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女')
    )
    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gender,default="男")
    c_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    # ???
    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"
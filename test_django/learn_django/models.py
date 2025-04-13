from django.db import models

# Create your models here.


class student(models.Model):
    '''
    学院管理表
    python .\manage.py makemigrations
    python .\manage.py migrate  
    '''
    id = models.AutoField(primary_key=True) # id 为字段名：AutoFidle 自增的意思; primary_key 唯一的意思 
    name = models.CharField(max_length=64, db_column='name') # CharField数据库里字符类型的意思； max_length最大长度 db_column数据库字段
    age = models.IntegerField(default=0) # IntegerField 数据库名整形 default默认数字
    phone = models.CharField(max_length=64, default='', db_column='phone')
    create_time = models.DateTimeField(auto_now=True) # DateTimeField YYYY-MM-DD HH:MM:SS auto_now 自动填充个当前时间

    def __unicode__(self):
        '''
        配置默认的返回数据
        '''
        return self.id, self.name
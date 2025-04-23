from django.db import models

class NeedFiles(models.Model):
    project = models.CharField(max_length=255, verbose_name='所属项目')
    requirement_doc = models.CharField(max_length=255, verbose_name='需求文档名称')
    version = models.CharField(max_length=50, verbose_name='版本号')
    
    class Meta:
        db_table = 'needfiles'  # 指定使用已存在的表名
        verbose_name = '需求文档表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.project}-{self.requirement_doc}"

class Contents(models.Model):
    needfile = models.ForeignKey(NeedFiles, on_delete=models.CASCADE, db_column='needfile_id', verbose_name='关联需求文档')
    title = models.CharField(max_length=255, verbose_name='分段标题')
    content = models.TextField(verbose_name='分段内容', blank=True, null=True)
    
    class Meta:
        db_table = 'contents'  # 指定使用已存在的表名
        verbose_name = '需求文档内容分段表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
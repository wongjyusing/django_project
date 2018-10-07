from django.db import models

# 个人空间工具链接
class ToolLinks(models.Model):
    name = models.CharField(verbose_name="链接文本",max_length=50)
    link = models.CharField(verbose_name="链接",max_length=200,help_text='请填写http或https开头的完整形式地址')
    img_link = models.URLField('图片地址', help_text='请填写http或https开头的完整形式地址',blank=True)
    class Meta:
        verbose_name = '个人空间'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    # 使对象在后台显示更友善
    def __str__(self):
        return self.name
# 首页和关于的页面内容
class HomeAndAbout(models.Model):
    title = models.CharField(verbose_name='标题',max_length=50)
    body = models.TextField(verbose_name='文章')
    author = models.CharField(verbose_name='作者',default='sing',max_length=50)
    created_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='修改时间',auto_now=True)



    class Meta:
        verbose_name = '首页和关于的页面内容'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    # 使对象在后台显示更友善
    def __str__(self):
        return self.title



# 网站信息填写
class MySiteData(models.Model):
    site_logo = models.CharField(verbose_name="网站logo",max_length=50)
    introduction = models.TextField(verbose_name='网站简介')
    approval_number = models.CharField(max_length=64,verbose_name='网站审批号',default='暂无审批号')

    class Meta:
        verbose_name = '网站信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    # 使对象在后台显示更友善
    def __str__(self):
        return self.site_logo

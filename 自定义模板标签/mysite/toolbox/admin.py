from django.contrib import admin
from .models import HomeAndAbout,MySiteData,ToolLinks
# Register your models here.
# 装饰器方法 注册 Blog类方法
@admin.register(HomeAndAbout)
# 生成一个类，继承admin 的模型后台方法
class HomeAndAboutAdmin(admin.ModelAdmin):
    # 定义一个元组
    list_display = ('title', 'id', 'author', 'created_time', 'update_time')



@admin.register(MySiteData)
# 生成一个类，继承admin 的模型后台方法
class MySiteDataAdmin(admin.ModelAdmin):
    # 定义一个元组
    list_display = ('site_logo', 'introduction')


@admin.register(ToolLinks)
# 生成一个类，继承admin 的模型后台方法
class ToolLinksAdmin(admin.ModelAdmin):
    # 定义一个元组
    list_display = ('name', 'link')

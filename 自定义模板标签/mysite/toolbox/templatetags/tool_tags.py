# toolbox/templaatetags/tool_tags.py
from django import template     # 从Django中导入模板方法

from ..models import HomeAndAbout,MySiteData,ToolLinks

register = template.Library()   # 注册   模板的库   Library 图书馆，可以理解为放书进去，

@register.simple_tag
def test(): # 测试
    return 'hello world'

# 返回所有的个人链接
@register.simple_tag
def get_toollinks():

    return ToolLinks.objects.all()

## 利用列表索引和函数传参的方式，返回Home或About的内容
@register.simple_tag
def get_home_or_about(num):
    return HomeAndAbout.objects.all()[num]

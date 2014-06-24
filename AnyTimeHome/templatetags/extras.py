# -*- coding:utf-8 -*-

from django import template
register = template.Library()

from AnyTimeHome.models import *

#用户模板获取用户名使用过滤器
@register.filter(name='getUsername')
def getUsername(alias):
    try:
        myusername=UserInfo.objects.using('reportplatform').get(useralias=alias).username
    except UserInfo.DoesNotExist:
        myusername=AuthUser.objects.using('default').get(username=alias).username
    return myusername

#根据Server取被修改的次数
@register.filter(name="getCCcounts")
def getCCcounts(serverip):
    countnumber=natlog.objects.filter(ccserver=serverlist(serverip=serverip)).count()
    if countnumber>10000:
        return "10000+"
    else:
        return countnumber

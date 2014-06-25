# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from AnyTimeHome.models import *
from django.template import RequestContext

#systemimport
import xmlrpclib,time

# Create your views here.
def HomePage(request):
    if request.user.is_authenticated():
        #NOWTIME=xmlrpclib.ServerProxy("http://10.2.9.39:7900").getNowtime()
        servers=serverlist.objects.all()
        logs=natlog.objects.all().order_by("-cctime")[0:25]
        user=request.user.username
        return render_to_response('index.html',
            {
                'servers':servers,
                'currentuser':user,
                'logs':logs,
            },
            context_instance=RequestContext(request)
        )
    else:
        return HttpResponseRedirect("/login")

def checkstatus(request):
    if request.user.is_authenticated():
        STATUS=""
        if "serverip" in request.POST:
            try:
                STATUS=xmlrpclib.ServerProxy("http://"+request.POST["serverip"]+":7900").getNowtime()
            except:
                STATUS="远程服务未启动"
            return HttpResponse(STATUS)
        else:
            return HttpResponse("非法操作!")
    else:
        return HttpResponseRedirect("/login")

def submitnewtime(request):
    if request.user.is_authenticated():
        STATUS=""
        if "serverip" in request.POST and "newtime" in request.POST:
            try:
                nowtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                ftimenow=xmlrpclib.ServerProxy("http://"+request.POST["serverip"]+":7900").getNowtime()
                xmlrpclib.ServerProxy("http://"+request.POST["serverip"]+":7900").setNewtime(request.POST["newtime"])
                #开始记录修改日志
                newlog=natlog(
                    ccman=AuthUser(username=request.user.username),
                    ccserver=serverlist(serverip=request.POST["serverip"]),
                    ftime=ftimenow,
                    btime=request.POST["aftertime"],
                    cctime=nowtime
                )
                #保存
                newlog.save()
            except:
                STATUS="发生错误"
            return HttpResponse(STATUS)
        else:
            return HttpResponse("参数错误")
    else:
        return HttpResponseRedirect("/login")

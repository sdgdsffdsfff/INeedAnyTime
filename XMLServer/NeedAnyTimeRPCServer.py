#!/usr/bin/env python
# -*- coding:utf-8 -*-

#system imports
from SimpleXMLRPCServer import SimpleXMLRPCServer as BaseServer
import win32api
import time
import win32serviceutil,win32service,win32event
import socket

#XMLRPC服务器提供的可调用的接口列表,从前端传过来
class anytimeServers(object):

    '''
    anytimeServers类,提供的获取时间和修改时间的方法
    '''

    def getNowtime(self):
        #取当前时间
        nowtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return nowtime

    #根据格式化的时间信息设置系统时间
    def setNewtime(self,newtime):
        #SetSystemTime函数的参数是使用gmt时间
        gmt=time.strptime(newtime, "%Y-%m-%d %H:%M:%S")
        win32api.SetSystemTime(gmt.tm_year,gmt.tm_mon,gmt.tm_wday,gmt.tm_mday,gmt.tm_hour,gmt.tm_min,gmt.tm_sec,0)

class PyNeedAnyTime(win32serviceutil.ServiceFramework):

    """
    写成NT服务
    """

    #服务名
    _svc_name_ = "NeedAnyTimeXMLRPC"
    #服务显示名称
    _svc_display_name_ = "NeedAnyTimeXMLRPC For Ctrip"
    #服务描述
    _svc_description_ = "NeedAnyTimeXMLRPC For Ctrip"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.isAlive = True

    def SvcDoRun(self):
        localIP = socket.gethostbyname(socket.gethostname()) #得到本地ip
        #开始注册和监听
        server=BaseServer((localIP,7900),allow_none=True)
        server.register_instance(anytimeServers())
        server.serve_forever()

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # 设置事件
        win32event.SetEvent(self.hWaitStop)
        self.isAlive = False

if __name__=='__main__':
    win32serviceutil.HandleCommandLine(PyNeedAnyTime)


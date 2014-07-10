INeedAnyTime(Ctrip内部使用)
============

项目简单架构
XML-RPC+Win32API+Django 

用途
============

在测试环境维护和管理中，经常存在测试人员频繁地提出更改服务器时间的需求，
别看只是更改服务器时间，对于管理员而言就需要做一些很低效的工作，远程连接是必不可少的。
为了提高该项工作的效率，INeedAnyTime诞生。

简介
=============
他是一款简单的基于xml-rpc的分布式调用工具。
得益于django的优雅，核心功能用了不到百行代码即完成了所有功能，包括对cas的支持。

Agent部署
=============
服务端的Agent写成了Windows标准服务
安装服务:
```python
python NeedAnyTimeRPCServer.py install

```
启动服务
```python
python NeedAnyTimeRPCServer.py start
```




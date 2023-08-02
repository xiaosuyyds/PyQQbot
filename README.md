# PyQQbot
## 一个基于go-cqhttp与python的QQ机器人。
<p align="center">
  <a href="https://xufuyu.eu.org/">
    <img src="https://cdn.jsdelivr.net/gh/xiaosuyyds/PyQQbot@master/blob/logo1.png"alt="logo">
  </a>
</p>
<div align="center">
_✨ 基于 [Mirai](https://github.com/mamoe/mirai) 以及 [MiraiGo](https://github.com/Mrs4s/MiraiGo) 的 [OneBot](https://github.com/howmanybots/onebot/blob/master/README.md) Golang 原生实现 ✨_  
</div>
<p align="center">
  <a href="https://raw.githubusercontent.com/Mrs4s/go-cqhttp/master/LICENSE">
    <img src="https://img.shields.io/github/license/Mrs4s/go-cqhttp" alt="license">
  </a>
  <a href="https://github.com/Mrs4s/go-cqhttp/releases">
    <img src="https://img.shields.io/github/v/release/Mrs4s/go-cqhttp?color=blueviolet&include_prereleases" alt="release">
  </a>
<a href="https://app.fossa.com/projects/git%2Bgithub.com%2FMrs4s%2Fgo-cqhttp?ref=badge_shield" alt="FOSSA Status"><img src="https://app.fossa.com/api/projects/git%2Bgithub.com%2FMrs4s%2Fgo-cqhttp.svg?type=shield"/></a>
  <a href="https://github.com/howmanybots/onebot/blob/master/README.md">
    <img src="https://img.shields.io/badge/OneBot-v11-blue?style=flat&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABABAMAAABYR2ztAAAAIVBMVEUAAAAAAAADAwMHBwceHh4UFBQNDQ0ZGRkoKCgvLy8iIiLWSdWYAAAAAXRSTlMAQObYZgAAAQVJREFUSMftlM0RgjAQhV+0ATYK6i1Xb+iMd0qgBEqgBEuwBOxU2QDKsjvojQPvkJ/ZL5sXkgWrFirK4MibYUdE3OR2nEpuKz1/q8CdNxNQgthZCXYVLjyoDQftaKuniHHWRnPh2GCUetR2/9HsMAXyUT4/3UHwtQT2AggSCGKeSAsFnxBIOuAggdh3AKTL7pDuCyABcMb0aQP7aM4AnAbc/wHwA5D2wDHTTe56gIIOUA/4YYV2e1sg713PXdZJAuncdZMAGkAukU9OAn40O849+0ornPwT93rphWF0mgAbauUrEOthlX8Zu7P5A6kZyKCJy75hhw1Mgr9RAUvX7A3csGqZegEdniCx30c3agAAAABJRU5ErkJggg==" alt="cqhttp">
  </a>
  <a href="https://github.com/Mrs4s/go-cqhttp/actions">
    <img src="https://github.com/Mrs4s/go-cqhttp/workflows/CI/badge.svg" alt="action">
  </a>
  <a href="https://goreportcard.com/report/github.com/Mrs4s/go-cqhttp">
  <img src="https://goreportcard.com/badge/github.com/Mrs4s/go-cqhttp" alt="GoReportCard">
  </a>
</p>

<p align="center">
  <a href="">文档</a>
  ·
  <a href="">下载</a>
  ·
  <a href="">开始使用</a>
  ·
  <a href="">参与贡献</a>
    ·
  <a href="https://xufuyu.eu.org">博客</a>
      ·
  <a href="mailto:xufuyu@xufuyu.eu.org">邮箱</a>
</p>


### 项目背景
### PyQQbot一个作者没事情干的时候写的QQ机器人
#### PyQQbot操作手册:[临时消息不回复]
1，发送/help 以获取本段文本(会时不时更新哦，记得常来看看)\
2，发送/响应 以开启机器人对话，/沉默 关闭对话（权限要求:群管理员/群主/机器人超管）\
3，发送 娶群友 以随机抽取一位群友作为今日的脑婆（?）\
4，早/午/晚安\
5，防撤回（你撤回个试试啊）\
6，戳一戳反馈（你戳个试试啊，信不信给你禁言了！）\
7，刷屏终结者（打断3条级以上的重复信息）（输入/响应刷屏 运行此功能（默认开启），输入/沉默刷屏 关闭此功能 （权限要求:群管理员/群主/机器人超管））\
8，聊天，atPyQQbot+聊天的内容即可~\
9，/ban add/remove [uid] （将uid拉入/移除黑名单）（权限要求:机器人超管）\
10，签到，发送 签到 即可\
11，/占用 查看机器人占用情况（权限要求:机器人超管）\
12，/群发 [内容] 在已响应的群群发消息。（权限要求:机器人超管）
#### 别的功能还在如火如荼的制作当中~
### 上手指南
## 环境要求
windows 7/8/8.1/10/11\
python 3.8\
go-cqhttp 1.10
## 安装步骤
1.打开go-cqhttp文件夹配置config.yml 填入QQbot的账户与密码\
ps:若是想让bot的封禁少一点的话就把sign-server配置上！\
2.打开pyQQbot文件夹配置Main.py QQbot的QQ号&QQ用户名&机器人超管（与config.yml一致）\
3.配置你的OpenAI的APIkey\
4.安装python依赖库\
requests\
flask\
psutil\
datetime\
openAI\
5.依次运行go-cqhttp与Main.py
## 框架或者技术选型
使用了 go-cqhttp QQ机器人框架，使用http与python通讯。
### 贡献者
#### 一如既往，感谢我们出色的贡献者。
<!-- readme: contributors -start -->
<!-- readme: contributors -end -->
<a href="https://github.com/xiaosuyyds/PyQQbot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=xiaosuyyds/PyQQbot" />
</a>

### 协作者
#### 一如既往，感谢我们出色的协作者。
<!-- readme: collaborators -start -->
<!-- readme: collaborators -end -->

### 作者
Xiaosuyyds\
邮箱：Xiaosu-1009@qq.com
### 版权说明:
开源协议：GNU General Public License v3.0
### 鸣谢:
#### 一如既往，感谢他们。

<a href="https://github.com/xufuyu">
  <img src="https://cdn.jsdelivr.net/gh/xufuyu/CDN@master/favicon.ico"width="100" height="100"alt="logo">
</a><br>
<a href="https://github.com/xufuyu">
  疯子XUFUYU
</a>


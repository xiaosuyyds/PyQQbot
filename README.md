# PyQQbot
## 一个基于go-cqhttp与python的QQ机器人。

### 项目背景
#### PyQQbot一个作者没事情干的时候写的QQ机器人
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
#### 操作环境 windows 7/8/8.1/10/11\
#### 安装步骤
1.打开go-cqhttp文件夹配置config.yml 填入QQbot的账户与密码\
ps:若是想让bot的封禁少一点的话就把sign-server配置上！\
2.打开pyQQbot文件夹配置Main.py QQbot的QQ号&QQ用户名&机器人超管（与config.yml一致）\
3.配置你的OpenAI的APIkey\
4.安装python依赖库\
requests\
flask\
psutil\
warnings\
datetime\
os\
openAI\
5.依次运行go-cqhttp与Main.py
### 框架或者技术选型
使用了 go-cqhttp QQ机器人框架，使用http与python通讯
### 贡献者
一如既往，感谢我们出色的贡献者
<!-- readme: contributors -start -->
<!-- readme: contributors -end -->

### 协作者
一如既往，感谢我们出色的协作者
<!-- readme: collaborators -start -->
<!-- readme: collaborators -end -->
### 版本控制
python 3.8\
go-cqhttp 1.10
### 作者
Xiaosuyyds\
邮箱：Xiaosu-1009@qq.com
### 版权说明:
开源协议：GNU General Public License v3.0
### 鸣谢:
疯子XUFUYU

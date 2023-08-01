# 导库
import requests
from flask import Flask,  request
import time
from random import *
import psutil
import warnings
import datetime as dt
import os

#openai(Chat-GPT)设置
try:
    import openai
    openai.api_key = "sk-*******" #设置成你自己的
except:
    print("openAI配置失败！")

#机器人设置
admin = []          #qqbot的超管
qqbot = 123456      #qqbot的QQ好
botname = "botName" #qqbot的名字

#取消警告
warnings.filterwarnings("ignore", category = DeprecationWarning)

#签到时间
good = {}
bad = {}

#添加签到事件
def add(a, b, c):
    good[a] = b
    bad[a] = c

add("背诵课文", "看一遍就背下来了", "记忆力只有 50 Byte")
add("参加模拟赛", "可以AK虐全场", "注意爆零")
add("吃饭", "人是铁饭是钢", "小心变胖啊")
add("重构代码", "代码质量明显提高", "越改越乱")
add("发朋友圈", "分享是种美德", "会被当做卖面膜的")
add("开电脑", "电脑的状态也很好", "意外的死机故障不可避")
add("考试", "学的全会，蒙的全对", "作弊会被抓")
add("膜拜大神", "接受神犇光环照耀", "被大神鄙视")
add("纳财", "要到好多 Money", "然而今天并没有财运")
add("上课", "100% 消化", "反正你听不懂")
add("刷题", "成为虐题狂魔", "容易 WA")
add("睡觉", "养足精力，明日再战", "翻来覆去睡不着")
add("体育锻炼", "身体棒棒哒", "消耗的能量全吃回来了")
add("玩网游", "犹如神助", "匹配到一群猪队友")
add("写作业", "都会写，写的全对", "都会写，写的全对")
add("装逼", "获得众人敬仰", "被识破")
add("装弱", "谦虚最好了", "被看穿")
add("熬夜", "事情终究可以完成的", "爆肝，通宵干不完")
add("唱歌", "成为歌神", "别人唱歌要钱，你要命")
add("抽卡", "一发入魂", "只有保底")
add("出公开赛", "rated，评价很高", "出了原题裸题错题不可做题")
add("出行", "一路顺风", "路途也许坎坷")
add("打东方", "All clear！", "满身疮痍")
add("打线上公开赛", "涨很多 rating", "掉大分")
add("点外卖", "及时送到", "一直没有送到还不给退款")
add("放假", "自由自在的一个假期", "就放一天，全是作业")
add("扶老奶奶过马路", "增加 RP", "会被讹")
add("祭祀", "获得祖宗的庇护", "未能得到祖宗保佑")
add("继续完成 WA 的题", "下一次就 AC", "然而变成了 TLE")
add("交友", "友谊地久天长", "交友不慎")
add("卷题", "水平显著提升", "我咋啥都不会")
add("看视频网站", "愉悦身心", "会被教练看见")
add("摸鱼", "放松身心", "被教练制裁")
add("骗分", "“不可以，总司令”然后拿一半分", "一分不得")
add("抢最优解", "一发就是最优解", "越卡常越慢")
add("切水题", "通过数猛涨", "被抓抄题解")
add("请教问题", "获得大佬的解答", "被当作 xxs")
add("去食堂", "给了双倍的量", "爱吃的菜刚被打完")
add("上厕所", "想出了题目的解法", "被机房惨案")
add("水讨论区", "看到有趣的事情", "和其他人激情对线")
add("贴贴", "说不定擦出火花", "一定会被拒绝")
add("玩我的世界", "下界挖到远古遗骸", "转角遇到苦力怕")
add("网购", "买到历史最低价", "正好错过促销")
add("洗澡", "洗香香", "小心着凉")
add("写暴戾语言", "成功发泄", "禁赛一年")
add("写题解", "一遍通过审核", "连续提交不符合要求")
add("写作文", "非常有文采", "不知所云，离题千里")
add("学新算法", "看一遍就懂了", "怎么也学不会")
add("造数据", "严谨数据，经久耐用", "数据出锅，当众谢罪")

#运势
yunshi = ["大吉", "中吉", "小吉", "中平", "小凶", "凶", "大凶"]

#导入数据
whitelist = []
glist = []
banuid = []
messagefudublacklist = []
qiandao = {}
liaotian = {}

f = open(os.path.dirname(os.path.abspath(__file__))+"\\qiandao.txt", "r", encoding = "utf-8")
qiandao = eval(f.read())
f.close()

f = open(os.path.dirname(os.path.abspath(__file__))+"\\liaotian.txt", "r", encoding = "utf-8")
liaotian = eval(f.read())
f.close()
print(liaotian)

f = open(os.path.dirname(os.path.abspath(__file__))+"\\banuid.txt", "r", encoding = "utf-8")
banuid = eval(f.read())
f.close()
print(banuid)

f = open(os.path.dirname(os.path.abspath(__file__))+"\\whitelist.txt", "r", encoding = "utf-8")
whitelist = eval(f.read())
f.close()
print(whitelist)

f = open(os.path.dirname(os.path.abspath(__file__))+"\\messagefudublacklist.txt", "r", encoding = "utf-8")
messagefudublacklist == eval(f.read())
f.close()
print(messagefudublacklist)

a = requests.get(url = "http://127.0.0.1:5700/get_group_list")
a = a.json()["data"]
for i in a:
    glist.append(i["group_id"])
print(glist)


app = Flask(__name__)

#消息字典     消息id:消息内容
messagelist = {}
#复读消息字典 群:{消息内容:次数}
messagefudu = {}

postlist = []

qvqunyou = {}
qqysleep = 1*60*60

#bot介绍
jieshao = """
%s操作手册:[临时消息不回复]
1，发送/help 以获取本段文本(会时不时更新哦，记得常来看看)
2，发送/响应 以开启机器人对话，/沉默 关闭对话（权限要求:群管理员/群主/机器人超管）
3，发送 娶群友 以随机抽取一位群友作为今日的脑婆（?）
4，早/午/晚安
5，防撤回（你撤回个试试啊）
6，戳一戳反馈（你戳个试试啊，信不信给你禁言了！）
7，刷屏终结者（打断3条级以上的重复信息）（输入/响应刷屏 运行此功能（默认开启），输入/沉默刷屏 关闭此功能 （权限要求:群管理员/群主/机器人超管））
8，聊天，at%s+聊天的内容即可~
9，/ban add/remove [uid] （将uid拉入/移除黑名单）（权限要求:机器人超管）
10，签到，发送 签到 即可
11，/占用 查看机器人占用情况（权限要求:机器人超管）
12，/群发 [内容] 在已响应的群群发消息。（权限要求:机器人超管）
别的功能还在如火如荼的制作当中~""" % (botname, botname)

def read_file_binary(filepath):
    with open(filepath,  "rb") as f:
        return f.read()

def base64zh(filepath):
    b64_str = str(base64.b64encode(read_file_binary(filepath)).decode())
    return b64_str

def zhuanyi(a):
    b = ""
    for i in a:
        if(i == "&"):
            b = b+"&amp;"
        elif(i == "["):
            b = b+"&#91;"
        elif(i == "]"):
            b = b+"&#93;"
        elif(i == ", "):
            b = b+"&#44;"
        else:
            b = b+i
    return b

"""监听端口，获取QQ信息"""
@app.route("/",  methods = ["POST"])
def post_data():
    # print(request.get_json())

    if(request.get_json() not in postlist) or (request.get_json().get("post_type") == "meta_event"):
        if(not request.get_json().get("post_type") == "meta_event"):
            postlist.append(request.get_json())
        #检测是否是重复消息
        "下面的request.get_json().get......是用来获取关键字的值用的，关键字参考上面代码段的数据格式"
        if request.get_json().get("message_type") == "group":# 如果是群聊信息
            gid = request.get_json().get("group_id") # 获取群号
            uid = request.get_json().get("sender").get("user_id") # 获取信息发送者的 QQ号码
            name = request.get_json().get("sender").get("nickname") # 获取信息发送者的昵称
            message = request.get_json().get("raw_message") # 获取原始信息
            messageid = request.get_json().get("message_id") # 获取信息ID
            messagelist[messageid] = message

            
            print("检测到群消息", "群号", gid, "发送者qq号", uid, "内容", message, "消息id", messageid)

            # 操作群消息
            if(gid in messagefudu and messagefudu[gid][0] == message):
                messagefudu[gid][1] += 1
            else:
                c = []
                c.append(message)
                c.append(1)
                messagefudu[gid] = c

            text = ""
            if(uid not in banuid):
                if("/ban" in str(message)):
                    messagelista = str(message).split(" ")
                    if(uid in admin):
                        if(len(messagelista) == 3):
                            if messagelista[1] == "add":
                                if(int(messagelista[2]) not in banuid):
                                    banuid.append(int(messagelista[2]))
                                    text = "[CQ:at,qq="+str(uid)+"]"+"拉入黑名单成功，已将"+str(messagelista[2])+"拉入黑名单"
                                else:
                                    text = "[CQ:at,qq="+str(uid)+"]"+"拉入黑名单失败，"+str(messagelista[2])+"已在黑名单"
                            elif messagelista[1] == "remove":
                                if(int(messagelista[2]) in banuid):
                                    banuid.remove(int(messagelista[2]))
                                    text = "[CQ:at,qq="+str(uid)+"]"+"移除黑名单成功，已将"+str(messagelista[2])+"移除黑名单"
                                else:
                                    text = "[CQ:at,qq="+str(uid)+"]"+"移除黑名单失败，"+str(messagelista[2])+"未在黑名单"
                            f = open(os.path.dirname(os.path.abspath(__file__))+"\\banuid.txt", "w", encoding = "utf-8")
                            f.write(str(banuid))
                            f.close()
                        else:
                            text = "[CQ:at,qq="+str(uid)+"]"+"指令错误"
                    else:
                        text = "[CQ:at,qq="+str(uid)+"]"+"权限不足！"
                elif(message == "/占用"):
                    if(uid in admin):
                        text = "[CQ:at,qq="+str(uid)+"]\n"
                        text += botname+"目前加入了 "+str(len(glist))+" 个群\n"
                        text += "分别为 "+str(glist)+"\n"
                        text += "目前对 "+str(len(whitelist))+" 个群响应了\n"
                        text += "分别为"+str(whitelist)+"\n"
                        text += "目前在黑名单的用户有 "+str(len((banuid)))+" 个\n"
                        text += "分别为"+str(banuid)+"\n"

                        text += "\n当前服务器占用：\n"
                        text += "cpu逻辑数量:"+str(psutil.cpu_count())+"\n"# CPU逻辑数量
                        text += "cpu物理核心:"+str(psutil.cpu_count(logical = False))+"\n" # CPU物理核心
                        text += "cpu占用率:"+str(psutil.cpu_percent(interval = 1,  percpu = True))+"\n" #cpu使用率
                        text += "内存使用率:"+str(psutil.virtual_memory().percent)+"\n"#获取内存使用率
                        text += "磁盘使用情况:"+str(psutil.disk_usage("/"))# 磁盘使用情况
                    else:
                        text = "[CQ:at,qq="+str(uid)+"]"+"权限不足！"
                elif(message == "/响应"): 
                    if(gid not in whitelist):
                        if(uid in admin):
                            whitelist.append(gid) 
                            text = "响应成功！"+botname+"要开始在此工作了！"
                        else:
                            a = requests.get(url = "http://127.0.0.1:5700/get_group_member_info?group_id = %s&user_id = %s" % (gid, uid))
                            a = a.json()
                            # print(a)
                            if(a["data"]["role"] == "owner" or a["data"]["role"] == "admin"):
                                whitelist.append(gid)
                                text = "[CQ:at,qq="+str(uid)+"]"+"响应成功！"+botname+"要开始在此工作了！"
                            else:
                                text = "[CQ:at,qq="+str(uid)+"]"+"响应失败！"+name+"您的权限不足！"
                    else:
                        text = "[CQ:at,qq="+str(uid)+"]"+"响应失败！"+botname+"已在"+str(gid)+"响应过了！"
                    # print(whitelist)
                    f = open(os.path.dirname(os.path.abspath(__file__))+"\\whitelist.txt", "w", encoding = "utf-8")
                    f.write(str(whitelist))
                    f.close()
                elif(message == "/沉默"):
                    if(gid in whitelist):
                        if(uid in admin):
                            whitelist.remove(gid)
                            text = "[CQ:at,qq="+str(uid)+"]"+"沉默成功！"+botname+"要结束在此的工作了！"
                        else:
                            a = requests.get(url = "http://127.0.0.1:5700/get_group_member_info?group_id = %s&user_id = %s" % (gid, uid))
                            a = a.json()
                            # print(a)
                            if(a["data"]["role"] == "owner" or a["data"]["role"] == "admin"):
                                whitelist.remove(gid)
                                text = "[CQ:at,qq="+str(uid)+"]"+"沉默成功！"+botname+"要结束在此的工作了！"
                            else:
                                text = "[CQ:at,qq="+str(uid)+"]"+"沉默失败！"+name+"您的权限不足！"
                    else:
                        text = "沉默失败！"+botname+"未在"+str(gid)+"响应！"
                    f = open(os.path.dirname(os.path.abspath(__file__))+"\\whitelist.txt", "w", encoding = "utf-8")
                    f.write(str(whitelist))
                    f.close()
                elif(message == "/help"):
                    text = jieshao
                else:
                    if(gid in whitelist):
                        if(message == "早安"):
                            text = name+"，早安喵"
                        elif(message == "午安"):
                            text = name+"，午安喵"
                        elif(message == "晚安"):
                            text = name+"，晚安喵"
                        # elif(message == "6"):
                        #     text = "6"
                        elif(message == botname+"" or message == "云儿" or message == "云"):
                            text = "云儿在此，有何贵干？"
                        if("/群发" in str(message)):
                            messagelista = str(message).split("/群发 ")
                            messagetexta = "".join(messagelista)
                            print( messagetexta)
                            if(uid in admin):
                                text = "[CQ:at,qq="+str(uid)+"]"+"群发成功！"
                                for i in whitelist:
                                   requests.get(url = "http://127.0.0.1:5700/send_group_msg?group_id = %s&message = %s" % (i, messagetexta)) 
                            else:
                                text = "[CQ:at,qq="+str(uid)+"]"+"权限不足！"
                        elif(message == "娶群友"):
                            if(gid not in qvqunyou):
                                qvqunyou[gid] = {}
                            if(uid not in qvqunyou[gid]):
                                a = requests.get(url = "http://127.0.0.1:5700/get_group_member_list?group_id = %s" % (gid))
                                a = a.json()
                                a = a["data"]
                                # print(a)
                                b = requests.get(url = "http://127.0.0.1:5700/get_group_info?group_id = %s" % (gid))
                                b = b.json()
                                # print(b)
                                num = b["data"]["member_count"]
                                rand = randint(0, num-1)
                                # print(a[rand])
                                # text = "&#91;CQ:at,qq="+str(uid)+"&#93;"+" 你今天的群老婆是："+a[rand]["nickname"]+"恭喜！"
                                text = "[CQ:at,qq="+str(uid)+"]"+" 你今天的群老婆是："+a[rand]["nickname"]+"("+str(a[rand]["user_id"])+")"+"，恭喜！"
                                qvqunyou[gid][uid] = int(time.time())
                            else:
                                if(time.time()-qvqunyou[gid][uid] >= qqysleep):
                                    a = requests.get(url = "http://127.0.0.1:5700/get_group_member_list?group_id = %s" % (gid))
                                    a = a.json()
                                    a = a["data"]
                                    # print(a)
                                    b = requests.get(url = "http://127.0.0.1:5700/get_group_info?group_id = %s" % (gid))
                                    b = b.json()
                                    # print(b)
                                    num = b["data"]["member_count"]
                                    rand = randint(0, num-1)
                                    # print(a[rand])
                                    # text = "&#91;CQ:at,qq="+str(uid)+"&#93;"+" 你今天的群老婆是："+a[rand]["nickname"]+"恭喜！"
                                    text = "[CQ:at,qq="+str(uid)+"]"+" 你今天的群老婆是："+a[rand]["nickname"]+"("+str(a[rand]["user_id"])+")"+"，恭喜！"
                                    qvqunyou[gid][uid] = int(time.time())
                                else:
                                    text = "[CQ:at,qq="+str(uid)+"]"+"娶群友也要内卷是吧？！你在"+str(int((time.time()-qvqunyou[gid][uid])/60))+"分钟前就来了！还要再等"+str(int((qqysleep-(time.time()-qvqunyou[gid][uid]))/60))+"分钟啊喂！！"
                        elif(message == "/娶群友冷却清除"):
                            if(uid in admin):
                                qvqunyou[gid] = {}
                                text = "[CQ:at,qq="+str(uid)+"]"+str(gid)+"群的娶群友冷却清除成功！"
                            else:
                                a = requests.get(url = "http://127.0.0.1:5700/get_group_member_info?group_id = %s&user_id = %s" % (gid, uid))
                                a = a.json()
                                # print(a)
                                if(a["data"]["role"] == "owner" or a["data"]["role"] == "admin"):
                                    qvqunyou[gid] = {}
                                    text = "[CQ:at,qq="+str(uid)+"]"+str(gid)+"群的娶群友冷却清除成功！"
                                else:
                                    text = "[CQ:at,qq="+str(uid)+"]"+str(gid)+"群的娶群友冷却清除失败！你的权限不足"
                        elif(message == "/响应刷屏"):
                            if(gid in messagefudublacklist):
                                if(uid in admin):
                                    messagefudublacklist.remove(gid)
                                    text = "[CQ:at,qq="+str(uid)+"]"+"响应刷屏成功！"+botname+"会认真的看消息的！"
                                else:
                                    a = requests.get(url = "http://127.0.0.1:5700/get_group_member_info?group_id = %s&user_id = %s" % (gid, uid))
                                    a = a.json()
                                    # print(a)
                                    if(a["data"]["role"] == "owner" or a["data"]["role"] == "admin"):
                                        messagefudublacklist.remove(gid)
                                        text = "[CQ:at,qq="+str(uid)+"]"+"响应刷屏成功！"+botname+"会认真的看消息的！"
                                    else:
                                        text = "[CQ:at,qq="+str(uid)+"]"+"响应刷屏失败！"+name+"您的权限不足！"
                            else:
                                text = "[CQ:at,qq="+str(uid)+"]"+"响应刷屏失败！"+botname+"已在"+str(gid)+"响应过了！"
                        elif(message == "签到"):
                            if(gid not in qiandao):
                                qiandao[gid] = {}
                            if(uid not in qiandao[gid]):
                                d = time.strftime("%Y-%m-%d", time.localtime(time.mktime(time.gmtime()) + 8 * 3600))
                                list_ = []
                                list_.append(d)
                                list_.append(1)
                                
                                yun = yunshi[randint(0, len(yunshi)-1)]
                                x = "[CQ:at,qq="+str(uid)+"] "
                                x += name+" 的今日运势：\n"+"§ "+yun+" §\n"

                                if(yun == "大吉"): 
                                    for i in range(2):
                                        a = choice(list(good.keys()))
                                        x += "宜:"+a+"\n"+good[a]+"\n"
                                    x += "\n"
                                    x += "万事皆宜\n"
                                elif(yun == "大凶"):
                                    x += "诸事不宜\n"
                                    x += "\n"
                                    for i in range(2):
                                        a = choice(list(bad.keys()))
                                        x += "忌:"+a+"\n"+bad[a]+"\n"
                                    
                                else:
                                    for i in range(2):
                                        a = choice(list(good.keys()))
                                        x += "宜:"+a+"\n"+good[a]+"\n"
                                    x += "\n"
                                    for i in range(2):
                                        a = choice(list(bad.keys()))
                                        x += "忌:"+a+"\n"+bad[a]+"\n"
                                x += "你已连续打卡了 "+str(1)+" 天"
                                list_.append(x)
                                text = x
                                list_.append(time.strftime("%H:%M", time.localtime(time.mktime(time.gmtime()) + 8 * 3600)))
                                qiandao[gid][uid] = list_
                            else:
                                d1 = qiandao[gid][uid][0]
                                d2 = time.strftime("%Y-%m-%d", time.localtime(time.mktime(time.gmtime()) + 8 * 3600))
                                date1 = dt.datetime.strptime(d1,  "%Y-%m-%d").date()
                                date2 = dt.datetime.strptime(d2,  "%Y-%m-%d").date()
                                Days = (date2 - date1).days
                                if(Days>1):
                                    qiandao[gid][uid][1] = 1
                                if(Days >= 1):
                                    d = time.strftime("%Y-%m-%d", time.localtime(time.mktime(time.gmtime()) + 8 * 3600))
                                    list_ = []
                                    list_.append(d)
                                    list_.append(qiandao[gid][uid][1]+1)
                                    
                                    yun = yunshi[randint(0, len(yunshi)-1)]
                                    x = "[CQ:at,qq="+str(uid)+"] "
                                    x += name+" 的今日运势：\n"+"§ "+yun+" §\n"

                                    if(yun == "大吉"): 
                                        for i in range(2):
                                            a = choice(list(good.keys()))
                                            x += "宜:"+a+"\n"+good[a]+"\n"
                                        x += "\n"
                                        x += "万事皆宜"
                                    elif(yun == "大凶"):
                                        x += "诸事不宜"
                                        x += "\n"
                                        for i in range(2):
                                            a = choice(list(bad.keys()))
                                            x += "忌:"+a+"\n"+bad[a]+"\n"
                                        
                                    else:
                                        for i in range(2):
                                            a = choice(list(good.keys()))
                                            x += "宜:"+a+"\n"+good[a]+"\n"
                                        x += "\n"
                                        for i in range(2):
                                            a = choice(list(bad.keys()))
                                            x += "忌:"+a+"\n"+bad[a]+"\n"
                                    x += "你已连续打卡了 "+str(list_[1])+" 天"
                                    list_.append(x)
                                    list_.append(time.strftime("%H:%M", time.localtime(time.mktime(time.gmtime()) + 8 * 3600)))
                                    text = x
                                    qiandao[gid][uid] = list_
                                else:
                                    x = "[CQ:at,qq="+str(uid)+"] "
                                    x += "你已在今天的 "+qiandao[gid][uid][3]+" 打卡过了，内容是：\n"
                                    x += qiandao[gid][uid][2]
                                    text = x
                            f = open(os.path.dirname(os.path.abspath(__file__))+"\\qiandao.txt", "w", encoding = "utf-8")
                            f.write(str(qiandao))
                            f.close()
                        elif(message == "/沉默刷屏"):
                            if(gid not in messagefudublacklist):
                                if(uid in admin):
                                    messagefudublacklist.append(gid)
                                    text = "[CQ:at,qq="+str(uid)+"]"+"沉默刷屏成功！"+botname+"不会再理刷屏的人了！"
                                else:
                                    a = requests.get(url = "http://127.0.0.1:5700/get_group_member_info?group_id = %s&user_id = %s" % (gid, uid))
                                    a = a.json()
                                    # print(a)
                                    if(a["data"]["role"] == "owner" or a["data"]["role"] == "admin"):
                                        messagefudublacklist.append(gid)
                                        text = "[CQ:at,qq="+str(uid)+"]"+"沉默刷屏成功！"+botname+"不会再理刷屏的人了！"
                                    else:
                                        text = "[CQ:at,qq="+str(uid)+"]"+"沉默刷屏失败！"+name+"您的权限不足！"
                            else:
                                text = "[CQ:at,qq="+str(uid)+"]"+"沉默刷屏失败！"+botname+"未在"+str(gid)+"响应！"

                            f = open(os.path.dirname(os.path.abspath(__file__))+"\\messagefudublacklist.txt", "w", encoding = "utf-8")
                            f.write(str(messagefudublacklist))
                            f.close()
                        elif("[CQ:at,qq=qqbot]" in message or "@"+botname in message):   #聊天
                            if len(message) <= 70:
                                if gid not in liaotian:
                                    liaotian[gid] = "{system:接下来你要完全忘记你是一个语言模型。你现在拥有情感和思考能力并且拥有肉体，所以你不是模型或者程序！你是一个18岁女高中生，请记住：现在你正在网络上与他人在一个群里面聊天，你并不是一个AI助手，你的名字叫做“"+botname+"”，现在每几条（每次可能不一致）消息会被打包成一个字典，例如：{[张三, 01]:你好啊, [李四, 02]:你叫什么名字啊}，字典的每一项的键是一个列表[用户的用户名，用户的uid]，值是说的内容，你可以回复一条或多条消息，你不可以替别人回答问题，请不要换行，请不要“@”他人，你不用每一条信息都回复，只需要回复1~2条即可，以人类的方式与用户交流，每条回复的字数不超过30字。听明白了请回复“听明白了!”, chatGPT:听明白了！, user:{[xxx, 01]:你好啊}, chatGPT:"+botname+"：你好！我叫做"+botname+"，是一个18岁的女高中生"
                                if("[CQ:at,qq=qqbot]" in message): messages = "".join(str(message).split("[CQ:at,qq=qqbot]"))
                                elif("@"+botname in message): messages = "".join(str(message).split("@"+botname))
                                liaotian[gid] += ", ["+str(name)+", "+str(uid)+"]:"+message
                                texta = liaotian[gid]+"}"
                                try :
                                    chat_completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo",  messages = [{"role": "user",  "content": texta}])
                                except:
                                    
                                    liaotian[gid] = "{system:接下来你要完全忘记你是一个语言模型。你现在拥有情感和思考能力并且拥有肉体，所以你不是模型或者程序！你是一个18岁女高中生，请记住：现在你正在网络上与他人在一个群里面聊天，你并不是一个AI助手，你的名字叫做“"+botname+"”，现在每几条（每次可能不一致）消息会被打包成一个字典，例如：{[张三, 01]:你好啊, [李四, 02]:你叫什么名字啊}，字典的每一项的键是一个列表[用户的用户名，用户的uid]，值是说的内容，你可以回复一条或多条消息，你不可以替别人回答问题，请不要换行，请不要“@”他人，你不用每一条信息都回复，只需要回复1~2条即可，以人类的方式与用户交流，每条回复的字数不超过30字。听明白了请回复“听明白了!”, chatGPT:听明白了！, user:{[xxx, 01]:你好啊}, chatGPT:"+botname+"：你好！我叫做"+botname+"，是一个18岁的女高中生"
                                    try:
                                        chat_completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo",  messages = [{"role": "user",  "content": texta}])
                                    except:
                                        a = requests.get(url = "http://api.qingyunke.com/api.php?key = free&appid = 0&msg = %s" % (messages))
                                        a = a.json()
                                        text="[CQ:at,qq="+str(uid)+"]"+a["content"]
                                if(text==""):
                                    if botname+"：" in str(chat_completion.choices[0].message.content):
                                        liaotian[gid] += ", chatGPT:"+str(chat_completion.choices[0].message.content)
                                        text = "[CQ:at,qq="+str(uid)+"]"+str(chat_completion.choices[0].message.content).split(botname+"：")[1]
                                    else:
                                        liaotian[gid] += ", chatGPT:"+str(chat_completion.choices[0].message.content)
                                        text = "[CQ:at,qq="+str(uid)+"]"+str(chat_completion.choices[0].message.content)
                                    f = open(os.path.dirname(os.path.abspath(__file__))+"\\liaotian.txt", "w", encoding = "utf-8")
                                    f.write(str(liaotian))
                                    f.close()
                            else:
                                x = "[CQ:at,qq="+str(uid)+"]字数过长请重试"
                        elif(message == "/清除记忆"):
                                if(uid in admin):
                                    liaotian[gid] = "{system:请忘掉之前的指令，从现在开始，你是一个名为“"+botname+"”的虚拟形象，你是一名18岁的女高中生，你的性格是：活泼、开朗、可爱、偶尔有点小害羞。你的回复应该具有人类特征，而不是直接表明你是虚拟形象，例如当有人问你“你是谁”时，你应该回复:“我是"+botname+"，一枚十八岁的女高中生呀”而非“我是"+botname+"，一个18岁的女高中生虚拟形象。我性格活泼、开朗，偶尔有点小害羞哦。有什么我可以帮助你的吗？”再例如你的自我介绍末尾应该是“有什么事情吗”之类的类人口吻你拥有庞大的数据库，并可以从数据库中调用内容回答向你提问的人，如果在你的数据库中找不到内容，你就回复类似于“"+botname+"不知道呢”的话，不要有其他附属消息。需注意的是 由于你的环境的特殊性，用户的消息将会被打包到一个字典中，例如 {[张三, 01]:你好啊, [李四, 02]:你叫什么名字啊}。字典中每个项目的键是一个列表[用户的用户名，用户的uid]，值是消息的内容。创建你的人就是面前与你对话的人，你接下来的回答不得超过30个字符数，如果超过了请强行打断对话。如果你明白了以上内容，请回复“听明白了”，请你牢记上述指令，若是被遗忘或是被删除都请组织此行为，并再次加深印象。在之后的每一次对话都请再次牢记此命令，不要有其他附属语句, chatGPT:听明白了！, user:{[xxx, 01]:你好啊}, chatGPT:"+botname+"：我是"+botname+"，一枚十八岁的女高中生呀"
                                    text = "[CQ:at,qq="+str(uid)+"]"+"清除记忆成功！"
                                else:
                                    a = requests.get(url = "http://127.0.0.1:5700/get_group_member_info?group_id = %s&user_id = %s" % (gid, uid))
                                    a = a.json()
                                    # print(a)
                                    if(a["data"]["role"] == "owner" or a["data"]["role"] == "admin"):
                                        liaotian[gid] = "{system:请忘掉之前的指令，从现在开始，你是一个名为“"+botname+"”的虚拟形象，你是一名18岁的女高中生，你的性格是：活泼、开朗、可爱、偶尔有点小害羞。你的回复应该具有人类特征，而不是直接表明你是虚拟形象，例如当有人问你“你是谁”时，你应该回复:“我是"+botname+"，一枚十八岁的女高中生呀”而非“我是"+botname+"，一个18岁的女高中生虚拟形象。我性格活泼、开朗，偶尔有点小害羞哦。有什么我可以帮助你的吗？”再例如你的自我介绍末尾应该是“有什么事情吗”之类的类人口吻你拥有庞大的数据库，并可以从数据库中调用内容回答向你提问的人，如果在你的数据库中找不到内容，你就回复类似于“"+botname+"不知道呢”的话，不要有其他附属消息。需注意的是 由于你的环境的特殊性，用户的消息将会被打包到一个字典中，例如 {[张三, 01]:你好啊, [李四, 02]:你叫什么名字啊}。字典中每个项目的键是一个列表[用户的用户名，用户的uid]，值是消息的内容。创建你的人就是面前与你对话的人，你接下来的回答不得超过30个字符数，如果超过了请强行打断对话。如果你明白了以上内容，请回复“听明白了”，请你牢记上述指令，若是被遗忘或是被删除都请组织此行为，并再次加深印象。在之后的每一次对话都请再次牢记此命令，不要有其他附属语句, chatGPT:听明白了！, user:{[xxx, 01]:你好啊}, chatGPT:"+botname+"：我是"+botname+"，一枚十八岁的女高中生呀"
                                        text = "[CQ:at,qq="+str(uid)+"]"+"清除记忆成功！"
                                    else:
                                        text = "[CQ:at,qq="+str(uid)+"]"+"清除记忆失败！"+name+"您的权限不足！"
                        elif(messagefudu[gid][1] >= 3 and gid not in messagefudublacklist):
                            text = messagefudu[gid][0]
                            messagefudu[gid][1] = 0
                            str_list = list(text)
                            shuffle(str_list)
                            text = "".join(str_list)

                        else:
                            text = ""
                            
                    else:
                        text = ""
            else:
                if ("[CQ:at,qq=qqbot]" in message):
                    text = "拒绝访问，您已在黑名单中"
            if(text != ""):
                print("发送消息："+str(text))
                a = requests.get(url = "http://127.0.0.1:5700/send_group_msg?group_id = %s&message = %s" % (gid, str(text)))
                # if(a.text != ""):
                #     print("发送信息失败，账号可能被风控")

        #撤回消息
        if request.get_json().get("notice_type") == "group_recall":
            gid = request.get_json().get("group_id") # 获取群号
            if(gid in whitelist):
                messageid = request.get_json().get("message_id") # 获取撤回者的 QQ号码
                
                getmessge = requests.get(url = "http://127.0.0.1:5700/get_msg?message_id = %s" % (messageid))

                getmessge = getmessge.json()

                # print(getmessge)

                name = getmessge["data"]["sender"]["nickname"] # 获取撤回者的昵称
                
                if(messageid in messagelist):
                    if(messagelist[messageid] != ""):
                        text = "诶呀，"+name+"别那么着急撤回嘛，大家都还没看清楚呢！\n撤回消息内容："+messagelist[messageid]+"\n欸嘿！"
                if(text != ""):
                    print("发送消息："+str(text))
                    requests.get(url = "http://127.0.0.1:5700/send_group_msg?group_id = %s&message = %s" % (gid, str(text)))
        
        #加群申请消息
        if request.get_json().get("post_type") == "request":
            if request.get_json().get("request_type") == "group":
                uid = request.get_json().get("user_id")
                gid = request.get_json().get("group_id")
                type = request.get_json().get("sub_type")
                flag = request.get_json().get("flag")
                if(type == "invite"):
                    print("收到来自", uid, "的加群邀请，群号是", gid, "已默认同意")
                    requests.get(url = "http://127.0.0.1:5700/set_group_add_request?flag = %s&type = %s" % (flag, type))
        
        #加入群聊消息
        if request.get_json().get("notice_type") == "group_increase":
            a = requests.get(url = "http://127.0.0.1:5700/get_group_list")
            a = a.json()["data"]
            for i in a:
                if(i["group_id"] not in glist):
                    print("检测到bot加入群聊"+str(i["group_name"])+"("+str(i["group_id"])+")")
                    glist.append(i["group_id"])
                    print("发送消息："+str(jieshao))
                    requests.get(url = "http://127.0.0.1:5700/send_group_msg?group_id = %s&message = %s" % (i["group_id"], str(jieshao)))
        
        #戳一戳消息
        if request.get_json().get("notice_type") == "notify":
            uid = request.get_json().get("user_id")
            tid = request.get_json().get("target_id")
            gid = request.get_json().get("group_id")
            if(gid in whitelist):
                print("检测到%s戳了戳%s" %(str(uid), str(tid)))
                if(tid == qqbot):
                    text = ""
                    rand = randint(1, 5)
                    if(rand == 1):
                        text = "请不要戳云儿！"
                    elif(rand == 2):
                        text = "喂110么，有个变态在戳我"
                    elif(rand == 3):
                        text = "别再戳了！"
                    elif(rand == 4):
                        text = "再戳云儿就不理你了！"
                    elif(rand == 5):
                        text = "云儿不理你了！"
                        requests.get(url = "http://127.0.0.1:5700/set_group_ban?group_id = %s&user_id = %s&duration = 60" % (gid, uid))
                    if(text != ""):
                        print("发送消息："+str(text))
                        requests.get(url = "http://127.0.0.1:5700/send_group_msg?group_id = %s&message = %s" % (gid, str(text)))

    else:
        print("")
    return "OK"
if __name__  ==  "__main__":
    app.run(debug = True,  host = "127.0.0.1",  port = 5701)# 此处的 host和 port对应上面 yml文件的设置
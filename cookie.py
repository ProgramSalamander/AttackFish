from urllib import request
from http import cookiejar

posturl = 'http://jfjwuxc.cn/abc/gogo.asp'

cookie = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
response = opener.open(posturl)
print(response.read().decode('gbk'))
response.delete_cookie
for item in cookie:
    print('Name = %s' % item.name)
    print('Value = %s' % item.value)
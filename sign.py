import requests
import time
import datetime
import re
import rsa
import json
import base64
import sys
from urllib import parse

if len(sys.argv) < 2:
    print('账号不能为空！!')
    exit()

if len(sys.argv) < 3:
    print('密码不能为空！!')
    exit()


username=sys.argv[1]
password=sys.argv[2]

header = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://dashboard.locyanfrp.cn/"
}
print('准备登录中....')
url = 'https://api-v2.locyanfrp.cn/api/v2/auth/login'
myobj = 'username=' + username + '&password='+password
#resp = requests.get(url, headers=header, proxies=proxies)
resp = requests.post(url, data=myobj , headers=header)
data = resp.json()
print(data)
token = data['data']['token']
if data['message'] == 'OK':
    print('登录成功')
else:
    print('登录失败')

print('准备签到中....')
url1 = 'https://api-v2.locyanfrp.cn/api/v2/sign'
header1 = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://dashboard.locyanfrp.cn/",
        'Authorization': 'Bearer ' + token
}
myobj1 = 'username='+data['data']['username']
resp1 = requests.post(url1, data=myobj1 , headers=header1)
data1 = resp1.json()
print(data1['message'])

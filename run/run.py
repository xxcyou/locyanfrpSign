#!/usr/bin/env python
# coding=utf-8

import sys
import datetime
import requests

if len(sys.argv) < 2:
    print('账号不能为空！')
    exit()

if len(sys.argv) < 3:
    print('密码不能为空！')
    exit()


username=sys.argv[1]
password=sys.argv[2]

header = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'referer': 'https://preview.locyanfrp.cn'
}
print('准备登录中....')
url = 'https://api-v2.locyanfrp.cn/api/v2/users/login'
myobj = {'0[username]': '','0[password]': '','username': username,'password':password}
#resp = requests.get(url, headers=header, proxies=proxies)
resp = requests.post(url, data=myobj , headers=header)
data = resp.json()
token = data['data']['token']
if data['msg'] == 'success':
    print('登录成功')
else:
    print('登录失败')

print('准备签到中....')
url1 = 'https://api.locyanfrp.cn/User/DoSign'
header1 = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'referer': 'https://preview.locyanfrp.cn',
        'Authorization': 'Bearer ' + token
}
myobj1 = {'token': token}
resp1 = requests.post(url1, data=myobj1 , headers=header1)
data1 = resp1.json()
print(data1['message'])

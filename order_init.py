# -*-coding:UTF-8-*
import urllib2
import  urllib
import  json
import  hashlib

#header
headers={
    'Content-Type': 'application/json',

    'Cookie':'JSESSIONID=8de751e3-9f5b-4d6a-a1ee-41237c3b14bc;\
    Hm_lvt_407473d433e871de861cf818aa1405a1=1522381448,1522637444;\
    Hm_lpvt_407473d433e871de861cf818aa1405a1=1522652420;\
    user=415703913;\
    sid=8de751e3-9f5b-4d6a-a1ee-41237c3b14bc'
}

#url
url="https://t.finlean.com/insb/insb1/order/init"
#session id
sessionld="8de751e3-9f5b-4d6a-a1ee-41237c3b14bc"
#创建md5对象
m = hashlib.md5()
#传入需要加密的字符串
m.update(sessionld)
#获取加密后的字符串
jttechSign=m.hexdigest()

#传参
data={

    'jttechSign':jttechSign
}

#发送请求
request=urllib2.Request(url=url,headers=headers,data=json.dumps(data))
#响应
responce=urllib2.urlopen(request)
#读出来
print responce.read()
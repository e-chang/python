# -*-coding:UTF-8-*
import urllib
import urllib2
import hashlib
import json
url="https://t.finlean.com/insb/insb1/order/list"
# headers = {
#     'Content-Type': 'application/json',
#     'Cookie':'JSESSIONID=e903840c-b994-40c2-806e-6572942b7045;\
#      Hm_lvt_407473d433e871de861cf818aa1405a1=1522381448;\
#       Hm_lpvt_407473d433e871de861cf818aa1405a1=1522394788;\
#      user=415703913;\
#      sid=e903840c-b994-40c2-806e-6572942b7045'
# }
#headers信息
headers={
    'Content-Type': 'application/json',

    'Cookie':'JSESSIONID=8de751e3-9f5b-4d6a-a1ee-41237c3b14bc;\
    Hm_lvt_407473d433e871de861cf818aa1405a1=1522381448,1522637444;\
    Hm_lpvt_407473d433e871de861cf818aa1405a1=1522652420;\
    user=415703913;\
    sid=8de751e3-9f5b-4d6a-a1ee-41237c3b14bc'
}
#session id
sessionld="8de751e3-9f5b-4d6a-a1ee-41237c3b14bc"

#创建md5对象
m = hashlib.md5()
#传入需要加密的字符串

m.update('10'+'2'+'1'+sessionld)
#获取加密后的字符串
jttechSign=m.hexdigest()
data={
    'page':1,
    'rows':10,
    'sortType':2,
    'jttechSign':jttechSign
}
print  json.dumps(data);
#请求
request = urllib2.Request(url=url, headers=headers, data=json.dumps(data))

#响应
response = urllib2.urlopen(request)
print  'hi'
#读
res=response.read()
print  res


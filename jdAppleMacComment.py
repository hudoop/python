#coding=utf-8
import urllib2
import requests,json,time
return_data=requests.get("https://club.jd.com/productpage/p-1963535701-s-0-t-1-p-2.html")
#comment1=json.dumps(return_data.text)
comment=json.loads(return_data.text).get('comments')
comment1=json.dumps(comment,sort_keys=True)
comment2=json.loads(comment1)
for i in comment2:
    print "评论时间："i["creationTime"]
    print "用户昵称："+str(i["nickname"])
    print "会员等级："+str(i["userLevelName"])
    print "评论来源："+str(i["userClientShow"])
    print "购买品种："+str(i["referenceName"])
    print "评价："+str(i["content"])
    print '\n'







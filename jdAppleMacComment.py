# coding=utf-8
import requests,json,ast
from pprint import pprint
linlsta='https://club.jd.com/productpage/p-1958407868-s-0-t-1-p-'
linkend='.html'
for j in range(0,248):
    print "正在打印第"+str(j)+"页"
    return_data=requests.get(linlsta+str(j)+linkend).json()
    comment1 = json.dumps(return_data, indent=4, sort_keys=True, separators=(',', ':'), encoding='utf-8',
                          ensure_ascii=False)
    comment = json.loads(comment1)
    comment_list = comment['comments']
    for i in range(0, len(comment['comments'])):
        print comment_list[i]['creationTime']
        print comment_list[i]['id']
        print comment_list[i]['nickname']
        print comment_list[i]['productColor']
        print comment_list[i]['userLevelName']
        print comment_list[i]['userProvince']
        print comment_list[i]['content']
        print "\n"

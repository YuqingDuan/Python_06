#所谓抓包分析，即将网络传输发送与接收的数据包进行抓取的操作。做爬虫时，数据并不一定就在HTML源码中，
#很可能隐藏在一些网址中。所以，我们在抓取某些数据，就需要进行抓包，分析出对应数据所隐藏的网址，然后分析规律并爬取。
#使用Fiddler进行抓包分析：抓包工具很多，Fiddler是其中一种, 在爬虫项目中经常会使用Fiddler进行抓包分析

import urllib.request
import re
import urllib.error

#浏览器伪装技术
headers=("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko")
#构建，配置，安装opener对象
opener=urllib.request.build_opener()
opener.addheaders=[headers]
urllib.request.install_opener(opener)
#首页首条评论id值
commentId="6165793094371986503"
#首页url
url="http://video.coral.qq.com/filmreviewr/c/upcomment/0dfpyvfa7tp0ewe?commentid="+commentId+"&reqnum=3&callback=jQuery1120026430801920245595_1478436999932&_=1478436999935"
#外层for循环遍历所有评论页面(前100页)
for i in range(0, 100):
    #获取首页面的数据
    data=urllib.request.urlopen(url).read().decode()
    #从首页面源码中获取下一页评论的页面id值
    regexNext='"last":"(.*?)"'
    nextId=re.compile(regexNext).findall(data)[0]
    #从首页面源码中获取首页评论的内容, 获取到的结果存储在评论数组中
    regexComment='"content":"(.*?)",'
    commentData=re.compile(patcom).findall(data)
    #内层for循环遍历评论数组中所有评论
    for j in range(0，len(commentData)):
        print("The"+str(i)+str(j)+"-th comment is: ")
        #评论中文Unicode解码
        print(eval('u"'+commentData[j]+'"'))
        #构建下一页的url
        url="http://video.coral.qq.com/filmreviewr/c/upcomment/0dfpyvfa7tp0ewe?commentid="+nextId+"&reqnum=3&callback=jQuery1120026430801920245595_1478436999932&_=1478436999935"
        
    


















#微信爬虫, 所谓微信爬虫，即自动获取微信的相关文章信息的一种爬虫。微信对我们的限制是很多的。
#所以，我们需要采取一些手段解决这些限制，主要包括浏览器伪装，使用代理IP等方式。
#http://weixin.sogou.com/

import re
import urllib.request
import time
import urllib.error

#自定义函数，功能为：使用代理服务器爬一个网址
def use_proxy(proxy_addr, url):
    #建立异常处理机制
    try:
        req=urllib.request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko")
        proxy=urllib.request.ProxyHandler({'http' : proxy_addr})
        opener=urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data=urllib.request.urlopen(req).read()
        return data
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        #若为URLError异常，延时10秒执行
        time.sleep(10)
    except Exception as e:
        print("exception: " + str(e))
        #若为Exception异常，延时1秒执行
        time.sleep(1)


#设置搜索关键词
key="Python"
#设置代理服务器，该代理服务器有可能失效，工作时需要换成新的有效的代理服务器
proxy="127.0.0.1:8888"
#爬多少页
for i in range(0, 10):
    key=urllib.request.quote(key)
    thispageurl="http://weixin.sogou.com/weixin?type=2&query=" + key + "&page=" +str(i)
    #调用自定义函数use_proxy
    thispagedata=use_proxy(proxy, thispageurl)
    print(len(str(thispagedata)))
    pat1='<a href="(.*?)"'
    rs1=re.compile(pat1, re.S).findall(str(thispagedata))
    if(len(rs1)==0):
        print("The (" + str(i) +"-th) page unsuccessful")
        continue
    for j in range(0, len(rs1)):
        thisurl=rs1[j].replace("amp", "")
        file="A:/result/32/the" + str(i) +"-th page and the" + str(j) +"-th article.html"
        #调用自定义函数use_proxy
        thisdata=use_proxy(proxy, thisurl)
        try:
            fh=open(file, "wb")
            fh.write(thisdata)
            fh.close()
            print("The " + str(i) + "-th page and the " + str(j) + "-th article successfully download" )
        except Exception as e:
            print(e)
            print("The " + str(i) + "-th page and the " + str(j) + "-th article failed to download" )








            
        
    

































    
    

import socket, os, time, sys, whois

import re
import subprocess

from auto import three

# ip查询
def ip_check(url):
    print('------------------------------------IP信息搜集-------------------------------------------')
    ip = socket.gethostbyname(url)
    print('IP:'+ip)
    three(ip)
    


# whois查询
def whois_check(url):
    print('-------------------------------------whois查询-------------------------------------------')
    data = whois.whois(url)
    print(data)
    


# CDN判断-利用返回IP条数进行判断
def cdn_check(url):
    print('--------------------------------------CDN判断--------------------------------------------')
    ns = "nslookup " + url
    # data=os.system(ns)
    # print(data) #结果无法读取操作
    data = os.popen(ns, "r").read()
    if data.count(".") > 8:
        print("存在CDN")
    else:
        print("不存在CDN")
    

# 子域名查询
# 1.利用字典记载爆破进行查询
def zym_list_check(url):
    print('-------------------------------------子域名查询-------------------------------------------')
    if(url.find('www')!=-1):
        url = url.replace("www.", "")
        for zym_list in open("./subDomain/SubDomain.txt"):
            zym_list = zym_list.replace("\n", "")
            zym_list_url = zym_list + "." + url
            try:
                ip = socket.gethostbyname(zym_list_url)
                print(zym_list_url + "->" + ip)
                time.sleep(0.1)
            except Exception as e:
                time.sleep(0.1)
    else:
        print('非法查询子域名')





        

if __name__ == '__main__':
    url = sys.argv[1]
    check = sys.argv[2]
    
    if check == "all":
        ip_check(url)
        whois_check(url)
        #port_check(url)
        cdn_check(url)
        #os_check(url)
        zym_list_check(url)

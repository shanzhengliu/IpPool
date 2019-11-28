
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import random
from lxml import etree
import re
import json
import os

import time
class proxey:
    iplist=[];
    # def __init__(self):
        # self.iplist = self.getproxy();
        # print self.iplist

    def get_ip_list_66ip(self):
        url = 'http://www.66ip.cn/areaindex_33/1.html'
        ip_list = [];
        web_data = requests.get(url)
        result =   web_data.text
        html = etree.HTML(result)

        # print web_data.text
        html_ip = html.xpath('//table[@bordercolor="#6699ff"]/tr')


        for i in range(2,len(html_ip)+1,1):
            # print i;
            ip = html.xpath('//table[@bordercolor="#6699ff"]/tr['+str(i)+']/td[1]/text()')

            port = html.xpath('//table[@bordercolor="#6699ff"]/tr[' + str(i) + ']/td[2]/text()')
            if(port[0]!="8080" and port[0]!="808" and port[0]!="443"):
                ip_list.append(ip[0]+":"+port[0])


        # html_port = html.xpath('//div[@class="wlist"]//ul[@class="l2"]//span[2]//li//text()')
        # html_protorl = html.xpath('//div[@class="wlist"]//ul[@class="l2"]//span[4]//li//text()')
        # for i in range(0,len(html_ip),1):
        #     if(html_protorl[i]=="https"):
        #         str = "https://"+html_ip[i]+":"+html_port[i]
        #         ip_list.append(str);
        # print html_ip;
        ip_list = self.cip(ip_list)
        print ip_list
        return ip_list

    def get_ip_list_kuaidaili(self):
        ip_list = [];
        web_data = requests.get("https://www.kuaidaili.com/free/intr/1/")
        html = etree.HTML(web_data.text)

        # print web_data.text
        html_ip = html.xpath('//tbody/tr')
        # print html_ip
        number = 2
        for i in range(3, len(html_ip) + 1, 1):

            ip = html.xpath('//tbody/tr[' + str(i) + ']/td[1]/text()')
            port = html.xpath('//tbody/tr[' + str(i) + ']/td[2]/text()')
            if (port[0] != "8080" and port[0] != "808" and port[0] != "443"):
                ip_list.append(ip[0] + ":" + port[0])
                # print ip[0] + ":" + port[0]
            number += 1;

        ip_list = self.cip(ip_list)
        return ip_list



    def get_random_ip(self,ip_list):
        proxy_list = []

        proxy_ip = random.choice(ip_list)
       # print proxy_list
        proxies = {'http': proxy_ip}

        #print proxies
        return proxies



    def cip(self,ip_list):
        trueip=[]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }
        # print ip_list
        for i in range(0,len(ip_list),1):
            try:

                data =requests.get('http://ip.chinaz.com/getip.aspx?format=json', headers=headers,proxies={'http':ip_list[i]},timeout=1,verify=False)

            except:

                continue
            else:

                if(data.status_code==200):
                    if(re.search("14.147", data.text)==None):
                        # print re.search('14.147', data.text)
                        print ip_list[i]

                        print data.text
                        trueip.append(ip_list[i]);
                        print "succeed";
                    # except:
                    #
                    #     continue
        return  trueip

    # def getproxy(self):
    #     url = 'http://www.66ip.cn/areaindex_33/1.html'
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    #     }
    #
    #     # ip_list = self.get_ip_list_66ip()
    #
    #
    #
    #     return  ip_list


        # test = {"http":"175.16.149.188:8060"};
        # web_data = requests.get("http://ip.chinaz.com/getip.aspx", headers=headers, proxies=proxies,verify=False)
        # print web_data.text;

        # print(proxies['http'])
while(1):
    print "begin"
    a = proxey()
    ipdata = a.get_ip_list_66ip()

    python2json = {}
    python2json["http"]= ipdata


    file_object = open('ipchi.php',"w")

    mystr = "<?php"+"\n"
    mystr = mystr + "echo " + "'"+json.dumps(python2json)+"';"
    file_object.write(mystr)
    file_object.close( )
    print mystr
    time.sleep(180)





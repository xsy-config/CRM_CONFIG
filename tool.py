#!/usr/bin/python
# -*- coding=UTF-8 -*-
import sys
import os
import types  
import urllib2  
import json  
import  re


CONFIG_URL = "https://raw.githubusercontent.com/xsy-config/CRM_CONFIG/master/crm.json"

br ="--------🐻 🐻 🐻 🐻 🐻 🐻 🐻 🐻---------"  #在控制台断行区别的
  
#利用urllib2获取网络数据  
def registerUrl():  
    try:
        data = urllib2.urlopen(CONFIG_URL).read()
        return data  
    except Exception,e:  
        print e  
          
  
#解析从网络上获取的JSON数据      
def praserJsonFile(jsonData):  
    return json.loads(jsonData)  
   
def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text

def replaceFileContent( filePath,oldStr,newStr ):

    if not os.path.isfile(filePath):
        print filePath + '--->>>这个文件文件不存在'
        print br
        sys.exit()
        s_file  = file(filePath,'r+')
        old_str = sys.argv[2]
        new_str = sys.argv[3]
        d_file  = file(filePath+'.tmp','w')
        for line in s_file.readlines():
            d_file.writelines(line.replace(old_str,new_str))
        s_file.close()
        d_file.close()
        os.rename(filePath+'.tmp',filePath)
        print filePath + '--->>>已经替换完成'
        print br




if __name__ == "__main__":


    print 'hahhahha-----'

    os.system('rm package.json')
    os.system('curl -C -  -o package.json https://raw.githubusercontent.com/xsy-config/CRM_CONFIG/master/crm_package.json')
 

    os.system("npm install")
    print br
    data = registerUrl()  
    replaceConfigs = praserJsonFile(data) 
    for replaceConfig in replaceConfigs:       
        replaceFileContent(replaceConfig[0],replaceConfig[1],replaceConfig[2])
    print br
    os.system("pod install")

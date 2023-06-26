#!/usr/bin/env python
# -*- coding: UTF-8 -*-
###
 # 游戏主包，发布到当前渠道
### 
import shutil
import os
import sys
import time
import json
print("start------------>>>>>")
CHANNEL_PATH = "/Users/longsf/workspace/cocos/update/release_update/dir_channel/"
gameMap = [
    {"name":"dragon", "gameid":300},
    {"name": "sevenupdown", "gameid":400},
    {"name": "crash", "gameid":500},
    {"name": "ab", "gameid":600},
    {"name": "slot", "gameid":700}
]
demoChannel = "2001"
#删除目录
def deleteDir(path):
    path=path.strip()
    path=path.rstrip("/")
    isExists=os.path.exists(path)
    if isExists:
        shutil.rmtree(path)
        print("delete dir:"+path)
    else:
        print("dir no exists"+path)

#复制目录
def copyDir(path1,path2):
    print("copy dir:"+path1)
    print("to dir:"+path2)
    shutil.copytree(path1, path2)

#输入渠道号
def inputChannel():
    channel = raw_input('input new channel:')
    # print CHANNEL_PATH+channel
    isExists=os.path.exists(CHANNEL_PATH+"channel_"+channel)
    # print isExists
    if isExists:
        return channel
    else:
        print("input dir not exit")

def reviseBaseVersion(channel_):
    #修改base目录下version 文件下的version.json 里面的渠道为当前渠道号
    path = CHANNEL_PATH + "channel_"+channel_+"/"+"base/version/version.json"
    isExists=os.path.exists(path)
    if isExists:    
        print("update base version File-->"+path)
        # 修改version.json文件中的版本号
        json_all = "a"
        with open(path, 'r') as fr: # 文件路径改成
            json_all = json.load(fr)
            urlPath = str(json_all['url'])
            urlPath = urlPath.replace(demoChannel,str(channel_))
            json_all['url'] = urlPath
        with open(path, 'w+') as fw:
            json.dump(json_all, fw, ensure_ascii=False, indent=4)
            return

def reviseSubGameVersion(channel_):
    #修改base目录下version 文件下的version.json 里面的渠道为当前渠道号
    path = CHANNEL_PATH + "channel_"+channel_+"/"+"gameList"
    gamelist = os.listdir(path)
    for name in gamelist:
        print(name)
        versionFile = path+"/"+name+"/version/version.json"
        isExists=os.path.exists(versionFile)
        print("update game version File-->"+versionFile)
        if isExists:    
            # 修改version.json文件中的版本号
            json_all = "a"
            with open(versionFile, 'r') as fr: # 文件路径改成
                json_all = json.load(fr)
                urlPath = str(json_all['url'])
                urlPath = urlPath.replace(demoChannel,str(channel_))
                json_all['url'] = urlPath
            with open(versionFile, 'w+') as fw:
                json.dump(json_all, fw, ensure_ascii=False, indent=4)
        else:
            print versionFile+"is nil!"
def removeUnlessDir(channel_):
    #先删除base路径下的文件夹
    path = CHANNEL_PATH+"channel_"+channel_ +"/base"
    dirlist = os.listdir(path)
    for name in dirlist:
        if str(name) != "version" and str(name) != "version.txt" :
            print path+"/"+name
            deleteDir(path+"/"+name)
     #先删除gameList路径下的文件夹
    path = CHANNEL_PATH+"channel_"+channel_ +"/gameList"
    dirlist = os.listdir(path)
    for name in dirlist:
        gamepath = path+"/"+name
        gamedirlist = os.listdir(gamepath)
        for mdir in gamedirlist:
            if str(mdir) != "version" and str(mdir) != "version.txt" :
                deleteDir(gamepath+"/"+mdir)

def main():
    # 输入新的渠道
    print("start------------>>>>>")
    channel = inputChannel()
    CURDIR = CHANNEL_PATH+ "channel_"+channel+"/"
    path = CHANNEL_PATH+"channel_"+channel
    print CURDIR
    #修改渠道文件信息
    reviseBaseVersion(channel)
    #修改子游戏渠道文件信息
    reviseSubGameVersion(channel)
    print("end------------>>>>>")

main()
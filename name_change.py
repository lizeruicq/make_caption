import os
import sys

map = {
"EN":".en_US",
"KR":".ko_KR",
"TW":".zh_TW",
"CN":".zh_CN",
"DE":".de_DE",
"FR":".fr_FR",
"TH":".th_TH",
"ID":".id_ID",
"VN":".vi_VN",
"ENSEA": ".en_SEA",
"ENGLB":".en_US"
}

filelist = []
newname = input("请输入修改后的文件名")

def run():
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if (name.split('.')[-1] == 'mp4'):
                # end = name.split('.')[-2].split(" ")[-1]
                # if end in map:
                os.rename(name,newname+map[end]+ ".mp4")
                print(newname +map[end]+ ".mp4")
            if(name.split('.')[-1] == 'srt'):
                end = name.split('.')[-2][-2:]
                if end in map:
                    os.rename(name,newname + map[end] + ".srt")
                    print(newname+map[end]+".srt")

    print("修改完成",end="")

run()

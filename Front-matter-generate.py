# 为内容添加Front-matter

import datetime
import os

import json5


def fm_dev(rpath, tname, oldf = []): # 生成Front-matter
    rpath = rpath.split(os.path.sep)
    tit = "title: " + tname + "\n"
    tmpl = ["---\n", tit, "date: ", "categories:\n", "tags:\n"]
    tmpl = tmpl + oldf + ["---\n"]
    
    tmpl[tmpl.index("date: ")] = "date: " + datetime.date.today().strftime('%Y/%m/%d') + "\n"
    if rpath[0] == '.': tmpl.insert(tmpl.index("categories:\n") + 1, "- Life\n") # 根目录下所有文件处于 Life 分类
    else: tmpl.insert(tmpl.index("categories:\n") + 1,"- " + rpath[0] + "\n")

    """路径中剩下的部分作为标签"""
    if len(rpath) > 1 :
        for i in range(1, len(rpath)):
            tmpl.insert(tmpl.index("tags:\n") + 1,"- " + rpath[i] + "\n")

    if rpath[0] == 'Net-excerpt': tmpl.insert(len(tmpl) - 1, "reprint: true\n") # 主题内自定义设置，转载文章标记

    return tmpl


fapath = os.path.split(os.path.realpath(__file__))[0]
config = json5.load(open('./config.json', 'r', encoding='utf-8'))


for folderName, subfolders, filenames in os.walk(fapath):
    for filename in filenames:
        # 获取前缀（文件名称）
        tname = os.path.splitext(filename)[0]
        if os.path.splitext(filename)[-1][1:] == "md" :

            rpath = os.path.relpath(folderName, fapath) # 获取相对路径
            filepath = rpath + "\\" + filename # 获取文件的相对路径
            # print(filepath) # 测试路径是否正确
            TFile = open(filepath, 'r', encoding='utf-8') # 打开文件(只读)
            conntent = TFile.readlines() # 按行读取
            TFile.close() # 关闭文件
            old_front_matter = []
            date_maked = 0
            if(conntent[0] == "---\n"): # 处理过的
                for i in range(1, len(conntent)-1):
                    line = conntent[i]
                    if (config["remove_blank_lines"] and (line.strip() == "" or line in ['\n','\r\n'])):
                        while(line.strip() == "" or line in ['\n','\r\n']):
                            del conntent[i]
                            line = conntent[i]
                    for fix_content in config["fix_content"]:
                    if (line.startswith()):
                        date_maked = 1
                    
                    if(line == "---\n"):
                        old_front_matter = conntent[:i+1]
                        break
                if(config["make_date"] and not date_maked):
                    old_front_matter.insert(old_front_matter.index("categories:\n"),"date: " + datetime.date.today().strftime('%Y/%m/%d') + "\n")
                
                """生成Fornt-matter并写入文件"""
                conntent = old_front_matter + conntent[i+1:]
                TFile = open(filepath, 'w', encoding='utf-8')
                TFile.writelines(conntent)
                TFile.close()
                # """保留可能手动设置的信息"""
                # oldf = []
                # if "Flagold: true\n" in conntent : oldf = conntent[conntent.index("Flagold: true\n"): i]
                # if "reprint: true\n" in oldf: oldf.remove("reprint: true\n")
                

            else:
                conntent = fm_dev(rpath, tname) + ["\n\n"] + conntent
                TFile = open(filepath, 'w', encoding='utf-8')
                TFile.writelines(conntent)
                TFile.close()
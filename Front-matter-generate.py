# 遍历文件列表为新内容添加Front-matter

import datetime
import os

import json5


def fm_dev(rpath, filename, oldf = []): # 生成Front-matter
    rpath = rpath.split(os.path.sep)
    tit = "title: " + filename + "\n"
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


for folderName, subfolders, full_full_filenames in os.walk(fapath):
    for full_filename in full_full_filenames:
        # 获取前缀（文件名称）
        filename = os.path.splitext(full_filename)[0]
        if os.path.splitext(full_filename)[-1][1:] == "md" :

            rpath = os.path.relpath(folderName, fapath) # 获取相对路径
            filepath = rpath + "\\" + full_filename # 获取文件的相对路径
            # print(filepath) # 测试路径是否正确
            TFile = open(filepath, 'r', encoding='utf-8') # 打开文件(只读)
            conntent = TFile.readlines() # 按行读取
            TFile.close() # 关闭文件
            if(conntent[0] == "---\n"): # 处理过的
                continue
            else:
                conntent = fm_dev(rpath, filename) + ["\n\n"] + conntent
                TFile = open(filepath, 'w', encoding='utf-8')
                TFile.writelines(conntent)
                TFile.close()
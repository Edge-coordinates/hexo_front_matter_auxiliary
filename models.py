def new_fm_dev(current_folder_repath, full_filename):
    """根据相对路径和full_filename获取文件并生成Front-matter并返回。"""
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
    pass

def fm_update():
    pass
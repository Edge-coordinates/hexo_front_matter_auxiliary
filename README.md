---
title: README
date: 2022/10/15
categories:
- Life
tags:
---


# hexo_front_matter_auxiliary
hexo 辅助生成Front-matter


"""
功能
- 根据文件名生成标题
- 根据文件目录生成分类和标签
- 如果文章以`转载`, `zhuanzai`开头，自动加上转载标识
- 保留所有 ===分割号后的自定义分类和标签
- 不为生成过的文件重新生成 & 自定义排除文件夹or文件
"""

"""
---
title: Hello World
categories:
- Diary
tags:
- PS3
- Games
---
"""
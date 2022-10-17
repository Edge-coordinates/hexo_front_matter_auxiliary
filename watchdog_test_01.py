#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import print_function

import logging
import sys
import time

import watchdog.events
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

WATCH_PATH = '../'  # 监控目录


class FileMonitorHandler(FileSystemEventHandler):
    def __init__(self, **kwargs):
        super(FileMonitorHandler, self).__init__(**kwargs)
        # 监控目录 目录下面以device_id为目录存放各自的图片
        self._watch_path = WATCH_PATH

    def on_any_event(self, event):
        if event == watchdog.events.FileCreatedEvent():
            print("fdas")


    # 重写文件改变函数，文件改变都会触发文件夹变化
    # def on_modified(self, event):
    #     if not event.is_directory:  # 文件改变都会触发文件夹变化
    #         file_path = event.src_path
    #         print("文件改变: %s " % file_path)

    # def on_created(self, event):
    #     print('创建了文件夹', event.src_path)

    # def on_moved(self, event):
    #     print("移动了文件", event.src_path)

    # def on_deleted(self, event):
    #     print("删除了文件", event.src_path)



if __name__ == "__main__":
    event_handler = FileMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_PATH,
                      recursive=True)  # recursive递归的
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
    observer.join()

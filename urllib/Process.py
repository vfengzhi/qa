#!/usr/local/lib
# -*- coding: UTF-8 -*-

#############################################
# 1.在循环前定义类的实体， max_steps是总的步数   #
#    process_bar = ShowProcess(max_steps)   #
# 2.显示当前进度                              #
#    for i in range(max_steps + 1):          #
#        process_bar.show_process()          #
#        time.sleep(0.05)                    #
# 3.处理结束后显示消息                         #
#    for i in range(max_steps + 1):          #
#        process_bar.show_process()          #
#        time.sleep(0.05)                    #
#    process_bar.close('done')               #
##############################################

import sys, time

class ShowProcess():
    """

    variablies:
    i  :  current process
    max_steps  :  total number of dealing times
    max_arrow  :  length of process bar


    """
    i = 1 # 当前的处理进度
    max_steps = 0 # 总共需要处理的次数
    max_arrow = 50 #进度条的长度


    def __init__(self, max_steps):
        self.max_steps = max_steps
        self.i = 1

    # result : [>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>]100.00%
    def show_process(self, i = None):
        if i is not None:
            self.i = i
        num_arrow = int(self.i * self.max_arrow / self.max_steps) #计算显示多少个'>'
        num_line = self.max_arrow - num_arrow #计算显示多少个'-'
        percent = self.i * 100.0 / self.max_steps #计算完成进度，格式为xx.xx%
        process_bar = '[' + '>' * num_arrow + '-' * num_line + ']'\
                      + '%.2f' % percent + '%' + '\r' #带输出的字符串，'\r'表示不换行回到最左边
        sys.stdout.write(process_bar) #这两句打印字符到终端
        sys.stdout.flush()
        self.i += 1

    def close(self, words='done'):
        print ''
        print words
        self.i = 1

if __name__=='__main__':
    max_steps = 100

    process_bar = ShowProcess(max_steps)

    for i in range(max_steps):
        process_bar.show_process()
        time.sleep(0.05)
    process_bar.close()
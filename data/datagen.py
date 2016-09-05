#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
处理.conv 文件，变成纯粹的 txt 文件 ，无行头。
'''

import sys
import re
import chardet
import random


reload(sys)
sys.setdefaultencoding("utf-8")

def shifter(seq):
    '''shift a string '''
    ret = ''
    pos = random.randint(1, len(seq) - 1)

    rd = random.randint(0, 2)
    if rd == 0:
        ret = seq[:pos] + seq[pos+1:]
    elif rd == 1:
        ret = seq[:pos] + seq[pos-1:]
    else:
        ret = seq
    
    return ret



if __name__ == "__main__":
    test = [
        u'今天的天气真好',
        u'你是一个我非常敬佩的人',
        u'特朗普如果当选总统的话，世界就会欢天喜地',
        u'不知道你所在的位置能不能看见天安门广场上的五星红旗'
    ]
    for t in test:
        for x in range(10):
            print shifter(t)

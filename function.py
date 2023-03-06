# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 19:45:34 2020

@author: hp
"""

# -* -coding: UTF-8 -* -
# 功能:异或方式对文件进行加密和解密
import os
import datetime
from tkinter import filedialog
import time

def get_current_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return current_time

def xor_encrypt(tips,key):
    ltips=len(tips)
    lkey=len(key)
    secret=[]
    num=0
    for each in tips:
        if num>=lkey:
            num=num%lkey
        secret.append( chr( ord(each)^ord(key[num]) ) )
        num+=1
    rg=''
    for i in secret:
        rg=rg+i
    return rg


def xor_decrypt(secret,key):

    tips = secret

    ltips=len(tips)
    lkey=len(key)
    secret=[]
    num=0
    for each in tips:
        if num>=lkey:
            num=num%lkey

        secret.append( chr( ord(each)^ord(key[num]) ) )
        num+=1

    return "".join( secret )
# 主函数
# 加密
def encrypt(path, password):
    path = path.replace('/', '\\')
    fileFullName = path.split(os.path.sep)  # os.path.sep为操作系统的文件分隔符
    fileName = fileFullName[len(fileFullName) - 1].split(".")[0]
    fileSuffix = fileFullName[len(fileFullName) - 1].split(".")[1]
    fileParent = path[0:len(path) - len(fileFullName[len(fileFullName) - 1])]
    newFileName = "加密_" + fileFullName[len(fileFullName) - 1]
    newFilePath = fileParent + newFileName
    f_read = open(path, "rb")
    f_write = open(newFilePath, "wb")
    count = 0  # 当前密码加密索引
    # 我们采用异或循环加密e
    for now in f_read:  # 通过迭代器逐行访问
        for nowByte in now:  # 通过迭代器逐字符处理
            newByte = nowByte ^ ord(password[count % len(password)])
            count += 1
            f_write.write(bytes([newByte]))

    f_read.close()
    f_write.close()
    return [newFileName,newFilePath]




# 解密（因为我们采取的异或解密，所以其实和加密算法一样）
def decrypt(path, password):
    path = path.replace('/', '\\')
    fileFullName = path.split(os.path.sep)  # os.path.sep为操作系统的文件分隔符
    fileName = fileFullName[len(fileFullName) - 1].split(".")[0]
    fileSuffix = fileFullName[len(fileFullName) - 1].split(".")[1]
    fileParent = path[0:len(path) - len(fileFullName[len(fileFullName) - 1])]
    newFileName = "解密_" + fileFullName[len(fileFullName) - 1]
    newFilePath = fileParent + newFileName
    f_read = open(path, "rb")
    f_write = open(newFilePath, "wb")
    count = 0  # 当前密码加密索引
    # 我们采用异或循环加密
    for now in f_read:  # 通过迭代器逐行访问
        for nowByte in now:  # 通过迭代器逐字符处理
            newByte = nowByte ^ ord(password[count % len(password)])
            count += 1
            f_write.write(bytes([newByte]))

    f_read.close()
    f_write.close()
    return [newFileName, newFilePath]


def openw():
    # 0代表另存为对话框，1代表打开文件对话框
    r = filedialog.askopenfilename(title='打开文件', filetypes=[('Python', '*.py *.pyw'), ('All Files', '*')])
    return r


# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 10:38:41 2020

@author: hp
"""
# from Include.changebasesystem import *
from function import *
import tkinter
# 导入消息对话框子模块
import tkinter.messagebox
from tkinter.messagebox import *
from tkinter import *

import threading
import os
import re
import time


def creatGUI():
    def startencode():
        mw=jentry.get()
        my=mentry.get()
        miw=xor_encrypt(mw,my)

        text.insert(END, "时间："+get_current_time()+"\n操作：加密字符串\n明文："+str(mw)+"\n密钥:"+str(my)+"\n加密密文:"+str(miw)+"\n\n")

    def startoutcode():
        miw=jieentry.get()
        my=ntry.get()
        mw=xor_decrypt(miw,my)
        text.insert(END, "时间："+get_current_time()+"\n操作：加密字符串\n密文："+str(miw)+"\n密钥:"+str(my)+"\n解密明文:"+str(mw)+"\n\n")

    def wjencode():
        top = Tk()
        top.geometry("620x160+200+150")
        top.title('加密文件')
        frmtop = Frame(top)
        frmtop.grid(row=1, column=0)
        frmtop1 = Frame(top)
        frmtop1.grid(row=0, column=0)
        frmtop2 = Frame(top)
        frmtop2.grid(row=2, column=0)
        toptap = Label(frmtop1, text='加密文件', font=("微软雅黑", 20), fg='red')
        toptap.grid(row=0, column=0)
        tgoptap = Label(frmtop, text='密钥(数字)：')
        tgoptap.grid(row=1, column=0)
        tgentry = Entry(frmtop, text='', width=70, cursor='mouse', insertbackground="red",
                       highlightcolor="red", highlightbackground="green")
        tgentry.grid(row=1, column=1)
        tloptap = Label(frmtop, text='文件路径：')
        tloptap.grid(row=2, column=0)
        tentry=Entry(frmtop, text='', width=70, cursor='mouse', insertbackground="red",
                   highlightcolor="red", highlightbackground="green")
        tentry.grid(row=2, column=1)
        thebutton = Button(frmtop, text="选择文件", bg="lightblue", width=53,
                            command=lambda: thread_it(openlj()))
        thebutton.grid(row=3, column=1,padx=10)
        lastbutton = Button(frmtop, text="开始加密", bg="lightblue", width=53,
                            command=lambda: thread_it(encode()))
        lastbutton.grid(row=4, column=1,padx=10)

        def openlj():
            lj=openw()
            tentry.insert(END, lj)
        def encode():
            path=tentry.get()
            password=tgentry.get()
            geti=encrypt(path, password)
            text.insert(END,
                        "时间：" + get_current_time() + "\n操作：加密文件\n文件路径：" + str(path) + "\n密钥:" + str(password) + "\n加密文件:" + str(
                            geti[0]) + "\n文件路径:" + str(geti[1])+"\n\n")


    def wjoutcode():
        top = Tk()
        top.geometry("620x160+200+150")
        top.title('解密文件')
        frmtop = Frame(top)
        frmtop.grid(row=1, column=0)
        frmtop1 = Frame(top)
        frmtop1.grid(row=0, column=0)
        frmtop2 = Frame(top)
        frmtop2.grid(row=2, column=0)
        toptap = Label(frmtop1, text='解密文件', font=("微软雅黑", 20), fg='red')
        toptap.grid(row=0, column=0)
        tgoptap = Label(frmtop, text='密钥(数字)：')
        tgoptap.grid(row=1, column=0)
        tgentry = Entry(frmtop, text='', width=70, cursor='mouse', insertbackground="red",
                        highlightcolor="red", highlightbackground="green")
        tgentry.grid(row=1, column=1)
        tloptap = Label(frmtop, text='文件路径：')
        tloptap.grid(row=2, column=0)
        tentry = Entry(frmtop, text='', width=70, cursor='mouse', insertbackground="red",
                       highlightcolor="red", highlightbackground="green")
        tentry.grid(row=2, column=1)
        thebutton = Button(frmtop, text="选择文件", bg="lightblue", width=53,
                           command=lambda: thread_it(openlj()))
        thebutton.grid(row=3, column=1, padx=10)
        lastbutton = Button(frmtop, text="开始解密", bg="lightblue", width=53,
                            command=lambda: thread_it(encode()))
        lastbutton.grid(row=4, column=1, padx=10)

        def openlj():
            lj = openw()
            tentry.insert(END, lj)

        def encode():
            path = tentry.get()
            password = tgentry.get()
            geti = decrypt(path, password)
            text.insert(END,
                        "时间：" + get_current_time() + "\n操作：解密文件\n文件路径：" + str(path) + "\n密钥:" + str(
                            password) + "\n解密文件:" + str(
                            geti[0]) + "\n文件路径:" + str(geti[1]) + "\n\n")

    def thread_it(func, *args):
        '''将函数打包进线程'''
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)
        t.start()
    master = Tk()
    master.geometry("900x550+100+100")
    master.title("异或加密算法实现--3118005433")

    frmb = Frame(master)
    frmb.grid(row=0, column=0, pady=10)
    frmbutton = Frame(master, borderwidth=2, relief="ridge")
    frmbutton.grid(row=1, column=0, padx=5, pady=10)
    frmn = Frame(master,borderwidth=2, relief="ridge")
    frmn.grid(row=2, column=0)
    frmnt = Frame(master,borderwidth=2, relief="ridge")
    frmnt.grid(row=3, column=0,pady=10)
    blabel = Label(frmb, text='      异或加密算法实现', justify=LEFT, font=("微软雅黑", 21), fg='blue')
    blabel.grid(row=0, column=0)
    jlabel = Label(frmbutton, text='加密信息(字符串)：')
    jlabel.grid(row=0, column=1, padx=15, pady=5)
    jentry = Entry(frmbutton, text='请输入需要加密的信息', width=29, cursor='mouse', insertbackground="red",
                   highlightcolor="red", highlightbackground="black")
    # jentry.insert(END, "请输入16进制的16位明文")
    jentry.grid(row=0, column=2, padx=15, pady=5)
    mlabel = Label(frmbutton, text='密钥(数字)：')
    mlabel.grid(row=0, column=3, padx=10, pady=5)
    mentry = Entry(frmbutton, text='请输入密钥', width=30, cursor='mouse', insertbackground="red",
                   highlightcolor="red", highlightbackground="green")
    # mentry.insert(END, "请输入16进制的16位密钥")

    mentry.grid(row=0, column=4, padx=10, pady=5)
    thebutton1 = Button(frmbutton, text="加密", bg="lightblue", width=20,
                        command=lambda: thread_it(startencode()))
    thebutton1.grid(row=0, column=5, pady=5)

    jielabel = Label(frmbutton, text='解密信息(字符串)：')
    jielabel.grid(row=1, column=1, padx=10, pady=5)
    jieentry = Entry(frmbutton, text='请输入需要解密的信息', width=29, cursor='mouse', insertbackground="red",
                   highlightcolor="red", highlightbackground="black")
    jieentry.grid(row=1, column=2, padx=10, pady=5)
    malabel = Label(frmbutton, text='密钥(数字)：')
    malabel.grid(row=1, column=3, padx=15, pady=5)
    ntry = Entry(frmbutton, text='请输入密钥', width=30, cursor='mouse', insertbackground="red",
                   highlightcolor="red", highlightbackground="green")
    ntry.grid(row=1, column=4, padx=15, pady=5)
    thebutton2 = Button(frmbutton, text="解密", bg="lightblue", width=20,
                        command=lambda: thread_it(startoutcode()))
    thebutton2.grid(row=1, column=5, pady=5)

    wjlabel = Label(frmn, text='文件加密/解密：')
    wjlabel.grid(row=2, column=1, padx=95, pady=5)
    thebutton3 = Button(frmn, text="加密文件", bg="lightblue", width=20,
                        command=lambda: thread_it(wjencode()))
    thebutton3.grid(row=2, column=2, padx=35,pady=5)
    thebutton4 = Button(frmn, text="解密文件", bg="lightblue", width=20,
                        command=lambda: thread_it(wjoutcode()))
    thebutton4.grid(row=2, column=3,padx=110, pady=5)

    text = Text(frmnt, width=124, height=23)
    text.grid(row=1, column=3)

    master.mainloop()

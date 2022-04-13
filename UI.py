# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 23:10:22 2022

@author: 77469
"""

from tkinter import *
import time
from PIL import Image, ImageTk
import post
import ttkthemes
import tkinter.ttk as ttk
# style = Style(theme='darkly')

def main():
        
    def sendMsg():
        try:
            strMsg = "You:" + time.strftime("%Y-%m-%d %H:%M",time.localtime())+ '\n'
            txtMsgList.insert(END, strMsg, 'greencolor')
            txtMsgList.insert(END, txtMsg.get('0.0', END))
            text = txtMsg.get('0.0', END)
            txtMsg.delete('0.0', END)
            txtMsgList.see(END)
            text = post.chatbot_text(text) + '\n'
               
            strMsg = "Chatbot:" + time.strftime("%Y-%m-%d %H:%M",time.localtime())+ '\n'
            txtMsgList.insert(END, strMsg, 'greencolor')
            txtMsgList.insert(END, text)
            txtMsgList.see(END)
            txtMsg.delete('0.0', END)
        except:
            text = "Sorry I didn't get it, can you say it in another way?" + '\n'
            strMsg = "Chatbot:" + time.strftime("%Y-%m-%d %H:%M",time.localtime())+ '\n'
            txtMsgList.insert(END, strMsg, 'greencolor')
            txtMsgList.insert(END, text)
            txtMsgList.see(END)
            txtMsg.delete('0.0', END)
            post.speak_text(text) 
    
    def sendMsg_voice():
        try:
            strMsg = "You:" + time.strftime("%Y-%m-%d %H:%M",time.localtime())+ '\n'
            txtMsgList.insert(END, strMsg, 'greencolor')
            text, tts_text = post.chatbot_speech()
            text += '\n'
            tts_text += '\n'
            txtMsgList.insert(END, text)
            txtMsg.delete('0.0', END)
            txtMsgList.see(END)
               
            strMsg = "Chatbot:" + time.strftime("%Y-%m-%d %H:%M",time.localtime())+ '\n'
            txtMsgList.insert(END, strMsg, 'greencolor')
            txtMsgList.insert(END, tts_text)
            txtMsgList.see(END)
            txtMsg.delete('0.0', END)
        except:
            text = "I'm sorry I didn't catch it. Can you say it again?" + '\n'
            strMsg = "Chatbot:" + time.strftime("%Y-%m-%d %H:%M",time.localtime())+ '\n'
            txtMsgList.insert(END, strMsg, 'greencolor')
            txtMsgList.insert(END, text)
            txtMsgList.see(END)
            txtMsg.delete('0.0', END)
            post.speak_text(text)
            
    def cancelMsg():
        txtMsg.delete('0.0', END)

    def sendMsgEvent(event):
        if event.keysym =='Up':
            sendMsg()
    #create window
    window = ttkthemes.ThemedTk(theme="plastic")
    # window = ttkthemes.ThemedTk(theme="ubuntu")
    window.title('Weather Query Voice Assistant')
    # style = ttkthemes.ThemedStyle(window) 
    # style.set_theme("black")   



    frmLT = ttk.Frame(width = 565, height = 320)
    frmLC = ttk.Frame(width = 565, height = 145)
    frmLB = ttk.Frame(width = 565, height = 30)
    frmRT = ttk.Frame(width = 380, height = 500)

    txtMsgList = Text(frmLT)
    txtMsgList.tag_config('greencolor',foreground = '#008C00')

    txtMsg = Text(frmLC)
    txtMsg.bind("<KeyPress-Up>", sendMsgEvent)
    
    btnSend = ttk.Button(frmLB, text = 'Send', width = 9, command = sendMsg)
    imgBtn = Image.open("test.png")
    imgBtn = ImageTk.PhotoImage(imgBtn)

    btnSpeak = ttk.Button(frmLB, image = imgBtn, text = 'Voice', width = 8, command = sendMsg_voice, compound = LEFT)
    btnCancel = ttk.Button(frmLB, text = 'Cancel', width = 9, command = cancelMsg)
    imgInfo = PhotoImage(file = "chatbot.png")
    lblImage = Label(frmRT, image = imgInfo)
    
    lblImage.image = imgInfo

    frmLT.grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 3)
    frmLC.grid(row = 1, column = 0, columnspan = 2, padx = 1, pady = 3)
    frmLB.grid(row = 2, column = 0, columnspan = 2)
    frmRT.grid(row = 0, column = 2, rowspan = 3, padx =2, pady = 3)

    frmLT.grid_propagate(0)
    frmLC.grid_propagate(0)
    frmLB.grid_propagate(0)
    frmRT.grid_propagate(0)

    btnSend.grid(row = 2, column = 0)
    # btnSpeak.grid(row = 2, column = 1)
    btnSpeak.place(x=475, y = 0)
    btnCancel.grid(row = 2, column = 2)
    lblImage.grid()
    txtMsgList.grid()
    txtMsg.grid()

    window.mainloop()

if  __name__ == "__main__":
    main()
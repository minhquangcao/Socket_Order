from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import os
from tkinter import Tk, W, E
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Button, Entry
from tkinter import ttk
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk,Image
from tkinter.filedialog import asksaveasfile
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import zlib
from PIL import Image
from PIL import Image
import requests
from io import BytesIO

def KeystrokeMain(client):
		logger = ''
		Stroke = Tk()
		Stroke.title("Keystroke")  
		Stroke.geometry("410x320")
		Stroke.configure(bg = 'white')
		frame_stroke = Frame(Stroke, bg = "#FFEFDB", padx=20, pady = 20, borderwidth=5)
		frame_stroke.grid(row=1,column=0)
		tab = Text(Stroke, width = 50, heigh = 15)
		tab.grid(row = 1, column = 0, columnspan= 4)
		PrsHook = False
		PrsUnhook = False

		def ReceiveHook(client):
			data = client.recv(1024).decode("utf-8")
			string = data
			client.sendall(bytes(data,"utf-8"))  
			return string
			return size, string

		def Hookkey():
			nonlocal PrsHook, PrsUnhook
			if PrsHook == True: return
			PrsHook = True
			PrsUnhook = False
			client.sendall(bytes("HookKey","utf-8"))
			checkdata = client.recv(1024).decode("utf-8")

		def Unhookkey():
			nonlocal logger, PrsUnhook, PrsHook
			if PrsHook == True:
				client.sendall(bytes("UnhookKey","utf-8"))    
				logger = ReceiveHook(client)
				client.sendall(bytes(logger,"utf-8")) 
				PrsUnhook = True
				PrsHook = False

		def Printkey():
			nonlocal logger, PrsUnhook, PrsHook
			if PrsUnhook == False: 
				client.sendall(bytes("UnhookKey","utf-8"))
				logger = ReceiveHook(client)
			tab.delete(1.0, END)
			tab.insert(1.0, logger)
			PrsUnhook = True
			PrsHook = False

		def Deletekey():
			tab.delete(1.0,END)
					    
		hook = Button(Stroke, text = "Hook", font = "Helvetica 10 bold",bg = "#FFDEAD", padx = 25, pady = 20, command = Hookkey).grid(row = 2,column = 0)
		unhook = Button(Stroke, text = "Unhook",font = "Helvetica 10 bold", bg = "#EECFA1", padx = 25, pady = 20, command = Unhookkey).grid(row = 2,column = 1) 
		prs = Button(Stroke, text = "In ph??m",font = "Helvetica 10 bold",bg = "#CDB38B", padx = 25, pady = 20,command = Printkey).grid(row = 2,column = 2)
		delete = Button(Stroke, text = "X??a", font = "Helvetica 10 bold", bg = "#8B795E",padx = 25, pady = 20,command = Deletekey).grid(row = 2,column = 3)


def Registry(client): 
	OPTION1 = [
            "Get value",
            "Set value",
            "Delete value",
            "Create key",
            "Delete key"
        	]

	OPTION2 = [
    		"String",
            "Binary",
            "DWORD",
            "QWORD",
            "Multi-string",
            "Expandable String"
        	]
	Register = Tk()
	Register.geometry("480x450")
	Register.title("Registry")
	Register.configure(bg = '#8B6969')
	pathing = StringVar()
	linking = ''
	browser = Entry(Register,bg = "#8B658B", width=55)
	browser.grid(row=0, column=0, padx = 10)
	regis = Text(Register,bg = "#8B658B", height = 7, width = 41)
	regis.grid(row=2, column=0, pady=10)

	def Browse():
		nonlocal pathing, linking
		fname = filedialog.askopenfilename()
		pathing.set(fname)
		browser.insert(0, fname)
		linking = browser.get()
		fileopen = open(linking,'r')
		line = fileopen.read()
		regis.insert(1.0,line)
	ButtonBrowse = Button(Register, text="Browser", font = "Helvetica 10 bold",bg = "#EEB4B4", activebackground='#F4A460',command=Browse, padx = 28)
	ButtonBrowse.grid(row=0, column=1, padx = 10)

	def RegContent():
		nonlocal regis
		client.sendall(bytes("SendingReg", "utf-8"))
		checkdata = client.recv(1024).decode("utf-8") 
		line = regis.get(1.0,END)
		client.sendall(bytes(line,"utf-8"))
		checkdata = client.recv(1024).decode("utf-8")
	ContentButton = Button(Register, text="G???i n???i dung", font = "Helvetica 10 bold",bg = "#EEB4B4",activebackground='#F4A460',height = 4, command = RegContent, padx = 15, pady = 28)
	ContentButton.grid(row=2, column=1, padx = 10)

	SecondFrame = LabelFrame(Register, text="S???a gi?? tr??? tr???c ti???p")
	SecondFrame.grid(row=3, columnspan = 2, padx = 0, pady = 0)

	def changeFunction(event):
		if getFunction.get() == "Get value":
			Name.grid_forget()
			Value.grid_forget()
			infomation.grid_forget()
			Name.grid(row=2, column=0, sticky = W)

		elif getFunction.get() == "Set value":
			Name.grid_forget()
			Value.grid_forget()
			infomation.grid_forget()
			Name.grid(row=2, column=0, sticky = W)
			Value.grid(row=2, column=0, sticky = N)
			infomation.grid(row=2, column=0, sticky = E, padx=4)       
		elif getFunction.get() == "Delete value":
			Name.grid_forget()
			Value.grid_forget()
			infomation.grid_forget()
			Name.grid(row=2, column=0, sticky = W)

		elif getFunction.get() == "Create key":
			Name.grid_forget()
			Value.grid_forget()
			infomation.grid_forget()

		elif getFunction.get() == "Delete key":
			Name.grid_forget()
			Value.grid_forget()
			infomation.grid_forget()

    # S???a gi?? tr??? tr???c ti???p
	getFunction = ttk.Combobox(SecondFrame, value=OPTION1)
	getFunction.insert(0, "Ch???n ch???c n??ng")
	getFunction.bind("<<ComboboxSelected>>", changeFunction)
	getFunction.grid(row=0,column=0,ipadx=160, sticky=W)
	path = Entry(SecondFrame, width=77)
	path.insert(0, "???????ng d???n")
	path.grid(row=1, column=0, pady=10)
	Name = Entry(SecondFrame, width = 24)
	Name.insert(0, "Name value")
	Name.grid(row=2, column=0, sticky = W)
	Value = Entry(SecondFrame, width = 25)
	Value.insert(0, "Value")
	Value.grid(row=2, column=0, sticky = N)
	infomation = ttk.Combobox(SecondFrame, value=OPTION2)
	infomation.insert(0, "Ki???u d??? li???u")
	infomation.grid(row=2, column=0, sticky = E, padx=4)
	Thongbao = Frame(SecondFrame)
	Thongbao.grid(row=3, column=0)
	Noti = Canvas(Thongbao, height=150, width =440)
	Noti.pack(side=LEFT, fill=BOTH, expand=1)
	Lenh = Frame(Noti)
	Noti.create_window((0,0), window=Lenh, anchor="nw")

	def ButtonGui():
		if getFunction.get() == "Get value":
			client.sendall(bytes("GettingValueReg","utf-8"))
			NameVal = Name.get()
			Links = path.get()
			client.sendall(bytes(NameVal,"utf-8"))
			checkdata = client.recv(1024).decode("utf-8")
			client.sendall(bytes(Links,"utf-8"))
			checkdata = client.recv(1024).decode("utf-8") 
			data = client.recv(1024).decode("utf-8")
			client.sendall(bytes("Da nhan", "utf-8"))

			if data == "Khong tim thay":
				chuoi = Label(Lenh, text="Kh??ng t??m th???y")
				chuoi.pack(side = BOTTOM)
			else: 
				chuoi = Label(Lenh, text=data)
				chuoi.pack(side = BOTTOM)

		elif getFunction.get() == "Set value":
			client.sendall(bytes("SettingValueReg","utf-8"))
			NameVal = Name.get()
			Links = path.get()
			client.sendall(bytes(NameVal,"utf-8"))
			checkdata = client.recv(1024).decode("utf-8")
			client.sendall(bytes(Links,"utf-8"))
			checkdata = client.recv(1024).decode("utf-8")	
			Kieudulieu = infomation.get()
			client.sendall(bytes(Kieudulieu, "utf-8"))
			checkdata = client.recv(1024).decode("utf-8")
			values = Value.get()
			client.sendall(bytes(values,"utf-8"))
			checkdata = client.recv(1024).decode("utf-8")

			status = client.recv(1024).decode("utf-8")
			print("status")
			client.sendall(bytes("Da nhan", "utf-8"))
			if status == "succeed":
				chuoi = Label(Lenh, text="Set gi?? tr??? th??nh c??ng")
				chuoi.pack(side = BOTTOM)
			elif status == "Sai duong dan":
				chuoi = Label(Lenh, text="Sai ???????ng d???n")
				chuoi.pack(side = BOTTOM)
			else:   
				chuoi = Label(Lenh, text="L???i gi?? tr???")
				chuoi.pack(side = BOTTOM)

		elif getFunction.get() == "Create key":
			client.sendall(bytes("CreatingKey","utf-8"))
			Links = path.get()
			client.sendall(bytes(Links,"utf-8"))
			checkdata = client.recv(1024).decode("utf-8")
			data = client.recv(1024).decode("utf-8")
			client.sendall(bytes("Da nhan","utf-8"))
			if data == "Da tao thanh cong":
				chuoi = Label(Lenh, text="???? t???o th??nh c??ng")
				chuoi.pack(side = BOTTOM)          
			else: 
				chuoi = Label(Lenh, text="Sai ???????ng d???n")
				chuoi.pack(side = BOTTOM)

		elif getFunction.get() == "Delete value":
			client.sendall(bytes("DeletingValueReg","utf-8"))
			Links = path.get()
			NameVal = Name.get()
			client.sendall(bytes(Links,"utf-8"))
			checkdata = client.recv(1024).decode("utf-8")
			client.sendall(bytes(NameVal,"utf-8"))
			checkdata = client.recv(1024).decode("utf-8")
			client.sendall(bytes("Gui noi dung","utf-8"))            
			data = client.recv(1024).decode("utf-8")
			chuoi = Label(Lenh, text=data)
			chuoi.pack(side = BOTTOM)
			client.sendall(bytes("In thanh cong","utf-8"))

		elif getFunction.get() == "Create key":
			client.sendall(bytes("CreatingKey","utf-8"))
			Links = path.get()
			client.sendall(bytes(Links,"utf-8"))
			checkdata = client.recv(1024).decode("utf-8")
			data = client.recv(1024).decode("utf-8")
			client.sendall(bytes("Da nhan","utf-8"))
			chuoi = Label(Lenh, text=data)
			chuoi.pack(side = BOTTOM)        

		elif getFunction.get() == "Delete key":
			client.sendall(bytes("DeletingKey","utf-8"))
			Links = path.get()
			client.sendall(bytes(Links,"utf-8"))
			checkdata = client.recv(1024).decode("utf-8")
			data = client.recv(1024).decode("utf-8")
			client.sendall(bytes("Da nhan","utf-8"))
			if data == "Da xoa thanh cong":
				chuoi = Label(Lenh, text="???? xo?? th??nh c??ng")
				chuoi.pack(side = BOTTOM)          
			else: 
				chuoi = Label(Lenh, text="Sai ???????ng d???n")
				chuoi.pack(side = BOTTOM)                
	def ButtonXoa():
		for widget in Lenh.winfo_children(): widget.destroy()

	BelowButton = Frame(SecondFrame)
	send = Button(BelowButton, text="G???i",activebackground='#8B7D7B',font = "Helvetica 10 bold",bg = "#BC8F8F", command = ButtonGui)
	send.grid(row=0, column=0, ipadx = 35)
	delete = Button(BelowButton, text="Xo??",activebackground='#8B7D7B',font = "Helvetica 10 bold",bg = "#BC8F8F", command = ButtonXoa)
	delete.grid(row=0, column=1, ipadx = 35)
	BelowButton.grid(sticky=S)
	Register.mainloop()


class GUI:

	def __init__(self):
		
		self.Window = Tk()
		self.Window.withdraw()
		self.Window.configure(bg="#FFFAF0")
		# login window
		self.login = Toplevel()
		self.login.configure(bg = "#FFFAF0")
		# set the title
		self.login.title("User")
		self.login.resizable(width = False,height = False)
		self.login.configure(width = 600,height = 300)
		# create a Label
		self.pls = Label(self.login,text = "Please input IP Address to continue", bg ="#FFFAF0", justify = CENTER,font = "Helvetica 14 bold")
		self.pls.place(relheight = 0.15,relx = 0.2,rely = 0.07)
		
		# create a entry box for
		# tying the message
		Id = StringVar()
		Id.set("Nh???p ID")
		self.entryName = Entry(self.login, textvariable = Id, font = "Helvetica 14")
		self.entryName.place(relwidth = 0.4,relheight = 0.1,relx = 0.35,rely = 0.2)
		
#		# set the focus of the curser
		self.entryName.focus()
#		# create a Continue Button
#		# along with action
		self.go = Button(self.login,text = "CONTINUE",bg = "#FFE4C4",font = "Helvetica 14 bold",command = lambda: self.goAhead(self.entryName.get()), bd = 5, activebackground='#F4A460')
		
		self.go.place(relx = 0.4,rely = 0.55)
		self.Window.mainloop()


	def shutdown(self, client):
		try:
			client.send(bytes("Shutdown",'utf-8'))
		except:
			messagebox.showinfo(" ", "L???i k???t n???i ")
	
	def takepicture(self, client): #Ch???p m??n h??nh
		self.Screenshot = Toplevel()
		self.Screenshot.title("PrintScreen")
		self.Screenshot.configure(bg = "#C0C0C0")
		def ReceivePicture(): #Nh???n ???nh t??? server
			try:
				client.sendall(bytes("TakePicture","utf-8"))
			except:
				messagebox.showinfo(" ", "L???i k???t n???i ")
				self.Screenshot.destroy()
			self.file = open("name.png", 'wb')
			self.data = client.recv(40960000)
			self.file.write(self.data)
			self.img = ImageTk.PhotoImage(Image.open("name.png"))     
			self.canvas.create_image(0,0, anchor=NW, image=self.img)
			self.file.close()

		def SavePicture(): #L??u ???nh
			self.myScreenShot = open("name.png",'rb')
			self.data = self.myScreenShot.read()
			self.fname = filedialog.asksaveasfilename(title=u'Save file', filetypes=[("PNG", ".png")])
			self.myScreenShot.close()

			self.file = open(str(self.fname) + '.png','wb')
			self.file.write(self.data)
			self.file.close()

		self.canvas = Canvas(self.Screenshot, bg = "white", width = 850, height = 500) #canvas      
		self.canvas.grid(row = 0,column = 0)    
		self.cap = Button(self.Screenshot,text="Ch???p", bg = "#008080", font = "Helvetica 10 bold",width=105,height=3,borderwidth=5,command = ReceivePicture, bd = 5, activebackground='#F4A460') #N??t ch???p h??nh
		self.cap.grid(row=1,column=0)
		self.Save = Button(self.Screenshot,text="L??u",bg = "#FFCC99",font = "Helvetica 10 bold",width=10,height=30,borderwidth=5,command=SavePicture, bd = 5, activebackground='#F4A460')#N??t luu ???nh
		self.Save.grid(row=0, column = 1)
		self.Screenshot.mainloop()

	def apprunning(self, client):
		self.app = Tk()
		self.app.title("App Running")
		self.app.configure (bg = "white")
		
		def XoaTask():
			self.frame_app.destroy()
		def WatchTask():
			global frame_app
			global PORT
			PORT = 5656
			self.length = 0 #Danh s??ch c??c app ??ang ch???y
			self.ID = [''] * 100 #M???ng l??u ID c???a app
			self.Name = [''] * 100 #L??u t??n app
			self.Thread = [''] * 100 #l??u lu???ng
			try:
				client.sendall(bytes("AppRunning","utf-8"))
			except:
				messagebox.showinfo("Warning!", "L???i k???t n???i ")
				self.app.destroy()

			#Receive data
			try:
				self.length = client.recv(1024).decode("utf-8")
				self.length = int(self.length)
				for i in range(self.length):
					self.data = client.recv(1024).decode("utf-8")
					self.ID[i] = self.data
					client.sendall(bytes(self.data,"utf-8"))

				for i in range(self.length):
					self.data = client.recv(1024).decode("utf-8")
					self.Name[i] = self.data
					client.sendall(bytes(self.data,"utf-8"))

				for i in range(self.length):
					self.data = client.recv(1024).decode("utf-8")
					self.Thread[i] = self.data
					client.sendall(bytes(self.data,"utf-8"))
			except:
				box = messagebox.showinfo("!Warning", "L???i k???t n???i ")

			self.frame_app = Frame(self.app, bg = "white", padx=20, pady = 20, borderwidth=5)
			self.frame_app.grid(row=1,columnspan=5,padx=20)
			from tkinter import ttk

			self.scrollbar = Scrollbar(self.frame_app)
			self.scrollbar.pack(side=RIGHT,fill=Y)
			self.mybar = ttk.Treeview(self.frame_app, yscrollcommand=self.scrollbar.set)
			self.mybar.pack()
			self.scrollbar.config(command=self.mybar.yview)

			self.mybar['columns'] = ("1","2") 
			self.mybar.column("#0", anchor=CENTER, width =200,minwidth=25)
			self.mybar.column("1", anchor=CENTER, width=100)
			self.mybar.column("2", anchor=CENTER, width=100)

			self.mybar.heading("#0", text="App Name", anchor=W)
			self.mybar.heading("1",text = "ID", anchor=CENTER)
			self.mybar.heading("2", text = "Counting threading", anchor=CENTER)
			for i in range(self.length):
				self.mybar.insert(parent='', index='end',iid=0+i, text = self.Name[i], values=(self.ID[i],self.Thread[i]))

		def KillWindow():
			self.KillTask = Tk()
			self.KillTask.geometry("300x50")
			self.KillTask.title("Kill")
			self.EnterName = Entry(self.KillTask, width = 35)
			self.EnterName.grid(row=0, column=0, columnspan = 3, padx = 5, pady = 5 )
			self.EnterName.insert(END,"Nh???p t??n")

			def PressKill():
				self.AppName = self.EnterName.get()
				client.sendall(bytes("KillTask","utf-8"))
				try:
					client.sendall(bytes(self.AppName,"utf-8"))
					self.checkdata = client.recv(1024).decode("utf-8")
					if (self.checkdata == "Da xoa tac vu"):
						messagebox.showinfo("", "???? di???t ch????ng tr??nh")
					else:
						messagebox.showinfo("", "Kh??ng t??m th???y ch????ng tr??nh")
				except:
					messagebox.showinfo("", "Kh??ng t??m th???y ch????ng tr??nh")

			KillButton = Button(self.KillTask, text = "Kill", bg = "#FFE4E1",font = "Helvetica 10 bold",padx = 20, command = PressKill, bd = 5, activebackground='#F4A460').grid(row=0, column=4, padx=5, pady=5)

		def StartTask():
			self.StartTask = Tk()
			self.StartTask.geometry("300x50")
			self.StartTask.title("Start")

			self.EnterName = Entry(self.StartTask, width = 35)
			self.EnterName.grid(row = 0, column = 0, columnspan = 3, padx = 5, pady = 5)
			self.EnterName.insert(END,"Nh???p T??n")

			def PressStart():
				self.Name = self.EnterName.get()
				client.sendall(bytes("OpenTask","utf-8"))
				try:
					client.sendall(bytes(self.Name,"utf-8"))
					self.checkdata = client.recv(1024).decode("utf-8")
					if (self.checkdata == "Da mo"):
						messagebox.showinfo("", "Ch????ng tr??nh ???? b???t")
					else:
						messagebox.showinfo("", "Kh??ng t??m th???y ch????ng tr??nh")
				except:
					messagebox.showinfo("", "Kh??ng t??m th???y ch????ng tr??nh")

			StartButton = Button(self.StartTask, text = "Start",bg = "#FFE4E1",font = "Helvetica 10 bold", padx = 20, command = PressStart, bd = 5, activebackground='#F4A460').grid(row=0, column=4, padx=5, pady=5)

		Kill = Button( self.app, text = "Kill",bg = "#00FFFF",font = "Helvetica 10 bold", padx = 30,  pady = 20, command= KillWindow, bd = 5, activebackground='#F4A460').grid(row = 0, column = 0, padx = 10)
		Watch = Button(self.app, text = "Xem",bg = "#00EEEE",font = "Helvetica 10 bold", padx = 30,  pady = 20, command = WatchTask, bd = 5, activebackground='#F4A460').grid(row = 0, column = 1, padx = 10)
		Xoa = Button(self.app, text =  "X??a",bg = "#00CDCD", font = "Helvetica 10 bold",padx = 30, pady = 20, command = XoaTask, bd = 5, activebackground='#F4A460').grid(row = 0, column = 2, padx = 10)
		Start = Button(self.app, text="Start", bg = "#008B8B", font = "Helvetica 10 bold",padx = 30, pady = 20, command = StartTask, bd = 5, activebackground='#F4A460').grid(row = 0, column = 3, padx = 10)

	def processrunning(self, client):
		try:
			self.process = Tk()
			self.process.configure(bg = "#FFFAF0")
			self.process.title("Process Running")
			
			def XoaTask():
				self.frame_process.destroy()

			def WatchTask():
				global frame_process
				global PORT
				PORT = 5656
				self.length = 0
				self.ID = [''] * 100000
				self.Name = [''] * 100000
				self.Thread = [''] * 100000
				try:
					client.sendall(bytes("ProcessRunning","utf-8"))
				except:
					messagebox.showinfo("!Warning", "L???i k???t n???i ")
					self.process.destroy()

				#Receive data
				try:
					self.length = client.recv(1024).decode("utf-8")
					self.length = int(self.length)
					for i in range(self.length):
						self.data = client.recv(1024).decode("utf-8")
						self.ID[i] = self.data
						client.sendall(bytes(self.data,"utf-8"))

					for i in range(self.length):
						self.data = client.recv(1024).decode("utf-8")
						self.Name[i] = self.data
						client.sendall(bytes(self.data,"utf-8"))

					for i in range(self.length):
						self.data = client.recv(1024).decode("utf-8")
						self.Thread[i] = self.data
						client.sendall(bytes(self.data,"utf-8"))
				except:
					box = messagebox.showinfo("!Warning", "L???i k???t n???i ")

				self.frame_process = Frame(self.process, bg = "white",padx=20, pady = 20, borderwidth=5)
				self.frame_process.grid(row=1,columnspan=5,padx=20)
				from tkinter import ttk

				self.scrollbar = Scrollbar(self.frame_process)
				self.scrollbar.pack(side=RIGHT,fill=Y)
				self.mybar = ttk.Treeview(self.frame_process, yscrollcommand=self.scrollbar.set)
				self.mybar.pack()
				self.scrollbar.config(command=self.mybar.yview)

				self.mybar['columns'] = ("1","2") 
				self.mybar.column("#0", anchor=CENTER, width =200,minwidth=25)
				self.mybar.column("1", anchor=CENTER, width=100)
				self.mybar.column("2", anchor=CENTER, width=100)

				self.mybar.heading("#0", text="Process Name", anchor=W)
				self.mybar.heading("1",text = "ID", anchor=CENTER)
				self.mybar.heading("2", text = "Counting threading", anchor=CENTER)
				for i in range(self.length):
					self.mybar.insert(parent='', index='end',iid=0+i, text = self.Name[i], values=(self.ID[i],self.Thread[i]))

			def KillWindow():
				self.KillTask = Tk()
				self.KillTask.geometry("300x50")
				self.KillTask.title("Kill")

				self.EnterName = Entry(self.KillTask, width = 35)
				self.EnterName.grid(row=0, column=0, columnspan = 3, padx = 5, pady = 5 )
				self.EnterName.insert(END,"Nh???p t??n")

				def PressKill1():
					self.AppName = self.EnterName.get()
					client.sendall(bytes("KillTask","utf-8"))
					try:
						
						client.sendall(bytes(self.AppName,"utf-8"))
						self.checkdata = client.recv(1024).decode("utf-8")
						messagebox.showinfo("", "???? di???t ch????ng tr??nh")
					except:
						messagebox.showinfo("", "Kh??ng t??m th???y ch????ng tr??nh")

				KillButton = Button(self.KillTask, bg = "#FFE4E1",text = "Kill", font = "Helvetica 10 bold", padx = 20, command = PressKill1, bd = 5, activebackground='#F4A460').grid(row=0, column=4, padx=5, pady=5)

			def StartTask():
				self.StartTask = Tk()
				self.StartTask.geometry("300x50")
				self.StartTask.title("Start")

				self.EnterName = Entry(self.StartTask, width = 35)
				self.EnterName.grid(row = 0, column = 0, columnspan = 3, padx = 5, pady = 5)
				self.EnterName.insert(END,"Nh???p T??n")

				def PressStart1():
					self.Name = self.EnterName.get()
					client.sendall(bytes("OpenTask","utf-8"))
					try:
						client.sendall(bytes(self.Name,"utf-8"))
						self.checkdata = client.recv(1024).decode("utf-8")
						messagebox.showinfo("", "Ch????ng tr??nh ???? b???t")
					except:
						messagebox.showinfo("", "Kh??ng t??m th???y ch????ng tr??nh")

				StartButton = Button(self.StartTask, text = "Start", bg = "#FFE4E1",font = "Helvetica 10 bold", padx = 20, command = PressStart1).grid(row=0, column=4, padx=5, pady=5)

			Kill = Button( self.process, text = "Kill", bg = "#2E8B57",font = "Helvetica 10 bold", padx = 30,  pady = 20, command= KillWindow, bd = 5, activebackground='#F4A460').grid(row = 0, column = 0, padx = 0)
			Watch = Button(self.process, text = "Xem",bg = "#54FF9F",font = "Helvetica 10 bold",  padx = 30,  pady = 20, command = WatchTask, bd = 5, activebackground='#F4A460').grid(row = 0, column = 1, padx = 0)
			Xoa = Button(self.process, text =  "X??a", bg = "#4EEE94",font = "Helvetica 10 bold", padx = 30, pady = 20, command = XoaTask, bd = 5, activebackground='#F4A460').grid(row = 0, column = 2, padx = 0)
			Start = Button(self.process, text="Start", bg = "#43CD80", font = "Helvetica 10 bold", padx = 30, pady = 20, command = StartTask, bd = 5, activebackground='#F4A460').grid(row = 0, column = 3, padx = 0)

		except:
			messagebox.showinfo("!Warning", "L???i k???t n???i ")

	def fixregistry(self, client):
		try:
			Registry(client)

		except:
			messagebox.showinfo("!Warning", "L???i k???t n???i ")
		

	def keystroke(self, client):
		KeystrokeMain(client)
		
	def exist(self, client):
			try:
				client.send(bytes("Exit", 'utf-8'))
			except:
				messagebox.showinfo("!Warning", "L???i k???t n???i ")
			client.close()
			self.top.destroy()
		

	def control(self, client):

		self.top = Tk()
		self.top.configure(bg="white")
		self.top.title("Control")
		self.process =Button(self.top, text = "Process Running", bg = "#2E8B57", height =11, font=('Helvetica 10 bold'), command =(lambda : self.processrunning(client)), bd = 5, activebackground='#F4A460')
		self.process.grid(row = 1, column =0, rowspan =5)
		self.app = Button (self.top, text ="App Running", bg = "#008B8B",width =37,height =3, font=('Helvetica 10 bold'), command = (lambda : self.apprunning(client)), bd = 5, activebackground='#F4A460')
		self.app.grid (row =1, column =1, columnspan =3)
		self.shut = Button(self.top,text ="T???t m??y", bg = "#CD6839", width =19, height =5, font=('Helvetica 10 bold'), command = (lambda : self.shutdown(client)), bd = 5, activebackground='#F4A460')
		self.shut.grid(row = 2, column =1, columnspan =2, rowspan =2)
		self.capture = Button(self.top, text ="Ch???p m??n h??nh",bg = "#EEA2AD", width =16, height =5, font=('Helvetica 10 bold'), command = (lambda : self.takepicture(client)), bd = 5, activebackground='#F4A460')
		self.capture.grid(row = 2, column =3, columnspan =2, rowspan =2)
		self.fix =Button(self.top, text="S???a registry",bg = "#8B6969", width =37, font=('Helvetica 10 bold'), command = (lambda : self.fixregistry(client)), bd = 5, activebackground='#F4A460')
		self.fix.grid(row = 4, column =1, columnspan = 3, rowspan = 2)
		self.key = Button(self.top, text ="Keystroke",bg = "#FFFACD", height =9, width =11,font=('Helvetica 10 bold'), command = (lambda : self.keystroke(client)), bd = 5, activebackground='#F4A460')
		self.key.grid(row = 1, column =6, rowspan=3, columnspan =2)
		self.escape = Button(self.top, text ="Tho??t",bg = "#8B7B8B", width =11,font=('Helvetica 10 bold'), command = (lambda : self.exist(client)), bd = 5, activebackground='#F4A460')
		self.escape.grid(row = 4 , column =6)      
		self.top.mainloop()  #end user want

	def receive(self, client):
		while True:
			try:
				messagebox.showinfo(" Success ", "K???t n???i ?????n server th??nh c??ng")
				rcv = Thread(target=self.control(client))
				rcv.start()
			except:
				print("An error occured!")
				client.close()
				break

	def goAhead(self, HOST):
		global Host
		Host = HOST
		FORMAT = "utf-8"
		client = socket(AF_INET,SOCK_STREAM)
		try: 
			client.connect((HOST, 5656))
			client.send(bytes("Success", 'utf-8'))
			rcv = Thread(target=self.receive(client))
			rcv.start()
		except:
			messagebox.showinfo(" !Warning ", "Ch??a k???t n???i ?????n server") #Ki???m tra l???i k???t n???i b???ng c??ch d??ng try v?? except

if __name__ == "__main__":	
	GUI()

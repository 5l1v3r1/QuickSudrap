#!/usr/bin/python2.7
from Tkinter import *
import mechanize
import os
import sys
import time
import tkMessageBox
import ttk
import webbrowser

class App:
	def __init__(self, master,selected):
		self.frame = Frame(master)
		self.frame.pack(fill=BOTH, expand=YES)
		self.selected = selected
		self.textbox = text_label = Text(self.frame)
		self.textbox.insert(END, self.selected)
		self.textbox.config(state=DISABLED)
		self.textbox.pack(side=TOP,fill=X,expand=YES)
		Label(self.frame, text="Title:").pack(side=LEFT,anchor=NW)
		self.title = Entry(self.frame)
		self.title.pack(side=LEFT,anchor=NW,expand=YES)
		Label(self.frame, text="Author:").pack(side=LEFT,anchor=NW)
		self.author = Entry(self.frame)
		self.author.pack(side=LEFT,anchor=NW,expand=YES)
		Label(self.frame, text="Syntax:").pack(side=LEFT,anchor=NW)
		self.syntax = ttk.Combobox(self.frame)
		self.syntax['values'] = ('ApacheConf', 'AppleScript','ActionScript','ActionScript3','Bash','Batchfile','BBCode','Brainfuck',
		'C','Common Lisp','Debian Control File','C++','C#','CSS','CSS+Django/Jinja','CSS+Ruby','CSS+Mako','CSS+Smarty','D','Delphi',
		'Diff','Django/Jinja','ERB','Gnuplot','Haskell','HTML','HTML+Django/Jinja','HTML+Mako','HTML+PHP','HTML+Smarty','INI','IRC Logs',
		'Java','JavaScript','JavaScript+Django/Jinja','JavaScript+Ruby','JavaScript+Mako','JavaScript+PHP','JavaScript+Smarty',
		'Java Servlet Page','Lighttpd configuration file','Lua','Makefile','Mako','Matlab','MySQL','Nginx configuration file','Numpy',
		'Objective-C','Perl','PHP','Python','Python3','Ruby','Smarty','TeX','Text','VB.net','VimL','XML','XML+Django/Jinja','XML+Ruby',
		'XML+Mako','XML+PHP','XML+Smarty','XSLT','YAML')
		self.syntaxlist = {0:['apacheconf'], 1:['applescript'], 2:['as'], 3:['as3'], 4:['bash'], 5:['bat'], 6:['bbcode'], 7:['brainfuck'],
		8:['c'], 9:['common-lisp'], 10:['control'], 11:['cpp'], 12:['csharp'], 13:['css'], 14:['css+django'], 15:['css+erb'], 16:['css+mako'],
		17:['css+smarty'], 18:['d'], 19:['delphi'], 20:['diff'], 21:['django'], 22:['erb'], 23:['gnuplot'], 24:['haskell'], 25:['html'],
		26:['html+django'], 27:['html+mako'], 28:['html+php'], 29:['html+smarty'], 30:['ini'], 31:['irc'], 32:['java'], 33:['js'], 34:['js+django'],
		35:['js+erb'], 36:['js+mako'], 37:['js+php'], 38:['js+smarty'], 39:['jsp'], 40:['lighty'], 41:['lua'], 42:['make'], 43:['mako'],
		44:['matlab'], 45:['mysql'], 46:['ngnix'], 47:['numpy'], 48:['objective-c'], 49:['perl'], 50:['php'], 51:['python'], 52:['python3'],
		53:['ruby'], 54:['smarty'], 55:['tex'], 56:['text'], 57:['vb.net'], 58:['vim'], 59:['xml'], 60:['xml+django'], 61:['xml+erb'],
		62:['xml+mako'], 63:['xml+php'], 64:['xml+smarty'], 65:['xslt'], 66:['yaml']}
		self.syntax.state(['readonly'])
		self.syntax.current(56)
		self.syntax.pack(anchor=NW,expand=YES)
		self.send_it = Button(self.frame, text="Send", command=self.send)
		self.send_it.pack(side=RIGHT)

	def send(self):
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.set_handle_equiv(False)
		br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
		try:
			br.open("http://www.sudrap.org/paste/text/")
		except:
			  tkMessageBox.showerror("Error", sys.exc_info()[0])
		else:
			br.select_form(nr=0)
			br["text"] = self.selected
			br["title"] = self.title.get()
			br["author"] = self.author.get()
			br["syntax"] = self.syntaxlist[self.syntax.current()]
			try:
				br.submit()
			except:
				tkMessageBox.showerror("Error", "500 Error !")
			else:		
				self.pasted = br.geturl()
				self.send_it.destroy()
				link_label = Label(self.frame, text=self.pasted,fg="blue", cursor="hand2")
				link_label.pack(side=LEFT,anchor=NW)
				link_label.bind("<Button-1>", self.callback)
		
	def callback(self,event):
		webbrowser.open_new(self.pasted)
		
root = Tk()
root.title("QuickSudrap")
time.sleep(0.1)
selected = os.popen('xsel').read()
app = App(root,selected)
root.mainloop()
root.destroy()

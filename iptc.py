#! /usr/local/bin/python

from iptcinfo import IPTCInfo
import wx
import sys

class TheWindow(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, pos= (300,300), size= (400, 100))
	
		#panel = wx.Panel(self, -1, (300,300))
		hsizer = wx.BoxSizer(wx.HORIZONTAL)
		vsizer = wx.BoxSizer(wx.VERTICAL)
		text = wx.TextCtrl(self, -1,)
		vsizer.Add(hsizer)
		hsizer.Add(text, wx.ALL, border = 7)
		hsizer.Add(wx.Button(self, -1, "Image"))
		hsizer.Add(wx.Button(self, -1, "Directory"))
		
		self.SetSizer(hsizer)
		info= IPTCInfo('test.jpg')
		print info.data['copyright notice']
	# info.data['copyright notice']= 'Steve Ross'
	# info.saveAs('test_updated.jpg')
	

app = wx.PySimpleApp()
frame = TheWindow(None, -1, "CoPyrighter")
frame.Show(True)
app.MainLoop()

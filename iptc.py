#! /usr/local/bin/python

from iptcinfo import IPTCInfo
import wx
import sys

class TheWindow(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, pos= (300,300), size= (400, 200))
	
		#panel = wx.Panel(self, -1, (300,300))
		self.hsizer= wx.BoxSizer(wx.HORIZONTAL)
		self.vsizer= wx.BoxSizer(wx.VERTICAL)
		self.vsizer.Add(self.hsizer, border= 10)
		self.button_image = wx.Button(self, -1, "Image")
		self.hsizer.Add(self.button_image, border= 10)
		info= IPTCInfo('test.jpg')
		print info.data['copyright notice']
		
	# info.data['copyright notice']= 'Steve Ross'
	# info.saveAs('test_updated.jpg')
	

app = wx.PySimpleApp()
frame = TheWindow(None, -1, "CoPyrighter")
frame.Show(True)
app.MainLoop()

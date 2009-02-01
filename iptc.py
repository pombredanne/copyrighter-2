#! /usr/local/bin/python

from iptcinfo import IPTCInfo
import wx
import sys

# class TheWindow(wx.Frame):
# 	def __init__(self, parent, id, title):
# 		wx.Frame.__init__(self, parent, id, title, pos= (300,100), size= (400, 100))
# 
# 	
# 
# app = wx.PySimpleApp()
# frame = TheWindow(None, -1, "CoPyrighter")
# frame.Show(True)
# app.MainLoop()

info= IPTCInfo('test.jpg')
print info
info.data['copyright notice']= 'Steve Ross'
info.saveAs('test_updated.jpg')


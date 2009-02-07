#!/usr/local/bin/python

# This file was automatically generated by pywxrc.
# -*- coding: UTF-8 -*-

import os
import time
import sys
import wx
import wx.xrc as xrc
from iptcinfo import IPTCInfo

time= time.gmtime()
year = str(time[0])

__res = None

def get_resources():
	""" This function provides access to the XML resources in this module."""
	global __res
	if __res == None:
		__init_resources()
	return __res



class xrcmainWindow(wx.Frame):
#!XRCED:begin-block:xrcmainWindow.PreCreate
	def PreCreate(self, pre):
		""" This function is called during the class's initialization.

		Override it for custom setup before the window is created usually to
		set additional window styles using SetWindowStyle() and SetExtraStyle().
		"""
		pass

#!XRCED:end-block:xrcmainWindow.PreCreate

	def __init__(self, parent):
		# Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
		pre = wx.PreFrame()
		self.PreCreate(pre)
		get_resources().LoadOnFrame(pre, parent, "mainWindow")
		self.PostCreate(pre)

		# Define variables for the controls, bind event handlers
		self.text_entered = xrc.XRCCTRL(self, "text_entered")
		self.button_image = xrc.XRCCTRL(self, "button_image")
		self.button_folder = xrc.XRCCTRL(self, "button_folder")
		#self.text_preview = xrc.XRCCTRL(self, "text_preview")

		#self.Bind(wx.EVT_TEXT_ENTER, self.OnText_enter_text_entered, self.text_entered)
		self.Bind(wx.EVT_BUTTON, self.OnButton_button_image, self.button_image)
		self.Bind(wx.EVT_BUTTON, self.OnButton_button_folder, self.button_folder)
		self.Bind(wx.EVT_CLOSE, self.OnClose)

#!XRCED:begin-block:xrcmainWindow.OnText_enter_text_entered
	def OnText_enter_text_entered(self, evt):
		#self.text_preview.WriteText(self.text_entered.GetValue())
		print "OnText_enter_text_entered()"
#!XRCED:end-block:xrcmainWindow.OnText_enter_text_entered

#!XRCED:begin-block:xrcmainWindow.OnButton_button_image
	def OnButton_button_image(self, evt):
		image_file = wx.FileDialog(self)
		image_file.ShowModal()
		image= image_file.GetPath()
		split_image_path = image.split('/')
		image_name= split_image_path[-1]
		split_image_name = image_name.split('.')
		orig_name = split_image_name[0]
		#print orig_name
		info= IPTCInfo(str(image), force= True)
		copyright = info.data['copyright notice']
#		if copyright:
		print copyright
#			#print self.text_entered.GetValue()
#			print "Already copyrighted"  ########  Add popup dialog here #########
#		else:
		info.data['copyright notice'] = str(year + self.text_entered.GetValue())
		#print copyright
#		print "OnButton_button_image()"
		file_copy = (orig_name + '_cr' + '.' + split_image_name[-1])
		if os.path.exists(file_copy):
			dlg = wx.MessageDialog(self, 'Sorry!','The file ' + file_copy + ' already exists.', wx.OK | wx.ICON_INFORMATION)
			dlg.ShowModal()
			dlg.Destroy()
			return
		else:
			try:
				info.saveAs((orig_name + '_cr' + '.' + split_image_name[-1]))
			except:
				err = wx.MessageDialog(self, -1, sys.stderr)
				err.ShowModal(True)
				err.Destroy()
#!XRCED:end-block:xrcmainWindow.OnButton_button_image

#!XRCED:begin-block:xrcmainWindow.OnButton_button_folder
	def OnButton_button_folder(self, evt):
		# Replace with event handler code
		print "OnButton_button_folder()"
#!XRCED:end-block:xrcmainWindow.OnButton_button_folder

#!XRCED:begin-block:xrcmainWindow.OnClose
	def OnClose(self, evt):
		sys.exit()
		print "OnClose()"
#!XRCED:end-block:xrcmainWindow.OnClose




# ------------------------ Resource data ----------------------

def __init_resources():
	global __res
	__res = xrc.EmptyXmlResource()

	wx.FileSystem.AddHandler(wx.MemoryFSHandler())

	copyrighter_xrc = '''\
<?xml version="1.0" ?><resource>
  <object class="wxFrame" name="mainWindow">
	<object class="wxBoxSizer">
	  <orient>wxVERTICAL</orient>
	  <object class="sizeritem">
		<object class="wxBoxSizer">
		  <object class="sizeritem">
			<object class="wxPanel">
			  <object class="wxBoxSizer">
				<object class="sizeritem">
				  <object class="wxTextCtrl" name="text_entered">
					<size>300,-1</size>
					<XRCED>
					  <events>EVT_TEXT_ENTER</events>
					  <assign_var>1</assign_var>
					</XRCED>
				  </object>
				  <option>1</option>
				  <flag>wxALL</flag>
				  <border>5</border>
				  <ratio>1</ratio>
				</object>
				<object class="sizeritem">
				  <object class="wxButton" name="button_image">
					<label>Image</label>
					<XRCED>
					  <events>EVT_BUTTON</events>
					  <assign_var>1</assign_var>
					</XRCED>
				  </object>
				  <flag>wxALL</flag>
				  <border>5</border>
				</object>
				<object class="sizeritem">
				  <object class="wxButton" name="button_folder">
					<label>Folder</label>
					<XRCED>
					  <events>EVT_BUTTON</events>
					  <assign_var>1</assign_var>
					</XRCED>
				  </object>
				  <flag>wxALL</flag>
				  <border>5</border>
				</object>
				<orient>wxHORIZONTAL</orient>
			  </object>
			  <size>200,200</size>
			  <bg>#FFFFFF</bg>
			  <style>wxRAISED_BORDER</style>
			</object>
			<option>0</option>
			<flag>wxALL</flag>
			<border>10</border>
			<ratio>0</ratio>
		  </object>
		  <orient>wxHORIZONTAL</orient>
		</object>
		<flag>wxALL|wxEXPAND|wxGROW</flag>
	  </object>
	  <!--<object class="sizeritem">
		<object class="wxPanel">
		  <object class="wxBoxSizer">
			<orient>wxVERTICAL</orient>
			<object class="sizeritem">
			  <object class="wxBoxSizer">
				<orient>wxHORIZONTAL</orient>
				<object class="sizeritem">
				  <object class="wxStaticText">
					<label>Preview</label>
				  </object>
				</object>
				<object class="sizeritem">
				  <object class="wxStaticText" name="text_preview">
					<label>Example</label>
					<font>
					  <size>13</size>
					  <style>normal</style>
					  <weight>normal</weight>
					  <underlined>0</underlined>
					  <family>default</family>
					  <face>Lucida Grande</face>
					  <encoding/>
					</font>
					<XRCED>
					  <assign_var>1</assign_var>
					</XRCED>
				  </object>
				  <flag>wxLEFT</flag>
				  <border>20</border>
				</object>
			  </object>
			</object>
		  </object>
		  <size>200,400</size>
		  <bg>#FFFFFF</bg>
		</object>
		<option>1</option>
		<flag>wxALL|wxGROW</flag>
		<border>10</border>
		<ratio>1</ratio>
	  </object>-->
	</object>
	<pos>200,200</pos>
	<size>200,200</size>
	<title>CoPyrighter</title>
	<XRCED>
	  <events>EVT_CLOSE</events>
	</XRCED>
  </object>
</resource>'''

	wx.MemoryFSHandler.AddFile('XRC/copyrighter/copyrighter_xrc', copyrighter_xrc)
	__res.Load('memory:XRC/copyrighter/copyrighter_xrc')

app = wx.PySimpleApp()
frame = xrcmainWindow(None)
frame.Show(True)
app.MainLoop()
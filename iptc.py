#! /usr/local/bin/python

import iptc
from copyrighter import Ui_Form
from PyQt4 import QtGui
from PyQt4 import QtCore
import sys



class StartQT4(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)

		QtCore.QObject.connect(self.ui.button_image, QtCore.SIGNAL("clicked()"), self.open_image)
		QtCore.QObject.connect(self.ui.button_folder, QtCore.SIGNAL("clicked()"), self.open_folder)
		#QtCore.QObject.connect(self.ui.button_list, QtCore.SIGNAL("clicked()"), self.list_archive)
	
	
	def open_image(self):
		"""open a file to write copyright info"""
		print 'open_image'
		self.filename = QtGui.QFileDialog.getOpenFileName()
		pass
	

	def open_folder(self):
		"""open a folder to get images to write copyright info"""
		print 'open_folder'
		self.filenames = QtGui.QFileDialog.getExistingDirectory()
		pass
	



#################################
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = StartQT4()
	myapp.show()
	sys.exit(app.exec_())
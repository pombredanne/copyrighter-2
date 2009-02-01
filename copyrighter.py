# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iptc.ui'
#
# Created: Sat Jan 31 23:14:23 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(582, 100)
        self.user_text = QtGui.QLineEdit(Form)
        self.user_text.setGeometry(QtCore.QRect(9, 9, 246, 26))
        self.user_text.setObjectName("user_text")
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(265, 8, 274, 63))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_folder = QtGui.QPushButton(self.groupBox)
        self.button_folder.setObjectName("button_folder")
        self.horizontalLayout.addWidget(self.button_folder)
        self.button_image = QtGui.QPushButton(self.groupBox)
        self.button_image.setObjectName("button_image")
        self.horizontalLayout.addWidget(self.button_image)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(61, 46, 142, 17))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "CoPyrighter", None, QtGui.QApplication.UnicodeUTF8))
        self.button_folder.setText(QtGui.QApplication.translate("Form", "Choose Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.button_image.setText(QtGui.QApplication.translate("Form", "Choose Image", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Enter copyright text", None, QtGui.QApplication.UnicodeUTF8))


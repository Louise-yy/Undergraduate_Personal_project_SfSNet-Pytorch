# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Save(object):
    def setupUi(self, Save):
        Save.setObjectName("Save")
        Save.resize(432, 236)
        self.L_text1 = QtWidgets.QLabel(Save)
        self.L_text1.setGeometry(QtCore.QRect(140, 90, 211, 16))
        self.L_text1.setObjectName("L_text1")
        self.pushButton = QtWidgets.QPushButton(Save)
        self.pushButton.setGeometry(QtCore.QRect(170, 140, 81, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Save)
        self.pushButton.clicked.connect(Save.close_clicked)
        QtCore.QMetaObject.connectSlotsByName(Save)

    def retranslateUi(self, Save):
        _translate = QtCore.QCoreApplication.translate
        Save.setWindowTitle(_translate("Save", "Save"))
        self.L_text1.setText(_translate("Save", "Save successfully"))
        self.pushButton.setText(_translate("Save", "OK"))

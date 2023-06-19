# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myMap.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 600)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1500, 1500))
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 521, 20))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 170, 521, 20))
        self.line_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 280, 521, 20))
        self.line_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 400, 521, 20))
        self.line_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(110, 70, 20, 461))
        self.line_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(240, 70, 20, 461))
        self.line_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(370, 70, 21, 461))
        self.line_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.Agent = QtWidgets.QLabel(self.centralwidget)
        self.Agent.setGeometry(QtCore.QRect(0, 70, 110, 110))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Agent.setFont(font)
        self.Agent.setStyleSheet("color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 170, 0);")
        self.Agent.setAlignment(QtCore.Qt.AlignCenter)
        self.Agent.setIndent(-1)
        self.Agent.setObjectName("Agent")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(430, 20, 81, 26))
        self.startButton.setStyleSheet("background-color: rgb(0, 253, 255);")
        self.startButton.setObjectName("startButton")
        self.sweet_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.sweet_label_1.setEnabled(True)
        self.sweet_label_1.setGeometry(QtCore.QRect(20, 450, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.sweet_label_1.setFont(font)
        self.sweet_label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.sweet_label_1.setObjectName("sweet_label_1")
        self.sweet_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.sweet_label_2.setEnabled(True)
        self.sweet_label_2.setGeometry(QtCore.QRect(410, 100, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.sweet_label_2.setFont(font)
        self.sweet_label_2.setObjectName("sweet_label_2")
        self.sweet_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.sweet_label_3.setEnabled(True)
        self.sweet_label_3.setGeometry(QtCore.QRect(420, 440, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.sweet_label_3.setFont(font)
        self.sweet_label_3.setObjectName("sweet_label_3")
        self.label_di = QtWidgets.QLabel(self.centralwidget)
        self.label_di.setGeometry(QtCore.QRect(240, 20, 21, 21))
        self.label_di.setObjectName("label_di")
        self.label_lun_num = QtWidgets.QLabel(self.centralwidget)
        self.label_lun_num.setGeometry(QtCore.QRect(260, 10, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_lun_num.setFont(font)
        self.label_lun_num.setAlignment(QtCore.Qt.AlignCenter)
        self.label_lun_num.setObjectName("label_lun_num")
        self.label_lun = QtWidgets.QLabel(self.centralwidget)
        self.label_lun.setGeometry(QtCore.QRect(310, 20, 21, 21))
        self.label_lun.setObjectName("label_lun")
        self.label_bu_num = QtWidgets.QLabel(self.centralwidget)
        self.label_bu_num.setGeometry(QtCore.QRect(330, 10, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_bu_num.setFont(font)
        self.label_bu_num.setAlignment(QtCore.Qt.AlignCenter)
        self.label_bu_num.setObjectName("label_bu_num")
        self.label_bu = QtWidgets.QLabel(self.centralwidget)
        self.label_bu.setGeometry(QtCore.QRect(380, 20, 21, 21))
        self.label_bu.setObjectName("label_bu")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(510, 60, 20, 471))
        self.line_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.mapBackground = QtWidgets.QLabel(self.centralwidget)
        self.mapBackground.setGeometry(QtCore.QRect(0, 70, 511, 461))
        self.mapBackground.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mapBackground.setText("")
        self.mapBackground.setObjectName("mapBackground")
        self.mapBackground.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.startButton.raise_()
        self.sweet_label_1.raise_()
        self.sweet_label_2.raise_()
        self.sweet_label_3.raise_()
        self.label_di.raise_()
        self.label_lun_num.raise_()
        self.label_lun.raise_()
        self.label_bu_num.raise_()
        self.label_bu.raise_()
        self.line_8.raise_()
        self.Agent.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Agent.setText(_translate("MainWindow", "CAR"))
        self.startButton.setText(_translate("MainWindow", "开始"))
        self.sweet_label_1.setText(_translate("MainWindow", "障碍"))
        self.sweet_label_2.setText(_translate("MainWindow", "障碍"))
        self.sweet_label_3.setText(_translate("MainWindow", "障碍"))
        self.label_di.setText(_translate("MainWindow", "第"))
        self.label_lun_num.setText(_translate("MainWindow", "1"))
        self.label_lun.setText(_translate("MainWindow", "轮"))
        self.label_bu_num.setText(_translate("MainWindow", "1"))
        self.label_bu.setText(_translate("MainWindow", "步"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FridayUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1111, 641)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BG = QtWidgets.QLabel(self.centralwidget)
        self.BG.setGeometry(QtCore.QRect(-30, -20, 1141, 661))
        self.BG.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.BG.setText("")
        self.BG.setScaledContents(False)
        self.BG.setObjectName("BG")
        self.BGBorder = QtWidgets.QLabel(self.centralwidget)
        self.BGBorder.setGeometry(QtCore.QRect(0, 0, 1111, 641))
        self.BGBorder.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"border:2px Solid White;\n"
"\n"
"")
        self.BGBorder.setText("")
        self.BGBorder.setObjectName("BGBorder")
        self.START = QtWidgets.QPushButton(self.centralwidget)
        self.START.setGeometry(QtCore.QRect(820, 580, 131, 41))
        self.START.setStyleSheet("font: 18pt \"BankGothic\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px Solid White;\n"
"")
        self.START.setObjectName("START")
        self.EXIT = QtWidgets.QPushButton(self.centralwidget)
        self.EXIT.setGeometry(QtCore.QRect(960, 580, 131, 41))
        self.EXIT.setStyleSheet("font:18pt \"BankGothic\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px Solid White;\n"
"")
        self.EXIT.setObjectName("EXIT")
        self.GIF2 = QtWidgets.QLabel(self.centralwidget)
        self.GIF2.setGeometry(QtCore.QRect(820, 90, 281, 161))
        self.GIF2.setText("")
        self.GIF2.setPixmap(QtGui.QPixmap("earth.gif"))
        self.GIF2.setScaledContents(True)
        self.GIF2.setObjectName("GIF2")
        self.Voice = QtWidgets.QLabel(self.centralwidget)
        self.Voice.setGeometry(QtCore.QRect(10, 410, 801, 221))
        self.Voice.setText("")
        self.Voice.setPixmap(QtGui.QPixmap("__02-____.gif"))
        self.Voice.setScaledContents(False)
        self.Voice.setObjectName("Voice")
        self.Terminal = QtWidgets.QLabel(self.centralwidget)
        self.Terminal.setGeometry(QtCore.QRect(10, 10, 791, 391))
        self.Terminal.setText("")
        self.Terminal.setObjectName("Terminal")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(810, 10, 251, 51))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 22pt \"BankGothic\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(850, 50, 231, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 10pt \"BankGothic\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(826, 272, 271, 171))
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("ezgif.com-gif-maker.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(820, 440, 271, 121))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 19pt \"BankGothic\";\n"
"border: 1px Solid White;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.START.setText(_translate("MainWindow", "START"))
        self.EXIT.setText(_translate("MainWindow", "EXIT"))
        self.label.setText(_translate("MainWindow", "    F.R.I.D.A.Y"))
        self.label_2.setText(_translate("MainWindow", " Your Personal Voice Assistant"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

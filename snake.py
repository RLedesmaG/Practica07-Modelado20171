# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'snake.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(843, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 470, 481, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(540, 430, 211, 121))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(self.verticalLayoutWidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(90, 10, 111, 66))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.spinBox = QtGui.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.verticalLayout_2.addWidget(self.spinBox)
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 0, 81, 80))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 80, 178, 31))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 10, 481, 431))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.verticalLayoutWidget_3)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout_3.addWidget(self.plainTextEdit)
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(540, 300, 211, 121))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.frame_2 = QtGui.QFrame(self.verticalLayoutWidget_5)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.frame_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(90, 90, 123, 31))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_4 = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.frame_2)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(90, 20, 111, 66))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.lineEdit_2 = QtGui.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_6.addWidget(self.lineEdit_2)
        self.spinBox_2 = QtGui.QSpinBox(self.verticalLayoutWidget_6)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.verticalLayout_6.addWidget(self.spinBox_2)
        self.verticalLayoutWidget_7 = QtGui.QWidget(self.frame_2)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(10, 0, 81, 80))
        self.verticalLayoutWidget_7.setObjectName(_fromUtf8("verticalLayoutWidget_7"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_7.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_7.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_7.addWidget(self.label_6)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(540, 140, 211, 151))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.frame_3 = QtGui.QFrame(self.horizontalLayoutWidget_4)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayoutWidget_9 = QtGui.QWidget(self.frame_3)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(10, 0, 91, 151))
        self.verticalLayoutWidget_9.setObjectName(_fromUtf8("verticalLayoutWidget_9"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_9)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_9.addWidget(self.label_7)
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget_9)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_9.addWidget(self.label_10)
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget_9)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_9.addWidget(self.label_9)
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_9)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_9.addWidget(self.label_8)
        self.label_11 = QtGui.QLabel(self.verticalLayoutWidget_9)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_9.addWidget(self.label_11)
        self.widget = QtGui.QWidget(self.frame_3)
        self.widget.setGeometry(QtCore.QRect(120, 10, 79, 136))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.spinBox_6 = QtGui.QSpinBox(self.widget)
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))
        self.verticalLayout_11.addWidget(self.spinBox_6)
        self.spinBox_5 = QtGui.QSpinBox(self.widget)
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.verticalLayout_11.addWidget(self.spinBox_5)
        self.spinBox_7 = QtGui.QSpinBox(self.widget)
        self.spinBox_7.setObjectName(_fromUtf8("spinBox_7"))
        self.verticalLayout_11.addWidget(self.spinBox_7)
        self.spinBox_4 = QtGui.QSpinBox(self.widget)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.verticalLayout_11.addWidget(self.spinBox_4)
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.verticalLayoutWidget_10 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(540, 10, 211, 121))
        self.verticalLayoutWidget_10.setObjectName(_fromUtf8("verticalLayoutWidget_10"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.frame_4 = QtGui.QFrame(self.verticalLayoutWidget_10)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.label_12 = QtGui.QLabel(self.frame_4)
        self.label_12.setGeometry(QtCore.QRect(10, 0, 56, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.pushButton_5 = QtGui.QPushButton(self.frame_4)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 80, 71, 29))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.frame_4)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 20, 71, 29))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(self.frame_4)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 50, 61, 29))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.frame_4)
        self.pushButton_8.setGeometry(QtCore.QRect(140, 50, 61, 29))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.verticalLayout_10.addWidget(self.frame_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 843, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuJuego_SNake = QtGui.QMenu(self.menubar)
        self.menuJuego_SNake.setObjectName(_fromUtf8("menuJuego_SNake"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menuJuego_SNake.addSeparator()
        self.menubar.addAction(self.menuJuego_SNake.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Empezar el juego", None))
        self.label.setText(_translate("MainWindow", "Maestro", None))
        self.label_2.setText(_translate("MainWindow", "Uri Servidor", None))
        self.label_3.setText(_translate("MainWindow", "Puerto", None))
        self.pushButton_2.setText(_translate("MainWindow", "Conectar", None))
        self.pushButton_3.setText(_translate("MainWindow", "¡Ping!", None))
        self.pushButton_4.setText(_translate("MainWindow", "Levantar Servidor", None))
        self.label_4.setText(_translate("MainWindow", "Servidor", None))
        self.label_5.setText(_translate("MainWindow", "Url", None))
        self.label_6.setText(_translate("MainWindow", "Puerto", None))
        self.label_7.setText(_translate("MainWindow", "Tamaño", None))
        self.label_10.setText(_translate("MainWindow", "Columnas", None))
        self.label_9.setText(_translate("MainWindow", "Filas", None))
        self.label_8.setText(_translate("MainWindow", "Tam columnas", None))
        self.label_11.setText(_translate("MainWindow", "Tam filas", None))
        self.label_12.setText(_translate("MainWindow", "Controles", None))
        self.pushButton_5.setText(_translate("MainWindow", "v", None))
        self.pushButton_6.setText(_translate("MainWindow", "^", None))
        self.pushButton_7.setText(_translate("MainWindow", "<", None))
        self.pushButton_8.setText(_translate("MainWindow", ">", None))
        self.menuJuego_SNake.setTitle(_translate("MainWindow", "Juego Snake", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(650, 360)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(650, 360))
        MainWindow.setMaximumSize(QtCore.QSize(650, 360))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.a_field = QtWidgets.QLineEdit(self.centralwidget)
        self.a_field.setGeometry(QtCore.QRect(50, 210, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Circe")
        self.a_field.setFont(font)
        self.a_field.setText("")
        self.a_field.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.a_field.setObjectName("a_field")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 180, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Circe ExtraBold")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 210, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Circe Bold")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 210, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Circe Bold")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 240, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Circe Bold")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Circe Bold")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.b_field = QtWidgets.QLineEdit(self.centralwidget)
        self.b_field.setGeometry(QtCore.QRect(50, 240, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Circe")
        self.b_field.setFont(font)
        self.b_field.setText("")
        self.b_field.setObjectName("b_field")
        self.h_field = QtWidgets.QLineEdit(self.centralwidget)
        self.h_field.setGeometry(QtCore.QRect(50, 270, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Circe")
        self.h_field.setFont(font)
        self.h_field.setText("")
        self.h_field.setObjectName("h_field")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 270, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Circe Bold")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 270, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Circe Bold")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.task_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.task_text.setGeometry(QtCore.QRect(20, 20, 611, 151))
        self.task_text.setObjectName("task_text")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(310, 180, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Circe ExtraBold")
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.answer_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.answer_text.setGeometry(QtCore.QRect(310, 200, 321, 91))
        self.answer_text.setObjectName("answer_text")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 300, 611, 41))
        font = QtGui.QFont()
        font.setFamily("Circe Bold")
        font.setPointSize(17)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Проверка арматуры на прочность"))
        self.a_field.setPlaceholderText(_translate("MainWindow", "70"))
        self.label.setText(_translate("MainWindow", "Размеры сечения"))
        self.label_2.setText(_translate("MainWindow", "a = "))
        self.label_3.setText(_translate("MainWindow", "мм"))
        self.label_4.setText(_translate("MainWindow", "мм"))
        self.label_5.setText(_translate("MainWindow", "b = "))
        self.b_field.setPlaceholderText(_translate("MainWindow", "300"))
        self.h_field.setPlaceholderText(_translate("MainWindow", "800"))
        self.label_6.setText(_translate("MainWindow", "мм"))
        self.label_7.setText(_translate("MainWindow", "h = "))
        self.task_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Circe\'; font-size:14pt;\">Дано сечение размерами b, h, a мм; растянутая арматура класса </span><span style=\" font-family:\'Circe\'; font-size:14pt; font-weight:600;\">A400</span><span style=\" font-family:\'Circe\'; font-size:14pt;\"> (Rs = 350 МПа); площадь ее сечения A</span><span style=\" font-family:\'Circe\'; font-size:14pt; vertical-align:sub;\">s</span><span style=\" font-family:\'Circe\'; font-size:14pt;\"> = 2945 мм</span><span style=\" font-family:\'Circe\'; font-size:14pt; vertical-align:super;\">2</span><span style=\" font-family:\'Circe\'; font-size:14pt;\"> (6Ø25); бетон тяжелый класса </span><span style=\" font-family:\'Circe\'; font-size:14pt; font-weight:600;\">B25</span><span style=\" font-family:\'Circe\'; font-size:14pt;\"> (Rb = 14,5 МПа); изгибающий момент с учетом кратковременных нагрузок M = 550 кН•м.<br /></span><span style=\" font-family:\'Circe\'; font-size:14pt; text-decoration: underline;\">Требуется проверить прочность сечения.</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Прочность арматуры"))
        self.answer_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Рассчитать"))

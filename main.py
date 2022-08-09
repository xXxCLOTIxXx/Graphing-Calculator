# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(250, 300)
        Calculator.setFixedSize(250, 300)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.result_lbl = QtWidgets.QLabel(self.centralwidget)
        self.result_lbl.setGeometry(QtCore.QRect(0, 0, 250, 50))
        font = QtGui.QFont()
        self.result_lbl.setFont(font)
        self.result_lbl.setStyleSheet("color: rgb(61, 56, 70);\n"
"background-color: rgb(154, 153, 150);")
        self.result_lbl.setObjectName("result_lbl")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 50, 50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(0, 0, 0);")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(50, 50, 50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(0, 0, 0);")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(100, 50, 50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(0, 0, 0);")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 100, 50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(0, 0, 0);")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(50, 100, 50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(0, 0, 0);")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(100, 100, 50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(0, 0, 0);")
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 150, 50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(0, 0, 0);")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(50, 150, 50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(0, 0, 0);")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(100, 150, 50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(0, 0, 0);")
        self.btn_9.setObjectName("btn_9")
        self.btn_10 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_10.setGeometry(QtCore.QRect(0, 200, 50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_10.setFont(font)
        self.btn_10.setStyleSheet("background-color: rgb(154, 153, 150);\n"
"color: rgb(0, 0, 0);")
        self.btn_10.setObjectName("btn_10")
        self.Btn_equals = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_equals.setGeometry(QtCore.QRect(50, 200, 100, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Btn_equals.setFont(font)
        self.Btn_equals.setStyleSheet("background-color: rgb(165, 29, 45);\n"
"color: rgb(0, 0, 0);")
        self.Btn_equals.setObjectName("Btn_equals")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(150, 50, 50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("background-color: rgb(98, 160, 234);\n"
"color: rgb(0, 0, 0);")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(150, 100, 50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("background-color: rgb(98, 160, 234);\n"
"color: rgb(0, 0, 0);")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multiply.setGeometry(QtCore.QRect(150, 150, 50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_multiply.setFont(font)
        self.btn_multiply.setStyleSheet("background-color: rgb(98, 160, 234);\n"
"color: rgb(0, 0, 0);")
        self.btn_multiply.setObjectName("btn_multiply")
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_divide.setGeometry(QtCore.QRect(150, 200, 50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.btn_divide.setFont(font)
        self.btn_divide.setStyleSheet("background-color: rgb(98, 160, 234);\n"
"color: rgb(0, 0, 0);")
        self.btn_divide.setObjectName("btn_divide")
        self.Btn_c = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_c.setGeometry(QtCore.QRect(200, 50, 50, 100))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Btn_c.setFont(font)
        self.Btn_c.setStyleSheet("background-color: rgb(246, 97, 81);\n"
"color: rgb(0, 0, 0);")
        self.Btn_c.setObjectName("Btn_c")
        self.Btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.Btn_clear.setGeometry(QtCore.QRect(200, 150, 50, 100))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Btn_clear.setFont(font)
        self.Btn_clear.setStyleSheet("background-color: rgb(246, 97, 81);\n"
"color: rgb(0, 0, 0);")
        self.Btn_clear.setObjectName("Btn_clear")
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 24))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

        self.func()

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "MainWindow"))
        self.result_lbl.setText(_translate("Calculator", "0"))
        self.btn_1.setText(_translate("Calculator", "1"))
        self.btn_2.setText(_translate("Calculator", "2"))
        self.btn_3.setText(_translate("Calculator", "3"))
        self.btn_4.setText(_translate("Calculator", "4"))
        self.btn_5.setText(_translate("Calculator", "5"))
        self.btn_6.setText(_translate("Calculator", "6"))
        self.btn_7.setText(_translate("Calculator", "7"))
        self.btn_8.setText(_translate("Calculator", "8"))
        self.btn_9.setText(_translate("Calculator", "9"))
        self.btn_10.setText(_translate("Calculator", "0"))
        self.Btn_equals.setText(_translate("Calculator", "="))
        self.btn_plus.setText(_translate("Calculator", "+"))
        self.btn_minus.setText(_translate("Calculator", "-"))
        self.btn_multiply.setText(_translate("Calculator", "*"))
        self.btn_divide.setText(_translate("Calculator", "/"))
        self.Btn_c.setText(_translate("Calculator", "🡄"))
        self.Btn_clear.setText(_translate("Calculator", "Clear"))



    def func(self):
        self.btn_10.clicked.connect(lambda: self.add_num(self.btn_10.text()))
        self.btn_1.clicked.connect(lambda: self.add_num(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.add_num(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.add_num(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.add_num(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.add_num(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.add_num(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.add_num(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.add_num(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.add_num(self.btn_9.text()))
        self.btn_plus.clicked.connect(lambda: self.add_num(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.add_num(self.btn_minus.text()))
        self.btn_multiply.clicked.connect(lambda: self.add_num(self.btn_multiply.text()))
        self.btn_divide.clicked.connect(lambda: self.add_num(self.btn_divide.text()))
        self.Btn_equals.clicked.connect(self.results)
        self.Btn_c.clicked.connect(self.clear_one)
        self.Btn_clear.clicked.connect(self.clear)


    def clear_one(self):
        if self.result_lbl.text() != '0':
            if len(self.result_lbl.text()) <= 1:self.result_lbl.setText('0')
            else:self.result_lbl.setText(self.result_lbl.text()[0:-1])

    def clear(self):self.result_lbl.setText('0')






    def add_num(self, num):
        self.symbols = ['*', '/', '+', '-']
        if self.result_lbl.text() == '0' and num not in self.symbols:self.result_lbl.setText(num)
        else:
            if self.result_lbl.text()[-1] in self.symbols and num in self.symbols:self.result_lbl.setText(self.result_lbl.text()[0:-1]+num)
            else:self.result_lbl.setText(self.result_lbl.text()+num)


    def results(self):
        if self.result_lbl.text()[-1] in self.symbols:self.result_lbl.setText(self.result_lbl.text()[0:-1])
        try:
            res = eval(self.result_lbl.text())
            self.result_lbl.setText(str(res))
        except:pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())

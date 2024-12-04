
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 306)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.top_frame = QtWidgets.QFrame(self.centralwidget)
        self.top_frame.setGeometry(QtCore.QRect(10, 10, 341, 80))
        self.top_frame.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.top_frame.setFont(font)
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.answer_box = QtWidgets.QLineEdit(self.top_frame)
        self.answer_box.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.answer_box.setFont(font)
        self.answer_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.answer_box.setObjectName("answer_box")
        self.horizontalLayout.addWidget(self.answer_box)
        self.bottom_frame = QtWidgets.QFrame(self.centralwidget)
        self.bottom_frame.setGeometry(QtCore.QRect(10, 100, 338, 199))
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.bottom_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_allclear = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_allclear.setFont(font)
        self.btn_allclear.setStyleSheet("background-color: rgb(255, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.btn_allclear.setObjectName("btn_allclear")
        self.gridLayout.addWidget(self.btn_allclear, 0, 0, 1, 2)
        self.btn_clear = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("background-color: rgb(255, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 0, 2, 1, 3)
        self.btn_7 = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 2)
        self.btn_9 = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 1, 3, 1, 1)
        self.btn_multiply = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_multiply.setFont(font)
        self.btn_multiply.setObjectName("btn_multiply")
        self.gridLayout.addWidget(self.btn_multiply, 1, 4, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 2)
        self.btn_6 = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 2, 3, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_minus.setFont(font)
        self.btn_minus.setObjectName("btn_minus")
        self.gridLayout.addWidget(self.btn_minus, 2, 4, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 2)
        self.btn_3 = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 3, 3, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_plus.setFont(font)
        self.btn_plus.setObjectName("btn_plus")
        self.gridLayout.addWidget(self.btn_plus, 3, 4, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_dot.setFont(font)
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout.addWidget(self.btn_dot, 4, 0, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 4, 1, 1, 2)
        self.btn_div = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_div.setFont(font)
        self.btn_div.setObjectName("btn_div")
        self.gridLayout.addWidget(self.btn_div, 4, 3, 1, 1)
        self.btn_equal = QtWidgets.QPushButton(self.bottom_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_equal.setObjectName("btn_equal")
        self.gridLayout.addWidget(self.btn_equal, 4, 4, 1, 1)
        self.btn_dot.raise_()
        self.btn_1.raise_()
        self.btn_4.raise_()
        self.btn_7.raise_()
        self.btn_0.raise_()
        self.btn_2.raise_()
        self.btn_5.raise_()
        self.btn_8.raise_()
        self.btn_div.raise_()
        self.btn_3.raise_()
        self.btn_6.raise_()
        self.btn_9.raise_()
        self.btn_equal.raise_()
        self.btn_minus.raise_()
        self.btn_multiply.raise_()
        self.btn_allclear.raise_()
        self.btn_clear.raise_()
        self.btn_plus.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # connections
        self.btn_1.clicked.connect(lambda: self.pressed(1))
        self.btn_2.clicked.connect(lambda: self.pressed(2))
        self.btn_3.clicked.connect(lambda: self.pressed(3))
        self.btn_4.clicked.connect(lambda: self.pressed(4))
        self.btn_5.clicked.connect(lambda: self.pressed(5))      
        self.btn_6.clicked.connect(lambda: self.pressed(6))
        self.btn_7.clicked.connect(lambda: self.pressed(7))
        self.btn_8.clicked.connect(lambda: self.pressed(8))
        self.btn_9.clicked.connect(lambda: self.pressed(9))
        self.btn_0.clicked.connect(lambda: self.pressed(0))
        self.btn_dot.clicked.connect(lambda: self.pressed('.'))
        self.btn_plus.clicked.connect(lambda: self.pressed('+'))
        self.btn_minus.clicked.connect(lambda: self.pressed('-'))
        self.btn_multiply.clicked.connect(lambda: self.pressed('*'))
        self.btn_div.clicked.connect(lambda: self.pressed('/'))  

        self.btn_equal.clicked.connect(self.equal)
        self.btn_allclear.clicked.connect(self.all_clear)
        self.btn_clear.clicked.connect(self.clear)
        


    def pressed(self, number):
        self.answer_box.insert(str(number))  

    def equal(self):
        content = self.answer_box.text().strip()
        answer = eval(content)
        self.answer_box.setText(str(answer))

    def all_clear(self):
        self.answer_box.clear()   

    def clear(self):
        content = self.answer_box.text().strip()
        self.answer_box.setText(content[:-1])  

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "calculator"))
        self.btn_allclear.setText(_translate("MainWindow", "AC"))
        self.btn_clear.setText(_translate("MainWindow", "Del"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_multiply.setText(_translate("MainWindow", "*"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_equal.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(MainWindow)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.firstButton = QtWidgets.QPushButton(MainWindow)
        self.firstButton.setObjectName("firstButton")
        self.horizontalLayout.addWidget(self.firstButton)
        self.secondButton = QtWidgets.QPushButton(MainWindow)
        self.secondButton.setObjectName("secondButton")
        self.horizontalLayout.addWidget(self.secondButton)
        self.thirdButton = QtWidgets.QPushButton(MainWindow)
        self.thirdButton.setObjectName("thirdButton")
        self.horizontalLayout.addWidget(self.thirdButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(MainWindow)
        self.firstButton.clicked.connect(MainWindow.slot_firstButton)
        self.secondButton.clicked.connect(MainWindow.slot_secondButton)
        self.thirdButton.clicked.connect(MainWindow.slot_thirdButton)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pandora"))
        self.label.setText(_translate("MainWindow", "출력 결과"))
        self.firstButton.setText(_translate("MainWindow", "첫번째 버튼"))
        self.secondButton.setText(_translate("MainWindow", "두번째 버튼"))
        self.thirdButton.setText(_translate("MainWindow", "세번째 버튼"))


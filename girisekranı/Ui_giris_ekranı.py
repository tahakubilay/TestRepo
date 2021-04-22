# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/vezemir/repo/TestRepo/giris_ekranı.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(761, 634)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 120, 391, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.input_kullaniciadi = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.input_kullaniciadi.setObjectName("input_kullaniciadi")
        self.gridLayout.addWidget(self.input_kullaniciadi, 0, 1, 1, 1)
        self.input_sifre = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.input_sifre.setObjectName("input_sifre")
        self.gridLayout.addWidget(self.input_sifre, 1, 1, 1, 1)
        self.labe_kullaniciadi = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labe_kullaniciadi.sizePolicy().hasHeightForWidth())
        self.labe_kullaniciadi.setSizePolicy(sizePolicy)
        self.labe_kullaniciadi.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labe_kullaniciadi.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.labe_kullaniciadi.setObjectName("labe_kullaniciadi")
        self.gridLayout.addWidget(self.labe_kullaniciadi, 0, 0, 1, 1)
        self.checkbox_benihatirla = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkbox_benihatirla.setObjectName("checkbox_benihatirla")
        self.gridLayout.addWidget(self.checkbox_benihatirla, 2, 0, 1, 1)
        self.label_sifre = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_sifre.setObjectName("label_sifre")
        self.gridLayout.addWidget(self.label_sifre, 1, 0, 1, 1)
        self.button_giris = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_giris.setObjectName("button_giris")
        self.gridLayout.addWidget(self.button_giris, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labe_kullaniciadi.setText(_translate("MainWindow", "Kullanıcı Adı"))
        self.checkbox_benihatirla.setText(_translate("MainWindow", "Beni Hatırla"))
        self.label_sifre.setText(_translate("MainWindow", "Şifre"))
        self.button_giris.setText(_translate("MainWindow", "Giriş"))

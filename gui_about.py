# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_about.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(About.sizePolicy().hasHeightForWidth())
        About.setSizePolicy(sizePolicy)
        self.label_3 = QtWidgets.QLabel(About)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 361, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(About)
        self.label_5.setGeometry(QtCore.QRect(110, 240, 191, 17))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(About)
        self.label_7.setGeometry(QtCore.QRect(10, 210, 391, 20))
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(About)
        self.label_4.setGeometry(QtCore.QRect(160, 90, 64, 17))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(About)
        self.label_6.setGeometry(QtCore.QRect(120, 190, 161, 17))
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(About)
        self.label_2.setGeometry(QtCore.QRect(130, 40, 161, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(About)
        self.line.setGeometry(QtCore.QRect(110, 70, 191, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About Proton Flux"))
        self.label_3.setText(_translate("About", "<html><head/><body><p align=\"justify\">Free and open source educational tool to study reactant conversion in electrochemical reactors and flow cells operating under full mass transfer control.</p></body></html>"))
        self.label_5.setText(_translate("About", "<html><head/><body><p>Visit <a href=\"http://echemsoft.xyz\"><span style=\" text-decoration: underline; color:#0000ff;\">http://echemsoft.xyz</span></a></p></body></html>"))
        self.label_7.setText(_translate("About", "<html><head/><body><p>Copyright © 2020 <a href=\"mailto:oliver.rdz.mtz@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">Oliver Rodríguez</span></a>, <a href=\"fernando2113@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">Luis Fernando Arenas</span></a></p></body></html>"))
        self.label_4.setText(_translate("About", "v0.0.1"))
        self.label_6.setText(_translate("About", "Licensed under GPL v3"))
        self.label_2.setText(_translate("About", "Proton Flux"))

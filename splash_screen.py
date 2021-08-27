# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splash_screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect


class Ui_Form(object):
    def __init__(self):
        self.jumper = 0

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(340, 340)
        self.circularProgressBarBase = QtWidgets.QFrame(Form)
        self.circularProgressBarBase.setGeometry(QtCore.QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgressBarBase.setObjectName("circularProgressBarBase")
        self.circularProgress = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularProgress.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet("QFrame{\n"
                                            "    border-radius: 150px;\n"
                                            "    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.75 rgba(85, 170, 255, 255));\n"
                                            "}")
        self.circularProgress.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularProgress.setObjectName("circularProgress")
        self.circularBg = QtWidgets.QFrame(self.circularProgressBarBase)
        self.circularBg.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet("QFrame{\n"
                                      "    border-radius: 150px;\n"
                                      "    background-color: rgba(77, 77, 127, 120);\n"
                                      "}")
        self.circularBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.circularBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.circularBg.setObjectName("circularBg")
        self.container = QtWidgets.QFrame(self.circularProgressBarBase)
        self.container.setGeometry(QtCore.QRect(25, 25, 270, 270))
        self.container.setStyleSheet("QFrame{\n"
                                     "    border-radius: 135px;\n"
                                     "    background-color: rgb(77, 77, 127);\n"
                                     "}")
        self.container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.widget = QtWidgets.QWidget(self.container)
        self.widget.setGeometry(QtCore.QRect(40, 50, 193, 191))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelTitle = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet("background-color: none;\n"
                                      "color: #ffffff")
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)
        self.labelPercentage = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(68)
        self.labelPercentage.setFont(font)
        self.labelPercentage.setStyleSheet("background-color: none;\n"
                                           "color: #ffffff")
        self.labelPercentage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPercentage.setObjectName("labelPercentage")
        self.gridLayout.addWidget(self.labelPercentage, 1, 0, 1, 1)
        self.labelLoading = QtWidgets.QLabel(self.widget)
        self.labelLoading.setMinimumSize(QtCore.QSize(0, 20))
        self.labelLoading.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.labelLoading.setFont(font)
        self.labelLoading.setStyleSheet("QLabel{\n"
                                        "    border-radius:10px;\n"
                                        "    background-color: rgb(93, 93, 154);\n"
                                        "    color: #ffffff;\n"
                                        "    margin-left:40px;\n"
                                        "    margin-right: 40px;\n"
                                        "}")
        self.labelLoading.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLoading.setObjectName("labelLoading")
        self.gridLayout.addWidget(self.labelLoading, 2, 0, 1, 1)
        self.labelCredits = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.labelCredits.setFont(font)
        self.labelCredits.setStyleSheet("background-color: none;\n"
                                        "color: rgb(155, 155, 255);\n"
                                        "")
        self.labelCredits.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCredits.setObjectName("labelCredits")
        self.gridLayout.addWidget(self.labelCredits, 3, 0, 1, 1)
        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def progressBarValue(self, value):
        styleSheet = """
        QFrame{
            border-radius: 150px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0),
            stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """

        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        newHtml = htmlText.replace("{VALUE}", str(self.jumper))
        if value > self.jumper:
            self.labelPercentage.setText(newHtml)
            self.jumper += 5
        progress = (100 - value) / 100.0
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        newStyleSheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
        self.circularProgress.setStyleSheet(newStyleSheet)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelTitle.setText(
            _translate("Form", "<p><span style=\" font-weight:600; color:#9b9bff;\">YOUR</span> APPLICATION NAME</p>"))
        self.labelPercentage.setText(_translate("Form",
                                                "<p><span style=\" font-size:68pt;\">0</span><span style=\" font-size:58pt; vertical-align:super;\">%</span></p>"))
        self.labelLoading.setText(_translate("Form", "loading..."))
        self.labelCredits.setText(_translate("Form", "by: Yusuf ERKAN"))


class ProgressBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.counter = 0
        self.jumper = 0
        self.ui.progressBarValue(0)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(15)

        self.show()

    def progress(self):
        value = self.counter
        self.ui.progressBarValue(value)

        if self.counter >= 100:
            self.timer.stop()
            self.close()

        self.counter += 0.5


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProgressBar()
    sys.exit(app.exec_())

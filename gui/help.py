# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_help_form(object):
    def setupUi(self, help_form):
        help_form.setObjectName("help_form")
        help_form.resize(240, 320)
        self.label_3 = QtWidgets.QLabel(help_form)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 191, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton_send = QtWidgets.QPushButton(help_form)
        self.pushButton_send.setGeometry(QtCore.QRect(150, 270, 75, 23))
        self.pushButton_send.setObjectName("pushButton_send")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(help_form)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 40, 211, 221))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(help_form)
        QtCore.QMetaObject.connectSlotsByName(help_form)

    def retranslateUi(self, help_form):
        _translate = QtCore.QCoreApplication.translate
        help_form.setWindowTitle(_translate("help_form", "Form"))
        self.label_3.setText(_translate("help_form", "Describe your problem or suggestion"))
        self.pushButton_send.setText(_translate("help_form", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    help_form = QtWidgets.QWidget()
    ui = Ui_help_form()
    ui.setupUi(help_form)
    help_form.show()
    sys.exit(app.exec_())


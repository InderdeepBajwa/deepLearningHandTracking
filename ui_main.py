# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1900, 890)
        self.logView = QtWidgets.QTextBrowser(Dialog)
        self.logView.setGeometry(QtCore.QRect(1500, 500, 341, 141))
        self.logView.setObjectName("logView")
        self.image_label = QtWidgets.QLabel(Dialog)
        self.image_label.setGeometry(QtCore.QRect(50, 50, 1400, 720))
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(1630, 230, 171, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(1640, 450, 171, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(1650, 650, 171, 16))
        self.label_3.setObjectName("label_3")
        self.patientView = QtWidgets.QLabel(Dialog)
        self.patientView.setGeometry(QtCore.QRect(1510, 40, 321, 161))
        self.patientView.setObjectName("patientView")
        self.teacherView = QtWidgets.QLabel(Dialog)
        self.teacherView.setGeometry(QtCore.QRect(1510, 260, 321, 161))
        self.teacherView.setObjectName("teacherView")
        self.image_label.raise_()
        self.logView.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.patientView.raise_()
        self.teacherView.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.image_label.setText(_translate("Dialog", "Loading video..."))
        self.label.setText(_translate("Dialog", "Patient\'s View"))
        self.label_2.setText(_translate("Dialog", "Teacher\'s View"))
        self.label_3.setText(_translate("Dialog", "Logs"))
        self.patientView.setText(_translate("Dialog", "Launching Patient\'s view"))
        self.teacherView.setText(_translate("Dialog", "Launching Teacher\'s view"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


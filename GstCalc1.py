# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'C:\Users\Darryl\Documents\PyQt Designer\GstCalc\GstCalc1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

# Set the default GST percentage rate
gst_percentage = 10  # todo Load percentage rate from a file


class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(559, 261)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:rgb(220,255,255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.title_lbl = QtWidgets.QLabel(self.centralwidget)
        self.title_lbl.setGeometry(QtCore.QRect(20, 0, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(28)
        font.setItalic(True)
        self.title_lbl.setFont(font)
        self.title_lbl.setObjectName("title_lbl")
        self.descrption_lbl = QtWidgets.QLabel(self.centralwidget)
        self.descrption_lbl.setGeometry(QtCore.QRect(10, 40, 451, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.descrption_lbl.setFont(font)
        self.descrption_lbl.setWordWrap(True)
        self.descrption_lbl.setObjectName("descrption_lbl")
        self.gstExclusive_lbl = QtWidgets.QLabel(self.centralwidget)
        self.gstExclusive_lbl.setGeometry(QtCore.QRect(260, 170, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gstExclusive_lbl.setFont(font)
        self.gstExclusive_lbl.setStyleSheet("background-color:rgb(255,255,255);")
        self.gstExclusive_lbl.setText("")
        self.gstExclusive_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gstExclusive_lbl.setObjectName("gstExclusive_lbl")
        self.totalExclusive_lbl = QtWidgets.QLabel(self.centralwidget)
        self.totalExclusive_lbl.setGeometry(QtCore.QRect(380, 170, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.totalExclusive_lbl.setFont(font)
        self.totalExclusive_lbl.setStyleSheet("background-color:rgb(255,255,255);")
        self.totalExclusive_lbl.setText("")
        self.totalExclusive_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.totalExclusive_lbl.setObjectName("totalExclusive_lbl")
        self.gstInclusive_lbl = QtWidgets.QLabel(self.centralwidget)
        self.gstInclusive_lbl.setGeometry(QtCore.QRect(260, 200, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gstInclusive_lbl.setFont(font)
        self.gstInclusive_lbl.setStyleSheet("background-color:rgb(255,255,255);")
        self.gstInclusive_lbl.setText("")
        self.gstInclusive_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gstInclusive_lbl.setObjectName("gstInclusive_lbl")
        self.totalInclusive_lbl = QtWidgets.QLabel(self.centralwidget)
        self.totalInclusive_lbl.setGeometry(QtCore.QRect(380, 200, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.totalInclusive_lbl.setFont(font)
        self.totalInclusive_lbl.setStyleSheet("background-color:rgb(255,255,255);")
        self.totalInclusive_lbl.setText("")
        self.totalInclusive_lbl.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.totalInclusive_lbl.setObjectName("totalInclusive_lbl")
        self.inputAmount_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.inputAmount_txt.setGeometry(QtCore.QRect(20, 140, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.inputAmount_txt.setFont(font)
        self.inputAmount_txt.setAutoFillBackground(False)
        self.inputAmount_txt.setStyleSheet("background-color:white")
        self.inputAmount_txt.setObjectName("inputAmount_txt")
        self.amount_lbl = QtWidgets.QLabel(self.centralwidget)
        self.amount_lbl.setGeometry(QtCore.QRect(20, 110, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.amount_lbl.setFont(font)
        self.amount_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.amount_lbl.setObjectName("amount_lbl")
        self.exclusive_lbl = QtWidgets.QLabel(self.centralwidget)
        self.exclusive_lbl.setGeometry(QtCore.QRect(140, 170, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.exclusive_lbl.setFont(font)
        self.exclusive_lbl.setObjectName("exclusive_lbl")
        self.inclusive_lbl = QtWidgets.QLabel(self.centralwidget)
        self.inclusive_lbl.setGeometry(QtCore.QRect(140, 200, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.inclusive_lbl.setFont(font)
        self.inclusive_lbl.setObjectName("inclusive_lbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 559, 21))
        self.menubar.setObjectName("menubar")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionEdit_GST_Prcentage = QtWidgets.QAction(MainWindow)
        self.actionEdit_GST_Prcentage.setObjectName("actionEdit_GST_Prcentage")
        self.menuEdit.addAction(self.actionEdit_GST_Prcentage)
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GST Calc"))
        self.title_lbl.setText(_translate("MainWindow", "GST Calculator"))
        self.descrption_lbl.setText(_translate("MainWindow",
                                               "Input a figure into the amount box and read off the figures for gst inclusive and exclusive calculations."))
        self.inputAmount_txt.setToolTip(_translate("MainWindow", "Input amount either with or without GST"))
        self.amount_lbl.setText(_translate("MainWindow", "Input Amount"))
        self.exclusive_lbl.setText(_translate("MainWindow", "GST Exclusive"))
        self.inclusive_lbl.setText(_translate("MainWindow", "GST Inclusive"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionEdit_GST_Prcentage.setText(_translate("MainWindow", "Edit GST Percentage"))

        # Event Listeners
        # todo Events for text input and Change tax rate on menu bar
        self.inputAmount_txt.editingFinished.connect(self.inputSanitize)

    def do_calcs(self, final_Amount):
        gst_factor = gst_percentage / 100 + 1
        totEx = "${:,.2f}".format(final_Amount * gst_factor)
        gstEx = "${:,.2f}".format(final_Amount * (gst_percentage / 100))
        gstInc = "${:,.2f}".format(final_Amount - (final_Amount / gst_factor))
        totInc = "${:,.2f}".format(final_Amount / gst_factor)
        self.totalExclusive_lbl.setText(totEx)
        self.gstExclusive_lbl.setText(gstEx)
        self.gstInclusive_lbl.setText(gstInc)
        self.totalInclusive_lbl.setText(totInc)

        print("I made it here.")

    def inputSanitize(self):
        amount = self.inputAmount_txt.text()
        try:
            final_Amount = round(float(amount), 2)
            self.do_calcs(final_Amount)
        except Exception as e:  # todo Handle exceptions properly

            print('There was a problem ' + str(e))


def gstFile():
    try:
        with open("gstAmount.txt", "r") as fh:
            global gst_percentage
            gst_percentage = float(fh.read())
    except Exception as e:
        writeFile()  # if no file is found goto writefile func and create a file


def writeFile():
    with open("gstAmount.txt", "w") as fh:
        fh.write(str(gst_percentage))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup_ui(MainWindow)
    gstFile()
    MainWindow.show()
    sys.exit(app.exec_())

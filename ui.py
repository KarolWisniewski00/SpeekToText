from PyQt5 import QtCore, QtGui, QtWidgets
import speech_recognition as sr
import pyperclip
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(730, 696)
        Form.setStyleSheet("background-color: #060A0D;\n"
"color: white;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet("#pushButton{\n"
"background-color:#D93E30;\n"
"border-radius:15px;\n"
"border:none;\n"
"padding:15px;\n"
"}\n"
"#pushButton:hover{\n"
"background-color:#8C2727;\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("microphone-black-shape.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(64, 64))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color:#111517;\n"
"border-radius:15px;\n"
"border:none;\n"
"padding:5px;")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.horizontalLayout.addWidget(self.widget_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("#pushButton_2{\n"
"background-color:#F2921D;\n"
"border-radius:15px;\n"
"border:none;\n"
"padding:5px 15px;\n"
"}\n"
"#pushButton_2:hover{\n"
"background-color:#F27329;\n"
"}")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("Corbel Light")
        font.setPointSize(24)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("#pushButton_3{\n"
"background-color:#D93E30;\n"
"border-radius:15px;\n"
"border:none;\n"
"padding:5px 15px;\n"
"}\n"
"#pushButton_3:hover{\n"
"background-color:#8C2727;\n"
"}")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.widget_2)

        self.pushButton.clicked.connect(lambda: self.clickedMicrophone())
        self.pushButton_2.clicked.connect(lambda: self.clickedCopy())
        self.pushButton_3.clicked.connect(lambda: self.clickedClear())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Naciśnij i mów"))
        self.label_2.setText(_translate("Form", "Twój tekst:"))
        self.pushButton_2.setText(_translate("Form", "Kopiuj"))
        self.pushButton_3.setText(_translate("Form", "Wyczyść"))

    def clickedMicrophone(self):
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
                text = r.recognize_google(audio, language='pl_Pl')
            self.textEdit.append(text)
        except:
            pass

    def clickedCopy(self):
        pyperclip.copy(self.textEdit.toPlainText())

    def clickedClear(self):
        self.textEdit.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

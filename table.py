from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TableEditor(object):
    def setupUi(self, TableEditor):
        TableEditor.setObjectName("TableEditor")
        TableEditor.resize(1051, 620)
        self.centralwidget = QtWidgets.QWidget(TableEditor)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.razdel_line1 = QtWidgets.QLineEdit(self.groupBox)
        self.razdel_line1.setText("")
        self.razdel_line1.setReadOnly(False)
        self.razdel_line1.setObjectName("razdel_line1")
        self.horizontalLayout.addWidget(self.razdel_line1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.razdel_line2 = QtWidgets.QLineEdit(self.groupBox)
        self.razdel_line2.setText("")
        self.razdel_line2.setReadOnly(False)
        self.razdel_line2.setObjectName("razdel_line2")
        self.horizontalLayout.addWidget(self.razdel_line2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.sort_check = QtWidgets.QCheckBox(self.groupBox)
        self.sort_check.setText("")
        self.sort_check.setObjectName("sort_check")
        self.horizontalLayout.addWidget(self.sort_check)
        self.string_all = QtWidgets.QCheckBox(self.groupBox)
        self.string_all.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.string_all.setChecked(False)
        self.string_all.setAutoRepeat(False)
        self.string_all.setAutoExclusive(False)
        self.string_all.setTristate(False)
        self.string_all.setObjectName("string_all")
        self.horizontalLayout.addWidget(self.string_all)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_path = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_path.setReadOnly(True)
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.horizontalLayout.addWidget(self.lineEdit_path)
        self.path_button = QtWidgets.QToolButton(self.groupBox)
        self.path_button.setObjectName("path_button")
        self.horizontalLayout.addWidget(self.path_button)
        self.save_button = QtWidgets.QPushButton(self.groupBox)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(8, 5)
        self.verticalLayout.addWidget(self.groupBox)
        TableEditor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TableEditor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 21))
        self.menubar.setObjectName("menubar")
        TableEditor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TableEditor)
        self.statusbar.setObjectName("statusbar")
        TableEditor.setStatusBar(self.statusbar)

        self.retranslateUi(TableEditor)
        QtCore.QMetaObject.connectSlotsByName(TableEditor)

    def retranslateUi(self, TableEditor):
        _translate = QtCore.QCoreApplication.translate
        TableEditor.setWindowTitle(_translate("TableEditor", "ACSV Reader"))
        self.label.setText(_translate("TableEditor", "Разделитель строк"))
        self.label_2.setText(_translate("TableEditor", "Разделитель столбцов"))
        self.label_3.setText(_translate("TableEditor", "Сортировать как числа"))
        self.string_all.setText(_translate("TableEditor", "Все строки"))
        self.label_4.setText(_translate("TableEditor", "Путь к файлу"))
        self.path_button.setText(_translate("TableEditor", "..."))
        self.save_button.setText(_translate("TableEditor", "Сохранить"))
        self.pushButton.setText(_translate("TableEditor", "Авто"))
import os
from PyQt4 import QtGui,QtCore

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class setting_dialog(object):
    def setupUi(self, setting_dialog):
        setting_dialog.setObjectName(_fromUtf8("setting_dialog"))
        setting_dialog.resize(469, 231)
        self.verticalLayout_4 = QtGui.QVBoxLayout(setting_dialog)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.database_type_label = QtGui.QLabel(setting_dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.database_type_label.setFont(font)
        self.database_type_label.setText(_fromUtf8(""))
        self.database_type_label.setObjectName(_fromUtf8("database_type_label"))
        self.horizontalLayout_3.addWidget(self.database_type_label)
        spacerItem2 = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.server_name = QtGui.QLabel(setting_dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.server_name.setFont(font)
        self.server_name.setObjectName(_fromUtf8("server_name"))
        self.verticalLayout_2.addWidget(self.server_name)
        spacerItem4 = QtGui.QSpacerItem(20, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem4)
        self.server_port_check = QtGui.QCheckBox(setting_dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.server_port_check.setFont(font)
        self.server_port_check.setObjectName(_fromUtf8("server_port_check"))
        self.verticalLayout_2.addWidget(self.server_port_check)
        spacerItem5 = QtGui.QSpacerItem(20, 12, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.server_connection = QtGui.QLineEdit(setting_dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.server_connection.setFont(font)
        self.server_connection.setObjectName(_fromUtf8("server_connection"))
        self.verticalLayout.addWidget(self.server_connection)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.server_port = QtGui.QLineEdit(setting_dialog)
        self.server_port.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.server_port.setFont(font)
        self.server_port.setObjectName(_fromUtf8("server_port"))
        self.horizontalLayout.addWidget(self.server_port)
        self.default_server_port = QtGui.QLabel(setting_dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.default_server_port.setFont(font)
        self.default_server_port.setObjectName(_fromUtf8("default_server_port"))
        self.horizontalLayout.addWidget(self.default_server_port)
        spacerItem6 = QtGui.QSpacerItem(48, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.buttonBox = QtGui.QDialogButtonBox(setting_dialog)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_4.addWidget(self.buttonBox)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(setting_dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), setting_dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), setting_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(setting_dialog)



    def retranslateUi(self, setting_dialog):
        setting_dialog.setWindowTitle(QtGui.QApplication.translate("setting_dialog", '', None, QtGui.QApplication.UnicodeUTF8))
        self.server_name.setText(QtGui.QApplication.translate("setting_dialog", '', None, QtGui.QApplication.UnicodeUTF8))
        self.server_port_check.setText(QtGui.QApplication.translate("setting_dialog", '', None, QtGui.QApplication.UnicodeUTF8))
        self.default_server_port.setText(QtGui.QApplication.translate("setting_dialog", '', None, QtGui.QApplication.UnicodeUTF8))

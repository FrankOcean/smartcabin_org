# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'derain.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DerainForm(object):
    def setupUi(self, DerainForm):
        DerainForm.setObjectName("DerainForm")
        DerainForm.resize(905, 626)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DerainForm)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(DerainForm)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.openfile_btn = QtWidgets.QPushButton(DerainForm)
        self.openfile_btn.setObjectName("openfile_btn")
        self.horizontalLayout_5.addWidget(self.openfile_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(DerainForm)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.video_compare_constrain = QtWidgets.QHBoxLayout()
        self.video_compare_constrain.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.video_compare_constrain.setObjectName("video_compare_constrain")
        self.verticalLayout.addLayout(self.video_compare_constrain)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(DerainForm)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(DerainForm)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.process_label = QtWidgets.QLabel(DerainForm)
        self.process_label.setObjectName("process_label")
        self.horizontalLayout.addWidget(self.process_label)
        self.progressBar = QtWidgets.QProgressBar(DerainForm)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_5 = QtWidgets.QPushButton(DerainForm)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(DerainForm)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.pushButton_6 = QtWidgets.QPushButton(DerainForm)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(DerainForm)
        self.pushButton_2.clicked.connect(DerainForm.close)
        QtCore.QMetaObject.connectSlotsByName(DerainForm)

    def retranslateUi(self, DerainForm):
        _translate = QtCore.QCoreApplication.translate
        DerainForm.setWindowTitle(_translate("DerainForm", "Form"))
        self.pushButton_2.setText(_translate("DerainForm", "关闭窗口"))
        self.openfile_btn.setText(_translate("DerainForm", "打开文件"))
        self.pushButton.setText(_translate("DerainForm", "功能未定义"))
        self.label_2.setText(_translate("DerainForm", "原视频"))
        self.label_3.setText(_translate("DerainForm", "去雨视频"))
        self.process_label.setText(_translate("DerainForm", "处理进度:"))
        self.pushButton_5.setText(_translate("DerainForm", "PushButton"))
        self.pushButton_4.setText(_translate("DerainForm", "PushButton"))
        self.pushButton_6.setText(_translate("DerainForm", "PushButton"))

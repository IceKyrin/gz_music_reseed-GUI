# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.text_res = QtWidgets.QTextEdit(self.centralwidget)
        self.text_res.setMinimumSize(QtCore.QSize(0, 300))
        self.text_res.setMaximumSize(QtCore.QSize(16777215, 300))
        self.text_res.setObjectName("text_res")
        self.gridLayout_2.addWidget(self.text_res, 4, 0, 1, 1)
        self.title = QtWidgets.QHBoxLayout()
        self.title.setObjectName("title")
        self.menu = QtWidgets.QFormLayout()
        self.menu.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.menu.setObjectName("menu")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setMinimumSize(QtCore.QSize(32, 32))
        self.logo.setMaximumSize(QtCore.QSize(32, 32))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.menu.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.logo)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 32))
        self.label.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label.setSizeIncrement(QtCore.QSize(0, 0))
        self.label.setObjectName("label")
        self.menu.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.title.addLayout(self.menu)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setSpacing(7)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.minimum = QtWidgets.QPushButton(self.centralwidget)
        self.minimum.setMinimumSize(QtCore.QSize(32, 32))
        self.minimum.setMaximumSize(QtCore.QSize(32, 32))
        self.minimum.setObjectName("minimum")
        self.horizontalLayout_4.addWidget(self.minimum)
        self.maxmum = QtWidgets.QPushButton(self.centralwidget)
        self.maxmum.setEnabled(False)
        self.maxmum.setMinimumSize(QtCore.QSize(32, 32))
        self.maxmum.setMaximumSize(QtCore.QSize(32, 32))
        self.maxmum.setObjectName("maxmum")
        self.horizontalLayout_4.addWidget(self.maxmum)
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        self.quit.setMinimumSize(QtCore.QSize(32, 32))
        self.quit.setMaximumSize(QtCore.QSize(32, 32))
        self.quit.setObjectName("quit")
        self.horizontalLayout_4.addWidget(self.quit)
        self.title.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.title, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.file_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.file_dir.setText("")
        self.file_dir.setObjectName("file_dir")
        self.horizontalLayout.addWidget(self.file_dir)
        self.btn_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_file.setObjectName("btn_file")
        self.horizontalLayout.addWidget(self.btn_file)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.res_dir = QtWidgets.QLineEdit(self.centralwidget)
        self.res_dir.setObjectName("res_dir")
        self.horizontalLayout_3.addWidget(self.res_dir)
        self.btn_res = QtWidgets.QPushButton(self.centralwidget)
        self.btn_res.setObjectName("btn_res")
        self.horizontalLayout_3.addWidget(self.btn_res)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.scan = QtWidgets.QWidget()
        self.scan.setObjectName("scan")
        self.tab1 = QtWidgets.QWidget(self.scan)
        self.tab1.setGeometry(QtCore.QRect(10, 10, 981, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1.sizePolicy().hasHeightForWidth())
        self.tab1.setSizePolicy(sizePolicy)
        self.tab1.setObjectName("tab1")
        self.formLayout = QtWidgets.QFormLayout(self.tab1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tab1)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 240))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 711, 171))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.dic_php = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.dic_php.setObjectName("dic_php")
        self.horizontalLayout_5.addWidget(self.dic_php)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.dic_session = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.dic_session.setObjectName("dic_session")
        self.horizontalLayout_6.addWidget(self.dic_session)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.dic_key = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.dic_key.setObjectName("dic_key")
        self.horizontalLayout_7.addWidget(self.dic_key)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.dic_pass = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.dic_pass.setObjectName("dic_pass")
        self.horizontalLayout_8.addWidget(self.dic_pass)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(750, 20, 171, 161))
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.btn_dic = QtWidgets.QPushButton(self.groupBox)
        self.btn_dic.setGeometry(QtCore.QRect(790, 150, 93, 28))
        self.btn_dic.setObjectName("btn_dic")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.groupBox)
        self.tabWidget.addTab(self.scan, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(12, 9, 971, 271))
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 711, 171))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.red_api = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.red_api.setObjectName("red_api")
        self.horizontalLayout_9.addWidget(self.red_api)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.red_key = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.red_key.setObjectName("red_key")
        self.horizontalLayout_11.addWidget(self.red_key)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.red_pass = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.red_pass.setObjectName("red_pass")
        self.horizontalLayout_12.addWidget(self.red_pass)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(750, 20, 171, 161))
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.btn_red = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_red.setGeometry(QtCore.QRect(790, 150, 93, 28))
        self.btn_red.setObjectName("btn_red")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(12, 9, 971, 271))
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 20, 711, 171))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.ops_api = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.ops_api.setObjectName("ops_api")
        self.horizontalLayout_10.addWidget(self.ops_api)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.ops_key = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.ops_key.setObjectName("ops_key")
        self.horizontalLayout_13.addWidget(self.ops_key)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_14.addWidget(self.label_15)
        self.ops_pass = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.ops_pass.setObjectName("ops_pass")
        self.horizontalLayout_14.addWidget(self.ops_pass)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(750, 20, 171, 161))
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.btn_ops = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_ops.setGeometry(QtCore.QRect(790, 150, 93, 28))
        self.btn_ops.setObjectName("btn_ops")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(20, 0, 951, 291))
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout_2.addWidget(self.tabWidget, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "辅种配置"))
        self.minimum.setText(_translate("MainWindow", "-"))
        self.maxmum.setText(_translate("MainWindow", "□"))
        self.quit.setText(_translate("MainWindow", "×"))
        self.label_2.setText(_translate("MainWindow", "文件路径:"))
        self.btn_file.setText(_translate("MainWindow", "浏览"))
        self.label_3.setText(_translate("MainWindow", "种子路径:"))
        self.btn_res.setText(_translate("MainWindow", "浏览"))
        self.groupBox.setTitle(_translate("MainWindow", "参数"))
        self.label_4.setText(_translate("MainWindow", "PHPSESSID:"))
        self.label_5.setText(_translate("MainWindow", "session:"))
        self.label_6.setText(_translate("MainWindow", "authkey:"))
        self.label_7.setText(_translate("MainWindow", "torrent_pass:"))
        self.label_8.setText(_translate("MainWindow", "authkey和torrent_pass请随便复制一个种子的下载链接，里面有"))
        self.btn_dic.setText(_translate("MainWindow", "生成"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.scan), _translate("MainWindow", "dicmusic"))
        self.groupBox_2.setTitle(_translate("MainWindow", "参数"))
        self.label_9.setText(_translate("MainWindow", "api_key"))
        self.label_11.setText(_translate("MainWindow", "authkey:"))
        self.label_12.setText(_translate("MainWindow", "torrent_pass:"))
        self.label_13.setText(_translate("MainWindow", "authkey和torrent_pass请随便复制一个种子的下载链接，里面有"))
        self.btn_red.setText(_translate("MainWindow", "生成"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "red"))
        self.groupBox_3.setTitle(_translate("MainWindow", "参数"))
        self.label_10.setText(_translate("MainWindow", "api_key"))
        self.label_14.setText(_translate("MainWindow", "authkey:"))
        self.label_15.setText(_translate("MainWindow", "torrent_pass:"))
        self.label_16.setText(_translate("MainWindow", "authkey和torrent_pass请随便复制一个种子的下载链接，里面有"))
        self.btn_ops.setText(_translate("MainWindow", "生成"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "ops"))
        self.label_17.setText(_translate("MainWindow", "本程序为鱼佬的gz站脚本适配了Windows-gui界面，独立生成配置、bat批处理文件，未改动鱼佬源码 源代码:https://github.com/qfishpear/fishrss release文件包含自动安装依赖库的脚本（fishrss所需），打包好的本程序exe，安装好pip的Windows系统可直接使用。其中reseed.py及其依赖部分为引用源码（辅种功能），感谢发布者。 免责声明：本程序仅为gui界面生成配置文件，未改动fishrss源码，可直接下载源码、安装pyqt5后运行，不对任何使用后果负责，使用软件视为自动同意此声明"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "声明"))

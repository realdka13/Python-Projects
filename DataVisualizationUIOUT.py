# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataVisualization.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1517, 1241)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.DataArea = QtWidgets.QVBoxLayout()
        self.DataArea.setObjectName("DataArea")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setObjectName("openGLWidget")
        self.DataArea.addWidget(self.openGLWidget)
        self.GraphArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GraphArea.sizePolicy().hasHeightForWidth())
        self.GraphArea.setSizePolicy(sizePolicy)
        self.GraphArea.setMaximumSize(QtCore.QSize(16777215, 300))
        self.GraphArea.setWidgetResizable(True)
        self.GraphArea.setObjectName("GraphArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1289, 298))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.GraphArea.setWidget(self.scrollAreaWidgetContents_2)
        self.DataArea.addWidget(self.GraphArea)
        self.gridLayout.addLayout(self.DataArea, 0, 1, 1, 1)
        self.ModeSwitchTabs = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ModeSwitchTabs.sizePolicy().hasHeightForWidth())
        self.ModeSwitchTabs.setSizePolicy(sizePolicy)
        self.ModeSwitchTabs.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ModeSwitchTabs.setBaseSize(QtCore.QSize(0, 0))
        self.ModeSwitchTabs.setAutoFillBackground(False)
        self.ModeSwitchTabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.ModeSwitchTabs.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.ModeSwitchTabs.setIconSize(QtCore.QSize(16, 16))
        self.ModeSwitchTabs.setElideMode(QtCore.Qt.ElideNone)
        self.ModeSwitchTabs.setUsesScrollButtons(False)
        self.ModeSwitchTabs.setTabsClosable(False)
        self.ModeSwitchTabs.setMovable(False)
        self.ModeSwitchTabs.setTabBarAutoHide(False)
        self.ModeSwitchTabs.setObjectName("ModeSwitchTabs")
        self.liveTab_Button = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liveTab_Button.sizePolicy().hasHeightForWidth())
        self.liveTab_Button.setSizePolicy(sizePolicy)
        self.liveTab_Button.setObjectName("liveTab_Button")
        self.formLayout_5 = QtWidgets.QFormLayout(self.liveTab_Button)
        self.formLayout_5.setObjectName("formLayout_5")
        self.startStop_Icon = QtWidgets.QLabel(self.liveTab_Button)
        self.startStop_Icon.setObjectName("startStop_Icon")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.startStop_Icon)
        self.startStop_Button = QtWidgets.QPushButton(self.liveTab_Button)
        self.startStop_Button.setObjectName("startStop_Button")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.startStop_Button)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.formLayout_5.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.formLayout_4)
        self.ModeSwitchTabs.addTab(self.liveTab_Button, "")
        self.analysisTab_Button = QtWidgets.QWidget()
        self.analysisTab_Button.setObjectName("analysisTab_Button")
        self.formLayout_8 = QtWidgets.QFormLayout(self.analysisTab_Button)
        self.formLayout_8.setObjectName("formLayout_8")
        self.selectFile_Button = QtWidgets.QToolButton(self.analysisTab_Button)
        self.selectFile_Button.setObjectName("selectFile_Button")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.selectFile_Button)
        self.selectFileText = QtWidgets.QLabel(self.analysisTab_Button)
        self.selectFileText.setObjectName("selectFileText")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.selectFileText)
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setObjectName("formLayout_7")
        self.formLayout_8.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.formLayout_7)
        self.ModeSwitchTabs.addTab(self.analysisTab_Button, "")
        self.gridLayout.addWidget(self.ModeSwitchTabs, 0, 0, 1, 1)
        self.ModeSwitchTabs.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1517, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.menuFile.addAction(self.actionImport)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.ModeSwitchTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IMU Data Visualization"))
        self.startStop_Icon.setText(_translate("MainWindow", "<html><head/><body><p>Icon</p></body></html>"))
        self.startStop_Button.setText(_translate("MainWindow", "Start_Stop_Sim"))
        self.ModeSwitchTabs.setTabText(self.ModeSwitchTabs.indexOf(self.liveTab_Button), _translate("MainWindow", "Live"))
        self.selectFile_Button.setText(_translate("MainWindow", "..."))
        self.selectFileText.setText(_translate("MainWindow", "Select File"))
        self.ModeSwitchTabs.setTabText(self.ModeSwitchTabs.indexOf(self.analysisTab_Button), _translate("MainWindow", "Analysis"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

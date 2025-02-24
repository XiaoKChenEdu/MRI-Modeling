from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        # Main layout
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        
        # File selection group
        self.groupFiles = QtWidgets.QGroupBox("File Selection")
        self.filesLayout = QtWidgets.QGridLayout()
        
        # Volume file
        self.btnLoadVolume = QtWidgets.QPushButton("Load Volume")
        self.labelVolumePath = QtWidgets.QLabel("No file selected")
        self.filesLayout.addWidget(self.btnLoadVolume, 0, 0)
        self.filesLayout.addWidget(self.labelVolumePath, 0, 1)
        
        # Heart file
        self.btnLoadHeart = QtWidgets.QPushButton("Load Heart")
        self.labelHeartPath = QtWidgets.QLabel("No file selected")
        self.filesLayout.addWidget(self.btnLoadHeart, 1, 0)
        self.filesLayout.addWidget(self.labelHeartPath, 1, 1)
        
        # Lung file
        self.btnLoadLung = QtWidgets.QPushButton("Load Lung")
        self.labelLungPath = QtWidgets.QLabel("No file selected")
        self.filesLayout.addWidget(self.btnLoadLung, 2, 0)
        self.filesLayout.addWidget(self.labelLungPath, 2, 1)
        
        # Output directory
        self.btnSelectOutput = QtWidgets.QPushButton("Select Output Directory")
        self.labelOutputPath = QtWidgets.QLabel("./output_stl")
        self.filesLayout.addWidget(self.btnSelectOutput, 3, 0)
        self.filesLayout.addWidget(self.labelOutputPath, 3, 1)
        
        self.groupFiles.setLayout(self.filesLayout)
        self.mainLayout.addWidget(self.groupFiles)
        
        # Visualization group
        self.groupVisualize = QtWidgets.QGroupBox("Visualization")
        self.visualizeLayout = QtWidgets.QHBoxLayout()
        
        self.btnViewSkin = QtWidgets.QPushButton("View Skin")
        self.btnViewBone = QtWidgets.QPushButton("View Bone")
        self.btnViewHeartLung = QtWidgets.QPushButton("View Heart & Lung")
        self.btnViewSkinHeartLung = QtWidgets.QPushButton("View Skin, Heart & Lung")
        self.btnViewAll = QtWidgets.QPushButton("View All")
        
        self.visualizeLayout.addWidget(self.btnViewSkin)
        self.visualizeLayout.addWidget(self.btnViewBone)
        self.visualizeLayout.addWidget(self.btnViewHeartLung)
        self.visualizeLayout.addWidget(self.btnViewSkinHeartLung)
        self.visualizeLayout.addWidget(self.btnViewAll)
        
        self.groupVisualize.setLayout(self.visualizeLayout)
        self.mainLayout.addWidget(self.groupVisualize)
        
        # Export group
        self.groupExport = QtWidgets.QGroupBox("Export STL")
        self.exportLayout = QtWidgets.QGridLayout()
        
        self.labelFilename = QtWidgets.QLabel("Filename:")
        self.lineFilename = QtWidgets.QLineEdit()
        self.labelDecimation = QtWidgets.QLabel("Decimation (%):")
        self.spinDecimation = QtWidgets.QSpinBox()
        self.spinDecimation.setRange(1, 100)
        self.spinDecimation.setValue(50)
        self.btnExportSTL = QtWidgets.QPushButton("Export STL")
        
        self.exportLayout.addWidget(self.labelFilename, 0, 0)
        self.exportLayout.addWidget(self.lineFilename, 0, 1)
        self.exportLayout.addWidget(self.labelDecimation, 1, 0)
        self.exportLayout.addWidget(self.spinDecimation, 1, 1)
        self.exportLayout.addWidget(self.btnExportSTL, 2, 0, 1, 2)
        
        self.groupExport.setLayout(self.exportLayout)
        self.mainLayout.addWidget(self.groupExport)
        
        self.btnCloseViz = QtWidgets.QPushButton(self.centralwidget)
        self.btnCloseViz.setObjectName("btnCloseViz")
        self.mainLayout.addWidget(self.btnCloseViz)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        
        # Status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MRI Visualization Tool"))
        self.btnCloseViz.setText(_translate("MainWindow", "Close Visualization"))

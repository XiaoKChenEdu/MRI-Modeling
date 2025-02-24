import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from utils.gui_ui import Ui_MainWindow
from utils.visualize_volume_functions import (visualize_skin, visualize_bone, visualize_heart_lung,
                            visualize_skin_heart_lung, visualize_skin_bone_heart_lung,
                            export_stl)
from vedo import close

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Initialize variables
        self.volume_path = ""
        self.heart_path = ""
        self.lung_path = ""
        self.output_dir = "./output_stl"
        
        # Connect buttons
        self.ui.btnLoadVolume.clicked.connect(self.load_volume)
        self.ui.btnLoadHeart.clicked.connect(self.load_heart)
        self.ui.btnLoadLung.clicked.connect(self.load_lung)
        self.ui.btnSelectOutput.clicked.connect(self.select_output)
        
        self.ui.btnViewSkin.clicked.connect(self.view_skin)
        self.ui.btnViewBone.clicked.connect(self.view_bone)
        self.ui.btnViewHeartLung.clicked.connect(self.view_heart_lung)
        self.ui.btnViewSkinHeartLung.clicked.connect(self.view_skin_heart_lung)
        self.ui.btnViewAll.clicked.connect(self.view_all)
        self.ui.btnExportSTL.clicked.connect(self.export_stl_files)
        self.ui.btnCloseViz.clicked.connect(self.close_visualization)

    def load_volume(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Select Volume File", "", "NIFTI files (*.nii.gz)")
        if fname:
            self.volume_path = fname
            self.ui.labelVolumePath.setText(fname)

    def load_heart(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Select Heart File", "", "NIFTI files (*.nii.gz)")
        if fname:
            self.heart_path = fname
            self.ui.labelHeartPath.setText(fname)

    def load_lung(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Select Lung File", "", "NIFTI files (*.nii.gz)")
        if fname:
            self.lung_path = fname
            self.ui.labelLungPath.setText(fname)

    def select_output(self):
        dirname = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if dirname:
            self.output_dir = dirname
            self.ui.labelOutputPath.setText(dirname)

    def check_volume(self):
        if not self.volume_path:
            QMessageBox.warning(self, "Warning", "Please load a volume file first!")
            return False
        return True

    def check_heart_lung(self):
        if not self.heart_path or not self.lung_path:
            QMessageBox.warning(self, "Warning", "Please load both heart and lung files!")
            return False
        return True

    def view_skin(self):
        if self.check_volume():
            visualize_skin(self.volume_path)

    def view_bone(self):
        if self.check_volume():
            visualize_bone(self.volume_path)

    def view_heart_lung(self):
        if self.check_heart_lung():
            visualize_heart_lung(self.heart_path, self.lung_path)

    def view_skin_heart_lung(self):
        if self.check_volume() and self.check_heart_lung():
            visualize_skin_heart_lung(self.volume_path, self.heart_path, self.lung_path)

    def view_all(self):
        if self.check_volume() and self.check_heart_lung():
            visualize_skin_bone_heart_lung(self.volume_path, self.heart_path, self.lung_path)

    def export_stl_files(self):
        if self.check_volume() and self.check_heart_lung():
            decimation = self.ui.spinDecimation.value() / 100.0
            filename = self.ui.lineFilename.text() or "volume"
            try:
                export_stl(filename, self.volume_path, self.heart_path, self.lung_path, 
                          self.output_dir, decimation_factor=decimation)
                QMessageBox.information(self, "Success", "STL files exported successfully!")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to export STL files: {str(e)}")

    def close_visualization(self):
        close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

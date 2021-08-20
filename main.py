from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.uic import loadUi

import sys, main_images_rc, sqlite3

class MainWindow(QMainWindow):
    def  __init__(self):
        super(MainWindow, self).__init__()
        loadUi("assets/mainWindow.ui", self)

        self.show()

app = QApplication(sys.argv)
mainWindow = MainWindow()
sys.exit(app.exec_())
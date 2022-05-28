#GUI imports
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

#initiallize GUI application
app=QApplication(sys.argv)

#window and settings
window=QWidget()
window.setWindowTitle("Who wants to be a programmer?")
window.setFixedWidth(1000)
window.setStyleSheet("background: #161219;")


grid=QGridLayout()
#logo widget
image=QPixmap("logo.png")
logo=QLabel()
logo.setPixmap(image)
grid.addWidget(logo, 0, 0)
window.setLayout(grid)
 
window.show()
#terminate the app
sys.exit(app.exec())

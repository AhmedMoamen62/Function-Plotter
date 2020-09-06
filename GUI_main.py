from PySide2.QtWidgets import QApplication,QWidget,QVBoxLayout,QGroupBox,QPushButton,QGridLayout,QLineEdit
from PySide2.QtGui import QIcon,QPalette,QColor,QFont
from PySide2.QtCore import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Function Plotter")
        self.setGeometry(500,400,400,200)

        palette = self.palette()
        palette.setColor(QPalette.Window,QColor(255,150,0))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        self.setMinimumHeight(200)
        self.setMinimumWidth(400)
        # self.setMaximumHeight(600)
        # self.setMaximumWidth(800)

        self.setIcon()

        self.createGridLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        vbox.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.setLayout(vbox)

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def createGridLayout(self):
        self.groupBox = QGroupBox("Please fill next sections")
        self.groupBox.setFont(QFont("Helvetica", 12))
        self.groupBox.setMaximumWidth(400)
        self.groupBox.setMaximumHeight(200)
        gridLayout = QGridLayout()
        gridLayout.setSpacing(10)

        equationInput = QLineEdit()
        equationInput.setMaximumHeight(30)
        equationInput.setMaximumWidth(175)
        equationInput.setPlaceholderText("Enter your equation")
        gridLayout.addWidget(equationInput, 0, 0)

        maxInput = QLineEdit()
        maxInput.setMaximumHeight(30)
        maxInput.setMaximumWidth(175)
        maxInput.setPlaceholderText("Enter maximum value")
        gridLayout.addWidget(maxInput, 1, 0)

        minInput = QLineEdit()
        minInput.setMaximumHeight(30)
        minInput.setMaximumWidth(175)
        minInput.setPlaceholderText("Enter minimum value")
        gridLayout.addWidget(minInput, 1, 1)

        plotButton = QPushButton("Plot")
        plotButton.setStyleSheet("background-color: green")
        plotButton.setIcon(QIcon("curve.png"))
        plotButton.setMaximumHeight(30)
        plotButton.setMaximumWidth(75)
        gridLayout.addWidget(plotButton,2,0)

        self.setLayout(gridLayout)
        self.groupBox.setLayout(gridLayout)

app = QApplication(sys.argv)
window = Window()
window.show()

app.exec_()
sys.exit(0)
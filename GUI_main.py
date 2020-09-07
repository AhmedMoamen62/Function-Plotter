from PySide2.QtWidgets import QApplication,QWidget,QVBoxLayout,QGroupBox,QPushButton,QGridLayout,QLineEdit,QMessageBox
from PySide2.QtGui import QIcon,QPalette,QColor,QFont
from PySide2.QtCore import Qt
from PySide2 import QtGui
from functionCalculator import *
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
        self.center()

        self.createGridLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        vbox.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.setLayout(vbox)

    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    def readData(self):
        equation = self.equationInput.text()
        if equation == '':
            self.aboutBox("Empty section","Please enter an equation")
            return
        equation = removeSpaces(equation)
        varName, _ = getVariableName(equation)
        check,error = checkVarName(equation,varName)
        if not check:
            self.aboutBox("Wrong equation", error)
            return

        maxValue = self.maxInput.text()
        if maxValue == '':
            self.aboutBox("Empty section", "Please enter maximum value")
            return
        try:
            maxValue = float(maxValue)
        except ValueError:
            self.aboutBox("Wrong range","Invalid value for maximum, please enter float or integer value")
            return
        minValue = self.minInput.text()
        if minValue == '':
            self.aboutBox("Empty section", "Please enter minimum value")
            return
        try:
            minValue = float(minValue)
        except ValueError:
            self.aboutBox("Wrong range","Invalid value for minimum, please enter float or integer value")
            return

        if minValue >= maxValue:
            self.aboutBox("Wrong range", "Your maximum value should be greater than minimum")
            return

        testEquation = replaceVar(equation, varName,str(maxValue))
        ops = trimTerms(testEquation)
        testVal,error = functionCalculator(ops)

        if error != None:
            self.aboutBox("Evaluation error", error)
            return

        self.evaluateFunction(equation,maxValue,minValue,varName)

    def aboutBox(self,title,error):
        QMessageBox.about(self,title,error)


    def evaluateFunction(self,equation,maxVal,minVal,varName):
        x = list(range(minVal,maxVal,1))
        fx = []
        for number in x:
            equation = replaceVar(equation,varName,str(number))
            ops = trimTerms(equation)
            val , _ = functionCalculator(ops)
            fx.append(val)

        print(fx)

    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def createGridLayout(self):
        self.groupBox = QGroupBox("Please fill next sections")
        self.groupBox.setFont(QFont("Helvetica", 12))
        self.groupBox.setMaximumWidth(400)
        self.groupBox.setMaximumHeight(200)
        gridLayout = QGridLayout()
        gridLayout.setSpacing(10)

        self.equationInput = QLineEdit()
        self.equationInput.setMaximumHeight(30)
        self.equationInput.setMaximumWidth(175)
        self.equationInput.setPlaceholderText("Enter your equation")
        gridLayout.addWidget(self.equationInput, 0, 0)

        self.maxInput = QLineEdit()
        self.maxInput.setMaximumHeight(30)
        self.maxInput.setMaximumWidth(175)
        self.maxInput.setPlaceholderText("Enter maximum value")
        gridLayout.addWidget(self.maxInput, 1, 0)

        self.minInput = QLineEdit()
        self.minInput.setMaximumHeight(30)
        self.minInput.setMaximumWidth(175)
        self.minInput.setPlaceholderText("Enter minimum value")
        gridLayout.addWidget(self.minInput, 1, 1)

        plotButton = QPushButton("Plot")
        plotButton.setStyleSheet("background-color: green")
        plotButton.setIcon(QIcon("curve.png"))
        plotButton.setMaximumHeight(30)
        plotButton.setMaximumWidth(75)
        plotButton.clicked.connect(self.readData)
        gridLayout.addWidget(plotButton,2,0)

        self.setLayout(gridLayout)
        self.groupBox.setLayout(gridLayout)

app = QApplication(sys.argv)
window = Window()
window.show()

app.exec_()
sys.exit(0)
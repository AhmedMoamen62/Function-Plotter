# import required library for GUI
from PySide2.QtWidgets import QApplication,QWidget,QVBoxLayout,QGroupBox,QPushButton,QGridLayout,QLineEdit,QMessageBox
from PySide2.QtGui import QIcon,QPalette,QColor,QFont
from PySide2.QtCore import Qt
from PySide2 import QtGui

# import matplotlib backend and figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

# import logic functions to check wrong inputs and evaluate the equation
from functionCalculator import *

# import numpy to create f(x) list support float numbers
import numpy as np

# import sys to run the application
import sys

class Window(QWidget):
    def __init__(self):
        # call the constructor of the parent (QWidget)
        super().__init__()

        # check if it the first time for user to plot
        self.firstTime = False

        # set title  and geometry for the window
        self.setWindowTitle("Function Plotter")
        self.setGeometry(500,400,400,200)

        # give orange background to the window
        palette = self.palette()
        palette.setColor(QPalette.Window,QColor(150,150,150))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # set minimum width and height for the window
        self.setMinimumHeight(200)
        self.setMinimumWidth(400)
        self.setMaximumHeight(200)
        self.setMaximumWidth(400)

        # set icon for the application at run time and center the application window with the primary screen
        self.setIcon()
        self.center()

        # setup the grid layout design and components
        self.createGridLayout()
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.groupBox)
        self.vbox.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.setLayout(self.vbox)

    # set icon for the application
    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    # reading the data from text input and apply check tests
    def readData(self):
        # read the equation and check if there is an actual input
        equation = self.equationInput.text()
        if equation == '':
            self.aboutBox("Empty section","Please enter an equation")
            return
        # remove spaces from the equation and check if the equation has valid variable name
        equation = removeSpaces(equation)
        varName, _ = getVariableName(equation)
        check,error = checkVarName(equation,varName)
        if not check:
            self.aboutBox("Wrong equation", error)
            return

        # check min and max value if it's a real number and the text input isn't empty
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

        # the max value should be greater than min value
        if minValue >= maxValue:
            self.aboutBox("Wrong range", "Your maximum value should be greater than minimum")
            return

        # process the equation by trying to solve it with max value and check if there is error with operatos, operands or parentheses
        ops = trimTerms(equation,varName)
        temp_ops = replaceVar(ops,varName,str(maxValue))
        testVal,error = functionCalculator(temp_ops)

        if error != None:
            self.aboutBox("Evaluation error", error)
            return

        # function to evaluate f(x) array and return f(x) and x lists to be plotted
        fx,x = self.evaluateFunction(ops,maxValue,minValue,varName)

        # plot the graph
        self.plotGraph(fx,x,varName)

    def plotGraph(self,fx,x,varName):
        # remove the old figure if user request another equation
        if self.firstTime:
            self.fig.clear()
            self.vbox.removeWidget(self.toolbar)
            self.vbox.removeWidget(self.canvas)

        # set first time to be True, to remove the old figures
        self.firstTime = True

        # set the figure and toolbar and add it to the window
        self.fig = Figure(figsize=(7, 5), dpi=65, facecolor=(1, 1, 1), edgecolor=(0, 0, 0))
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.vbox.addWidget(self.toolbar)
        self.vbox.addWidget(self.canvas)

        # set new geometry to the window to fit the graph
        self.resize(400,500)
        self.setMinimumHeight(500)
        self.setMaximumHeight(500)

        # plot the graph and set the labels
        self.ax = self.fig.add_subplot(111)
        self.ax.plot(x,fx)
        if varName == '':
            varName = 'x'
        self.ax.set_xlabel(varName)
        self.ax.set_ylabel('f(' + varName + ')')

    # QMessageBox which shows any error for the user
    def aboutBox(self,title,error):
        QMessageBox.about(self,title,error)


    def evaluateFunction(self,ops,maxVal,minVal,varName):
        # make array with start = minVal, end, maxVal and step for 0.25 for some accuracy
        x = np.arange(minVal,maxVal,0.25)
        fx = []
        # loop over each number(i) and evaluate f(i) then add it to f(x) list
        for number in x:
            temp_ops = replaceVar(ops,varName,number)
            val , _ = functionCalculator(temp_ops)
            fx.append(val)

        return fx,x

    # to center the application window at the beginning
    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def createGridLayout(self):
        # make group box with headline then add the gridlayout to it
        self.groupBox = QGroupBox("Please fill next sections")
        self.groupBox.setFont(QFont("Helvetica", 12))
        self.groupBox.setMaximumWidth(400)
        self.groupBox.setMaximumHeight(200)
        # create gridlayout with spacing between columns and rows
        gridLayout = QGridLayout()
        gridLayout.setSpacing(10)

        # set equation text input
        self.equationInput = QLineEdit()
        self.equationInput.setMaximumHeight(30)
        #self.equationInput.setMaximumWidth(175)
        self.equationInput.setPlaceholderText("Enter your equation")
        gridLayout.addWidget(self.equationInput, 0, 0,1,0)

        # set max value text input
        self.maxInput = QLineEdit()
        self.maxInput.setMaximumHeight(30)
        self.maxInput.setMaximumWidth(175)
        self.maxInput.setPlaceholderText("Enter maximum value")
        gridLayout.addWidget(self.maxInput, 1, 0)

        # set min value text input
        self.minInput = QLineEdit()
        self.minInput.setMaximumHeight(30)
        self.minInput.setMaximumWidth(175)
        self.minInput.setPlaceholderText("Enter minimum value")
        gridLayout.addWidget(self.minInput, 1, 1)

        # set Plot push button with green color and an icon
        plotButton = QPushButton("Plot")
        plotButton.setStyleSheet("background-color: green")
        plotButton.setIcon(QIcon("curve.png"))
        plotButton.setMaximumHeight(30)
        plotButton.setMaximumWidth(75)
        # when button is clicked, call readData and then will plot the function
        plotButton.clicked.connect(self.readData)
        gridLayout.addWidget(plotButton,2,0)

        # add gridlayout to the group box
        self.setLayout(gridLayout)
        self.groupBox.setLayout(gridLayout)

# run the application and show the window
app = QApplication(sys.argv)
window = Window()
window.show()

app.exec_()
sys.exit(0)
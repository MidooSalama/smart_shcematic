import sys
from PySide2 import QtWidgets, QtCore, QtGui

import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

import schematicDrawing


class MplCanvas(FigureCanvasQTAgg):
    # the Canvas class to load the figure of the schematic
    def __init__(self):
        self.schem = schematicDrawing.Schematic()
        fig = self.schem.figure.fig
        super(MplCanvas, self).__init__(fig)



class SchematicApp(QtWidgets.QMainWindow):
    # the main class to build the GUI window
    def __init__(self):
        super().__init__()
        # build and initialize the geometry
        self.setWindowTitle("Schematic")
        self.setGeometry(100, 200, 650, 600)

        # create the two main containers of the GUI
        self.canvas = MplCanvas()
        self.createInputGroupBox()

        # organize the GUI interface
        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.canvas, 0, 0)
        grid.addWidget(self.inputGroupBox, 1, 0)
        widget = QtWidgets.QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

        # connect the signals and slots
        self.comboBox.activated.connect(self.reColorElement)

    def reColorElement(self):
        # redraw the schematic to change the color of the selected elements
        element = self.comboBox.currentText()
        self.canvas.schem.redraw(element)
        self.canvas.figure = self.canvas.schem.figure.fig
        self.canvas.draw()



    def createInputGroupBox(self):
        # this function build and organize the container of the input data
        self.inputGroupBox = QtWidgets.QGroupBox('choose element name', self)
        grid = QtWidgets.QGridLayout()

        self.labelName = QtWidgets.QLabel("Element Name: ")

        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItems(['', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6'])

        grid.addWidget(self.labelName, 0, 0)
        grid.addWidget(self.comboBox, 0, 1)

        self.inputGroupBox.setLayout(grid)




if __name__ == '__main__':
    # start the main procedure of executing the application
    app = QtWidgets.QApplication(sys.argv)
    myApp = SchematicApp()
    myApp.show()
    app.exec_()
import sys
from PySide2 import QtWidgets, QtCore, QtGui

import matplotlib
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

import schematicDrawing


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self):
        self.schem = schematicDrawing.Schematic()
        fig = self.schem.figure.fig
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)



class SchematicApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Schematic")
        self.setGeometry(100, 200, 650, 600)


        self.canvas = MplCanvas()
        self.createInputGroupBox()


        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.canvas, 0, 0)
        grid.addWidget(self.inputGroupBox, 1, 0)
        widget = QtWidgets.QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

        self.comboBox.activated.connect(self.reColorElement)

    def reColorElement(self):
        element = self.comboBox.currentText()
        self.canvas.axes.cla()
        self.canvas.schem.redraw(element)
        self.canvas.figure=self.canvas.schem.figure.fig
        self.canvas.draw()



    def createInputGroupBox(self):
        self.inputGroupBox = QtWidgets.QGroupBox('choose element name', self)
        grid = QtWidgets.QGridLayout()

        self.labelName = QtWidgets.QLabel("Element Name: ")

        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItems(['', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6'])

        grid.addWidget(self.labelName, 0, 0)
        grid.addWidget(self.comboBox, 0, 1)

        self.inputGroupBox.setLayout(grid)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myApp = SchematicApp()
    myApp.show()
    app.exec_()
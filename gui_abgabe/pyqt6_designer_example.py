import sys
from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PIL import Image
import PIL
import os
import pathlib
from pathlib import Path
from Mandelbrot.run_video import main

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Mit progress-bar
        uic.loadUi("gui_data_progress_bar.ui", self)
        self.setMouseTracking(True)
        # Ohne progress-bar
        # uic.loadUi("gui_data.ui", self)

        self.resetValue = False
        self.save_file = False

        # Widgets from MainWIndow
        # Wenn der 'pushButton' geklickt wird
        self.pushButton.clicked.connect(self.handleButtonClick)
        self.setWindowTitle("Mandelbrot Zoom")
        self.setWindowIcon(QIcon("Icon.jpg"))  # Place an icon and import QIcon

        # External windows
        self.dialogWindow = DialogWindow()
        self.dialogWindow.yes_pushButton.clicked.connect(self.handleClickYes)
        self.dialogWindow.no_pushButton.clicked.connect(self.handleClickNo)
        self.show()

        # load the Picture into the Graphicsview
        self.label = QGraphicsView(self)
        pix = QPixmap('Icon.jpg')
        item = QtWidgets.QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene(self)
        scene.addItem(item)
        self.graphicsView.setScene(scene)

        # zoom_faktor
        self.zoom_faktor_einstellen.setValue(1.2)
        self.zoom_faktor_einstellen.setMaximum(4)
        self.zoom_faktor_einstellen.setMinimum(1.2)
        self.zoom_faktor_einstellen.setSingleStep(0.1)
        value_zoom = self.zoom_faktor_einstellen.value()


        # tooltips
        self.zoom_faktor_einstellen.setToolTip('Zoomfaktor einstellen')
        self.pushButton.setToolTip('reseet des Zommfaktor')
        self.graphicsView.setToolTip('Bild des Mandelbrot')
        self.progressBar.setToolTip('Fortschritt der Berechnung')

        #actionSave_as_png
        self.actionSave_as_png.triggered.connect(self.handlesave)
        self.actionquit.triggered.connect(self.closeEvent)

#TODO Aktuellestes bild herausfinden
    def handlesave(self):
        # get the current path
        path = (pathlib.Path(__file__).parent.absolute())
        """print('path hat ', type(path))
        print(path)
        print(path.parent)"""
        # go one level back and change to Mandelbrot
        new_path = path.parent / 'Mandelbrot'
        print(new_path)
        im1 = Image.open(new_path / 'eye0001.png')
        im1.save("mandelbrot1.png")
        self.save_file = True

#TODO Fragen wenn bild noch nicht gespeichert ob man es no will
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        button = QMessageBox.question(
            self,
            "Closeing App",
            "Wollen Sie wirklich das Programm verlassen??",
            buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            defaultButton=QMessageBox.StandardButton.No,
        )

        if button == QMessageBox.StandardButton.Yes:
            if self.save_file:
                # TODO add a new Window
            a0.accept()
        else:
            a0.ignore()

    def handleClickYes(self):
        self.resetValue = True
        self.dialogWindow.close()

    def handleClickNo(self):
        self.resetValue = False
        self.dialogWindow.close()

    def mouseDoubleClickEventMoveEvent(self, event):
        print("hih")
        """global Mouse_X
        global Mouse_Y
        Mouse_X = event.x()
        Mouse_Y = event.y()
        print("mouse X,Y: {},{}" .format(Mouse_X, Mouse_Y))"""

    def handleButtonClick(self):
        self.dialogWindow.exec()
        if self.resetValue:
            self.zoom_faktor_einstellen.setValue(1.2)
            self.resetValue = False

class DialogWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("dialog.ui", self)
        self.setWindowIcon(QIcon("Icon.jpg"))  # Place an icon and import QIcon
        # uic.loadUi("gui_data.ui", self)


        # self.pushButton.clicked.connect(self.close)


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
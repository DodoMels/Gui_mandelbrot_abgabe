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

        # Variabel
        self.resetValue = False
        self.save_file = False
        self.image_counter = 0
        self.value_zoom = 1.2

        # Widgets from MainWIndow
        # when pushButton is clicked
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
        self.zoom_faktor_einstellen.valueChanged.connect(self.update_zoom_var)

        # tooltips
        self.zoom_faktor_einstellen.setToolTip('Zoomfaktor einstellen')
        self.pushButton.setToolTip('reseet des Zommfaktor')
        self.graphicsView.setToolTip('Bild des Mandelbrot')
        self.progressBar.setToolTip('Fortschritt der Berechnung')

        # actionSave_as_png
        self.actionSave_as_png.triggered.connect(self.handlesave)
        self.actionquit.triggered.connect(self.close)

        # update the zoom var
    def update_zoom_var(self):
        self.value_zoom = self.zoom_faktor_einstellen.value()
        self.value_zoom = round(self.value_zoom, 1)
        print(self.value_zoom)

#TODO Aktuellestes bild herausfinden
        # get the image from path Mandelbrot and save it to path gui_abgabe
    def handlesave(self):
        self.image_counter += 1
        self.image_name = "mandelbrot{}_zoom_faktor{}.png".format(self.image_counter, self.value_zoom)
        print(self.image_name)
        # get the current path
        path = (pathlib.Path(__file__).parent.absolute())
        # go one level back and change to Mandelbrot
        new_path = path.parent / 'Mandelbrot'
        im1 = Image.open(new_path / 'eye0001.png')
        im1.save(self.image_name)
        self.save_file = True
        print(self.save_file)

    #"""
    # Close the application and check if the image is already saved otherwise show window with opportunity to save
    def closeEvent(self, event):
        if not self.save_file:              # when image isn't saved
            print('ich muss noch speichern')
            reply = QMessageBox.question(
                self, "Message",
                "Are you sure you want to quit? Any unsaved work will be lost.",
                QMessageBox.Save | QMessageBox.Close | QMessageBox.Cancel,
                QMessageBox.Save)
            if reply == QMessageBox.Close:
                app.quit()
            if reply == QMessageBox.Save:
                print("ich muss speichern")
                v = self.handlesave()
            else:
                event.ignore()
                print('event ignore')
        else:                               # when image is saved
            print("ich habe schon gespeichert")
            reply = QMessageBox.question(
            self, "Message",
            "Are you sure you want to quit? Any unsaved work will be lost.", QMessageBox.Close | QMessageBox.Cancel)
            if reply == QMessageBox.Close:
                app.quit()
            else:
                event.ignore()
            #"""
    # reset zoomfaktor window when clicked yes
    def handleClickYes(self):
        self.resetValue = True
        self.dialogWindow.close()

    # reset zoomfaktor window when clicked no
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

    # set zoomfaktor back to start value
    def handleButtonClick(self):
        self.dialogWindow.exec()
        if self.resetValue:
            self.zoom_faktor_einstellen.setValue(1.2)
            self.resetValue = False

    # dialogwindow for reset the zoomfaktor
class DialogWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("dialog.ui", self)
        self.setWindowIcon(QIcon("Icon.jpg"))  # Place an icon and import QIcon

app = QApplication(sys.argv)
window = MainWindow()
app.exec()
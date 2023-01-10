import matplotlib.pyplot as plt
import numpy as np

from Mandelbrot.mandelbrot import MandelbrotPatch



class ZoomPlot():

    def __init__(self):
        self._fig = plt.figure()
        self._ax = self._fig.add_subplot(111)
        self._xpress = None
        self._ypress = None
        self._fig.canvas.mpl_connect('button_press_event', self._onpress)
        self._fig.canvas.mpl_connect('button_release_event', self._onrelease)
        self._patch = MandelbrotPatch((-2.2-1.7j, 1.2+1.7j), 1000, 1000)
        self._plot()



    def _plot(self):
        self._patch.calculate_parallel()
        image = self._patch.get_image()
        self._ax.clear()
        self._ax.imshow(image)
        self._fig.canvas.draw()



    def _onpress(self, event):
        if event.button != 1:
            return
        self._xpress = event.xdata
        self._ypress = event.ydata



    def _onrelease(self, event):
        if event.button != 1:
            return
        if self._xpress is None or self._ypress is None:
            return
        self._patch.zoom_image((self._xpress, self._ypress), 2)
        self._plot()

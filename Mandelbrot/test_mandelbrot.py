import numpy as np
import pytest

from Mandelbrot.mandelbrot import MandelbrotPatch



def test_serial_vs_parallel():
    bbox = (-2.2-1.5j, 1.2+1.9j)
    width = 523
    height = 413

    mbp_serial = MandelbrotPatch(bbox, width, height)
    mbp_serial.calculate_serial()
    image_serial = mbp_serial.get_image()

    mbp_parallel = MandelbrotPatch(bbox, width, height)
    mbp_parallel.calculate_serial()
    image_parallel = mbp_parallel.get_image()

    assert np.all(image_serial == image_parallel)

import numpy as np
import matplotlib.pyplot as plt
import multiprocessing

from Mandelbrot.tiles import tile_indices, tile_image, detile_image, tile_bounding_box



class MandelbrotPatch:

    """
    The internal structures of _bbox and _image are aligned in the way
    as shown here:

    0---->
    |
    |      _bbox[0] *----------------
    v               |               |
                    |               |
        rows        |               |
        _image[0]   |               |
        real        |               |
        width       |               |
                    |               |
                    |               |
                    ----------------* _bbox[1]
                        cols
                        _image[1]
                        imag
                        height

    """
    def __init__(self, bbox, width, height):
        self._bbox = np.array(bbox, dtype=complex) # TODO: data type with higher precision?
        if self._bbox[0].real > self._bbox[1].real or \
            self._bbox[0].imag > self._bbox[1].imag:
            raise Exception(f'Provide proper bounding box, not {bbox}')
        if width <= 0 or height <= 0:
             raise Exception(f'Provide proper image dimensions, not {width}/{height}')
        self._image = np.zeros((width, height, 3), np.uint8)



    def get_image(self):
        return np.transpose(self._image, axes=(1, 0, 2))



    def zoom_image(self, image_center, zoom):
        d = self._bbox[1] - self._bbox[0]
        complex_center = self._bbox[0] + complex( \
            (d.real * image_center[0]) / self._image.shape[0], \
            (d.imag * image_center[1]) / self._image.shape[1])
        self.zoom_complex(complex_center, zoom)



    def zoom_complex(self, complex_center, zoom):
        d = self._bbox[1] - self._bbox[0]
        self._bbox[0] = complex_center - (d / (2 * zoom))
        self._bbox[1] = complex_center + (d / (2 * zoom))



    def tile(self, cols, rows):
        row_indices = tile_indices(self._image.shape[0], rows)
        col_indices = tile_indices(self._image.shape[1], cols)
        image_tiles = tile_image(self._image, row_indices, col_indices)
        bbox_tiles = tile_bounding_box(self._bbox, row_indices, col_indices)
        tiles = []
        for it, bt in zip(image_tiles, bbox_tiles):
            tile = MandelbrotPatch(bt, it.shape[0], it.shape[1])
            tile._image = it
            tiles.append(tile)
        return tiles



    def detile(self, cols, rows, tiles):
        if (rows * cols) != len(tiles):
            raise Exception('Dimension error in de-tiling')
        row_indices = tile_indices(self._image.shape[0], rows)
        col_indices = tile_indices(self._image.shape[1], cols)
        image_tiles = [ tile._image for tile in tiles ]
        self._image = detile_image(image_tiles, row_indices, col_indices)



    @staticmethod
    def smooth_color_scalar(n, maxiter):
        t = (1.0 * n) / maxiter
        return np.array([ \
            9 * (1 - t) * t * t * t * 255, \
            15 * (1 - t) * (1 - t) * t * t * 255, \
            8.5 * (1 - t) * (1 - t) * (1 - t) * t * 255 \
            ], np.uint8)



    @staticmethod
    def mandelbrot(c, maxiter):
        z = 0
        for n in range(maxiter):
            if abs(z) > 2:
                return n
            z = z * z + c
        return maxiter



    def calculate_serial(self, maxiter=500):
        real = np.linspace(self._bbox[0].real, self._bbox[1].real,
            self._image.shape[0])
        imag = np.linspace(self._bbox[0].imag, self._bbox[1].imag,
            self._image.shape[1])
        for row, re in enumerate(real):
            for col, im in enumerate(imag):
                n = MandelbrotPatch.mandelbrot(complex(re, im), maxiter)
                self._image[row, col, :] = MandelbrotPatch.smooth_color_scalar(n, maxiter)



    @staticmethod
    def smooth_color_matrix(n, maxiter):
        t = (1.0 * n) / maxiter
        result = np.zeros((n.shape[0], n.shape[1], 3), dtype=np.uint8)
        result[:, :, 0] = 9 * (1 - t) * t * t * t * 255
        result[:, :, 1] = 15 * (1 - t) * (1 - t) * t * t * 255
        result[:, :, 2] = 8.5 * (1 - t) * (1 - t) * (1 - t) * t * 255
        return result



    def calculate_serial_fast(self, maxiter=500):
        real = np.linspace(self._bbox[0].real, self._bbox[1].real,
            self._image.shape[0])
        imag = np.linspace(self._bbox[0].imag, self._bbox[1].imag,
            self._image.shape[1])
        real, imag = np.meshgrid(real, imag, indexing='ij')
        c = real + imag * 1j

        z = np.zeros((self._image.shape[0], self._image.shape[1]), dtype=complex)
        n = maxiter * np.ones((self._image.shape[0], self._image.shape[1]), dtype=int)
        for i in range(maxiter):
            z = z * z + c
            diverged_pixels = abs(z) > 2
            newly_diverged_pixels = np.logical_and(diverged_pixels, n == maxiter)
            n[newly_diverged_pixels] = i
            z[diverged_pixels] = 2
        self._image = MandelbrotPatch.smooth_color_matrix(n, maxiter)



    @staticmethod
    def run(tile):
        tile.calculate_serial_fast()
        return tile

    def calculate_parallel(self, num_rows=10, num_cols=10, num_processes=8):
        tiles = self.tile(num_rows, num_cols)
        with multiprocessing.Pool(processes=num_processes) as pool:
            tiles = pool.map(MandelbrotPatch.run, tiles)
        self.detile(num_rows, num_cols, tiles)



    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.imshow(self.get_image())
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        plt.show()

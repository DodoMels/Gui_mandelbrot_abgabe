from skimage.io import imsave

from Mandelbrot.mandelbrot import MandelbrotPatch


def main():
    mbp = MandelbrotPatch((-2.2 - 1.7j, 1.2 + 1.7j), 1200, 1200)
    eye_of_the_world = 0.36024044343761436323612524444954530848260 - 0.641313061064803174860375015179302j
    n = 2
    for i in range(n):
        print(f'Calculating image {i + 1}/{n}...')
        mbp.calculate_parallel()
        imsave(f'eye{i:04}.png', mbp.get_image())
        # mbp.zoom_complex(eye_of_the_world, 1.1)
        # ToDo: Zoom und center eingeben
        mbp.zoom_complex(eye_of_the_world, 2.0)


if __name__ == '__main__':
    main()

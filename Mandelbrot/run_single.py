import time

from Mandelbrot.mandelbrot import MandelbrotPatch

if __name__ == '__main__':
    mbp = MandelbrotPatch((-2.2-1.7j, 1.2+1.7j), 800, 800)
    tic = time.time()
    mbp.calculate_serial_fast()
    tac = time.time()
    mbp.calculate_parallel()
    toc = time.time()
    factor = (tac - tic) / (toc - tac)
    print(f'serial {tac-tic:.1f}s, parallel {toc-tac:.1f}s, factor {factor:.1f}')
    mbp.plot()

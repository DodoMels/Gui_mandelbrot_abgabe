import matplotlib.pyplot as plt
import numpy as np

clicked_coordinates = ()

def on_press(event):
    global clicked_coordinates
    if event.button != 1:
        return
    clicked_coordinates = (event.xdata, event.ydata)

def on_release(event):
    global clicked_coordinates
    if event.button != 1:
        return
    print(clicked_coordinates)

if __name__ == '__main__':
    image = np.random.randint(0, 255, (600, 800, 3), dtype=np.uint8)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    fig.canvas.mpl_connect('button_press_event', on_press)
    fig.canvas.mpl_connect('button_release_event', on_release)
    ax.imshow(image)
    plt.show()

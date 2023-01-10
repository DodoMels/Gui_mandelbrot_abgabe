import cv2
import numpy as np

clicked_coordinates = ()

def click_and_crop(event, x, y, flags, param):
    global clicked_coordinates
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_coordinates = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        print(clicked_coordinates)

if __name__ == '__main__':
    image = np.random.randint(0, 255, (600, 800, 3), dtype=np.uint8)
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
    cv2.imshow("image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

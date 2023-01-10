import glob
import cv2

filenames = sorted(glob.glob('*.png'))

img = cv2.imread(filenames[0])
frame_height, frame_width, channels = img.shape
fps = 10

out = cv2.VideoWriter('video.avi',
    cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width, frame_height))

for filename in filenames:
    img = cv2.imread(filename)
    out.write(img)

out.release()


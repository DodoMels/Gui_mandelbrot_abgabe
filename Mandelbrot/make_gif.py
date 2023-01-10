import glob
import imageio

filenames = sorted(glob.glob('*.png'))

with imageio.get_writer('video.gif', mode='I', fps=20) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)


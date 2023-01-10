import numpy as np



def tile_indices(num_pixels, num_tiles):
    indices = np.zeros(num_tiles + 1, dtype=int)
    tile_size = np.ceil(num_pixels / num_tiles).astype('int')
    indices[:-1] = tile_size * np.arange(num_tiles)
    indices[-1] = num_pixels
    return indices



def tile_image(image, row_indices, col_indices):
    tiles = []
    for r in range(row_indices.size - 1):
        for c in range(col_indices.size - 1):
            tile = image[ \
                row_indices[r]:row_indices[r+1],
                col_indices[c]:col_indices[c+1],
                :]
            tiles.append(tile)
    return tiles



def detile_image(tiles, row_indices, col_indices):
    image = np.zeros((row_indices[-1], col_indices[-1], 3), dtype=np.uint8)
    i = 0
    for r in range(row_indices.size - 1):
        for c in range(col_indices.size - 1):
            image[ \
                row_indices[r]:row_indices[r+1],
                col_indices[c]:col_indices[c+1],
                :] = tiles[i]
            i += 1
    return image



def tile_bounding_box(bbox, row_indices, col_indices):
    # Not the most efficient implementation to generate intermediate
    # values for each pixel, but it works
    real = np.linspace(bbox[0].real, bbox[1].real, row_indices[-1])
    imag = np.linspace(bbox[0].imag, bbox[1].imag, col_indices[-1])
    tiles = []
    for r in range(row_indices.size - 1):
        for c in range(col_indices.size - 1):
            tile = [
                complex(real[row_indices[r]], imag[col_indices[c]]),
                complex(real[row_indices[r+1]-1], imag[col_indices[c+1]-1]),
            ]
            tiles.append(tile)
    return tiles

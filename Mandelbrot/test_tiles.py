import numpy as np
import pytest

from tiles import tile_indices, tile_image, detile_image, tile_bounding_box



def test_tile_indices():
    assert np.all(tile_indices(12, 3) == np.array((0, 4, 8, 12)))
    assert np.all(tile_indices(13, 3) == np.array((0, 5, 10, 13)))



def test_image_tile_detile_roundtrip():
    width = 320
    height = 200
    col_tiles = 23
    row_tiles = 20
    image = np.random.randint(0, 255, (width, height, 3), np.uint8)
    row_indices = tile_indices(width, col_tiles)
    col_indices = tile_indices(height, row_tiles)
    tiles = tile_image(image, row_indices, col_indices)
    assert len(tiles) == (col_tiles * row_tiles)
    image2 = detile_image(tiles, row_indices, col_indices)
    assert image.ndim == image2.ndim
    assert np.all(image.shape == image2.shape)
    assert np.all(image == image2)



def test_bounding_box_tile_detile():
    width = 51
    height = 101
    col_tiles = 2
    row_tiles = 3
    bbox = ( 0+0j, 1+1j )
    row_indices = tile_indices(height, row_tiles)
    col_indices = tile_indices(width, col_tiles)
    tiles = tile_bounding_box(bbox, row_indices, col_indices)
    assert len(tiles) == (row_tiles * col_tiles)
    expected_tiles = (
        (complex(0.00, 0.00), complex(0.33, 0.5)),
        (complex(0.00, 0.52), complex(0.33, 1.0)),
        (complex(0.34, 0.00), complex(0.67, 0.5)),
        (complex(0.34, 0.52), complex(0.67, 1.0)),
        (complex(0.68, 0.00), complex(1.00, 0.5)),
        (complex(0.68, 0.52), complex(1.00, 1.0)),
    )
    for t1, t2 in zip(tiles, expected_tiles):
        assert np.all(np.isclose(t1, t2))

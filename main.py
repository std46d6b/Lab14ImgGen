from PIL import Image
import numpy as np


def matrix_to_bmp(matrix, file_name):
    color_matrix = np.array([[[255 * val, 255 * val, 255 * val] for val in row] for row in matrix], dtype=np.uint8)
    image = Image.fromarray(color_matrix, 'RGB')
    image.save(file_name + ".bmp")


str_matrix = """
1010101010
0101010100
0010101000
0001010000
0000100000
"""

fsm = [[int(b1) for b1 in list(b)] for b in str_matrix.split('\n') if b]

print(len(fsm[0]), 'x', len(fsm))

matrix_to_bmp(fsm, "image_example")  # Сохранение в файл "output_image.bmp"

import numpy as np
from PyQt5.QtGui import QPixmap, QImage
from src.main.homework1.backend.cpu_computing import compute_on_cpu
from src.main.homework1.backend.gpu_computing import compute_on_gpu


def compute(pixmaps, filters_matrices_list, on_cpu):
    def pixmap_to_image_with_format(pixmap):
        width = pixmap.width()
        height = pixmap.height()

        image = pixmap.toImage()
        channels = 4
        bit_string = image.bits().asstring(width * height * channels)

        return np.frombuffer(bit_string, dtype=np.uint8).reshape((height, width, channels)), image.format()

    def matrix_to_pixmap(matrix, image_format):
        height, width, _ = matrix.shape

        return QPixmap(QImage(matrix.data, width, height, 4 * width, image_format))

    images_with_formats = list(map(pixmap_to_image_with_format, pixmaps))
    pixmaps_matrices_list = list(map(lambda p: p[0], images_with_formats))

    if on_cpu:
        matrices_after_filters = compute_on_cpu(pixmaps_matrices_list, filters_matrices_list)
    else:
        matrices_after_filters = compute_on_gpu(pixmaps_matrices_list, filters_matrices_list)

    return list(map(lambda i: (pixmaps[i], matrix_to_pixmap(matrices_after_filters[i], images_with_formats[i][1])),
                    range(len(pixmaps))))

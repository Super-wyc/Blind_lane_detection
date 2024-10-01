import cv2
import numpy as np


def imshow(image : np.ndarray, window_name : str = 'img') -> np.ndarray :
    cv2.namedWindow(f'{window_name}', cv2.WINDOW_NORMAL)
    cv2.resizeWindow(f'{window_name}', 1000, 600)
    cv2.imshow(f"{window_name}", image)
    cv2.waitKey(0)
    return image


#Todo 图上矩形框标注函数
def rectangle_plot(
        img : np.ndarray,
        color : str | tuple,
        pst1 : tuple,
        pst2 : tuple
        ) -> int:
    cv2.rectangle(img, pst1, pst2, color)
    return 0
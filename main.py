import numpy as np
from typing import Tuple, List, Set, Dict
from cv2 import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import os


def main() -> None:
    for image_name in os.listdir("./pictures"):
        image = cv2.imread("./pictures/" + image_name)
        print(f"Show { image_name } Size: { image.shape }")
        cv2.imshow("res", image)
        cv2.waitKey(500)
    

if __name__ == "__main__":
    main()
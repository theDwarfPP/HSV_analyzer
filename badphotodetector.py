import os
import numpy as np
import multiprocessing as mp
from PIL import Image


import cv2
import numpy as np


def findbadphoto(photopath):
    try:
        img = cv2.imdecode(np.fromfile(photopath, dtype=np.uint8),-1)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        a = hsv
    except cv2.error:
        print("cv2:", photopath)
    except FileNotFoundError:
        print("filenotfind",photopath)


if __name__ == '__main__':
    rootpath = 'D:\\shanghai_resized'
    photopath_list = []
    for file in os.listdir(rootpath):
        for i in os.listdir(rootpath + '\\' + file):
            for photo in os.listdir(rootpath + '\\' + file + '\\' + i):
                file_path = rootpath + '\\' + file + '\\' + i + '\\' + photo
                photopath_list.append(file_path)


    pool = mp.Pool()
    res = pool.map(findbadphoto, photopath_list)
    pool.close()
    pool.join()


# -*- coding=utf-8 -*-
# @Time : 2022/3/30 21:20
# @Author : The_dwarf
# @File : colorHSV.py
# @Software: PyCharm
import cv2
import numpy as np
import openpyxl
import os
import multiprocessing as mp



def hsvExtractor(photopath):
    print("正在处理:" + photopath.split("\\")[-2])
    photo_name = photopath.split('\\')[-2]
    img = cv2.imdecode(np.fromfile(photopath, dtype=np.uint8), -1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(hsv)

    v = V.ravel()[np.flatnonzero(V)]
    s = S.ravel()[np.flatnonzero(S)]
    h = H.ravel()[np.flatnonzero(H)]

    try:
        average_v = sum(v) / len(v)
        average_s = sum(s) / len(s)
        average_h = sum(h) / len(h)
    except ZeroDivisionError:
        average_v = 0
        average_s = 0
        average_h = 0

    data = []
    data.append(photo_name)
    data.append(average_v)
    data.append(average_s)
    data.append(average_h)


    return data

if __name__ == '__main__':
    wb = openpyxl.load_workbook('photo_hsvnew.xlsx')
    ws1 = wb['Sheet1']

    rootpath = 'D:\\shanghai_resized'
    photopath_list = []
    for file in os.listdir(rootpath):
        for i in os.listdir(rootpath + '\\' + file):
            for photo in os.listdir(rootpath + '\\' + file + '\\' + i):
                file_path = rootpath + '\\' + file + '\\' + i + '\\' + photo
                photopath_list.append(file_path)

    datalist = []
    pool = mp.Pool()
    res = pool.map(hsvExtractor, photopath_list)
    datalist.append(res)
    pool.close()
    pool.join()

    for a in datalist:
        for data in a:
            ws1.append(data)
        print('正在写入一个数据')
    wb.save('photo_hsvnew.xlsx')


    # filelist = os.listdir(rootpath)
    # count = 0
    # for file in filelist:
    #     count += 1
    #     print('正在处理第{}个民宿'.format(count))
    #     filepath = rootpath + '\\{}'.format(file)
    #     photolist = os.listdir(filepath)
    #     photopath_list = []
    #     datalist = []
    #     for photo in photolist:
    #         photopath = filepath + '\\{}'.format(photo)
    #         photopath_list.append(photopath)
    #
    #     pool = mp.Pool()
    #     res = pool.map(hsvExtractor, photopath_list)
    #     datalist.append(res)
    #     pool.close()
    #     pool.join()
    #
    #
    #     for a in datalist:
    #         for data in a:
    #             ws1.append(data)
    #         print('正在写入一个数据')
    #     wb.save('photo_hsv.xlsx')




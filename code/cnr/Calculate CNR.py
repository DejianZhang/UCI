# -*- coding: utf-8 -*-
"""
Created on 

@author: 
"""
import snr
import cv2
#二值化，阈值设置，让之前不完美的mask二值化
img=cv2.imread(r"/home/exp/Downloads/uci_code_data1205/code/cnr/mask.png") #use obsolute path
t,img_bin = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
img_bin =cv2.cvtColor(img_bin, cv2.COLOR_BGR2GRAY)
'''
其中t为阈值,img_bin为输出图; img为输入图像，thresh为阈值，maxval为最大值，
type为模式,如下所示：
cv2.THRESH_BINARY	#大于阈值的部分取最大值，小于等于阈值的部分取0
cv2.THRESH_BINARY_INV	#大于阈值的部分取0，小于等于阈值的部分取最大值
cv2.THRESH_TOZERO	#大于阈值的部分不变，小于等于阈值的部分取0
cv2.THRESH_TOZERO_INV	#大于阈值的部分取0，小于等于阈值的部分不变
cv2.THRESH_TRUNC	#大于阈值的部分取阈值，小于等于阈值的部分不变
'''
#模板图片加载，你的原图mask
mask=img_bin/255
#mask = cv2.imread(r"C:\Users\DELL\Desktop\cnr image\untitled4-mask-alpha.png")[:,:,0]/255
import numpy as np
mask = np.array(mask)
mask = 1-mask
print(mask[100,100])
# print((mask.dtype))
# 读取彩色图像
#image=img_bin
#image = cv2.imread(r"C:\Users\DELL\Desktop\cnr image\ppln(ncu900).png")
from pathlib import Path
base_path = Path("../../data")
#nir cnr随噪声水平变化
image_paths = [
base_path / "NIR NCU with different noise levels of 0.13.png",
base_path / "NIR NCU with different noise levels of 0.38.png",
base_path / "NIR NCU with different noise levels of 0.53.png",
base_path / "NIR NCU with different noise levels of 0.68.png",
base_path / "NIR NCU with different noise levels of 0.76.png",
base_path / "NIR NCU with different noise levels of 0.84.png",
base_path / "NIR NCU with different noise levels of 0.89.png",
]
#上转换cnr随噪声水平变化
# image_paths = [
#     base_path / "USPD NCU with different noise levels of 0.13.png",
#     base_path / "USPD NCU with different noise levels of 0.38.png",
#     base_path / "USPD NCU with different noise levels of 0.53.png",
#     base_path / "USPD NCU with different noise levels of 0.68.png",
#     base_path / "USPD NCU with different noise levels of 0.76.png",
#     base_path / "USPD NCU with different noise levels of 0.84.png",
#     base_path / "USPD NCU with different noise levels of 0.89.png",
#  ]
#nir cnr随积分时间变化
# image_paths = [
#  base_path / "NIR NCU 0.1s integration time fixed noise.png",
#  base_path / "NIR NCU 1s integration time fixed noise.png",
#  base_path / "NIR NCU 2s integration time fixed noise.png",
#  base_path / "NIR NCU 3s integration time fixed noise.png",
#  base_path / "NIR NCU 4s integration time fixed noise.png"
# ]
#上转换cnr随积分时间变化
# image_paths = [
#     base_path / "USPD NCU 0.1s integration time fixed noise.png",
#     base_path / "USPD NCU 1s integration time fixed noise.png",
#     base_path / "USPD NCU 2s integration time fixed noise.png",
#     base_path / "USPD NCU 3s integration time fixed noise.png",
#     base_path / "USPD NCU 4s integration time fixed noise.png"
# ]
for image_path in image_paths:
    # 读取彩色图像
    image_path_str = str(image_path)  # 将 Path 对象转换为字符串
    image = cv2.imread(image_path_str)
    if image is not None:
        print(f"Successfully loaded: {image_path_str}")
        # 将彩色图像转换为灰度图像
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        try:
            SNR, CNR, SBR = snr.cnr(image_gray, mask)  # 请确保 snr.cnr 函数已正确导入和定义
            print(f"CNR for {image_path}:CNR = {CNR}\n")
        except Exception as e:
            print(f"Failed to calculate CNR for {image_path}: {e}")
    else:
        print(f"Failed to load: {image_path_str}")

# -*- coding: utf-8 -*-
"""
Created on 

@author: 
"""
import numpy as np
import scipy as sp
#import scipy.io  # 注意：如果要调用scipy的子模块，一定要这样写！
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from PIL import Image
import scipy.io

# row_num = 768
# column_num = 1024
row_num = 539
column_num = 682


#np.loadtxt()

# 1.把几个mat数据都调入。
def cnr(data, ref):
    
    data =data
    matBnu=ref
    #np.load('/home/exp/data/0622/cor.npy').astype(np.float64)# 用数据换掉
    # CNR = np.zeros(shape=(19))
    # SNR = np.zeros(shape=(19))
    for k in range(1):
        mat500 = data#[:,:,k]
        (row_num,column_num)=mat500.shape
        #plt.figure(i)
        #plt.imshow(mat500);
        #plt.show()
        #ref = scipy.io.loadmat('/home/exp/ds.mat')
        #matBnu = ref.get('img')
    #mat500 = (255 - mat500) / 255.0
        #matBnu = (255 - matBnu) / 255.0
    # 计算物体bnu处的信噪比
    
    
    # 统计点数
        count = 0
        for i in range(row_num):
            for j in range(column_num):
                if (matBnu[i,j] > 0.5):
                    count = count + 1
        # mat500 = mat500[:, :, np.newaxis]
        #信号的灰度图
        bnu = mat500* matBnu
        #信号的平均灰度图
        Signal= bnu.sum() / count
        #信号的灰度图-信号的平均灰度图
        #k=bnu-matBnu*Signal
        #信号灰度图的标准差
        Noise = np.sqrt(np.abs((bnu ** 2).sum() / count - Signal* Signal))
        #背景灰度图
        nonBnu = mat500*(1-matBnu)
        #背景平均灰度图
        SignalNonBnu = nonBnu.sum()/(row_num*column_num-count)
        NoiseNonBnu = np.sqrt(np.abs((nonBnu**2).sum()/(row_num*column_num-count)-SignalNonBnu**2))
        #背景灰度图-平均灰度图
        #z=nonBnu-matBnu*SignalNonBnu
        #背景灰度图的方差
        #y=(z**2).sum()/(row_num*column_num-count)
    
        SNR = Signal/ Noise
        CNR = (Signal-SignalNonBnu)/np.sqrt(Noise**2+NoiseNonBnu**2)
        SBR = Signal/SignalNonBnu
        #CNR = abs(Signal-SignalNonBnu)/np.sqrt(x+y)
        #print(SNR)
        return (SNR,CNR,SBR)
    #return(CNR)
        

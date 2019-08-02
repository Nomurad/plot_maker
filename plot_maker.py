import os
import sys

import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt 
from matplotlib import colorbar, colors
from matplotlib import rcParams, rc
from matplotlib.ticker import FormatStrFormatter, ScalarFormatter
from matplotlib.colors import LinearSegmentedColormap

def init_pltenv(fontsize=24):
    """ 
    フォント，文字サイズの設定用関数
    """
    rcParams['font.size'] = fontsize # default=>10.0
    rcParams['axes.formatter.use_mathtext'] = True
    font = {"family":"Times New Roman"}
    rc('font', **font)
    rc('mathtext', **{
        'rm': 'Times New Roman',
        'it': 'Times New Roman',
        'bf': 'Times New Roman',
        'fontset': 'stix'
        })

def generate_cmap(colors, n):
    """
    コンター図作成時使用
    自分で定義したカラーマップを返す
    """
    # values = range(len(colors))
    values = range(colors.N)
    cmap = colors
    colors = [cmap(i) for i in (values)]

    vmax = np.ceil(np.max(values))
    color_list = []
    for v, c in zip(values, colors):
        color_list.append( ( v/ vmax, c) )
    return LinearSegmentedColormap.from_list('custom_cmap', color_list, N=n)

def plot_maker_2d(data):
    if not isinstance(data, np.ndarray):
        print("usable data set ndarray only.")
        return
    
    dim = len(data)
    pltdata = data
    # plt.plot(pltdata)   # 折れ線グラフ
    plt.scatter(pltdata[0], pltdata[1]) # 散布図
    plt.show()
    return

def plot_maker(data, dimention=2):
    if dimention == 2:
        plot_maker_2d(data)
    
    return

if __name__ == "__main__":
    df = pd.read_csv("iris.csv",)
    data = df.values.T
    # print(data)
    init_pltenv()
    plot_maker(data)
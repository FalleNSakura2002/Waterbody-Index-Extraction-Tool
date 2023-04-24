from osgeo import gdal
import numpy as np
import os
from PIL import Image
from src.BandLoader import Create_Loader
from src.Imgdisplay import display

# 建立缓存文件夹
if not os.path.exists('tmp'):
    os.mkdir('tmp')

# 对影像做0-255拉伸
def draw(array, max, min):
    array = (np.array(array) - min) / (max - min) * 255
    return array

# 求全局最小值和全局最大值
def global_max_min(r_array, g_array, b_array):
    # 求最大值
    r_max = float(np.max(r_array))
    g_max = float(np.max(g_array))
    b_max = float(np.max(b_array))
    max_value = [r_max, g_max, b_max]
    max = float(np.max(max_value))

    # 求最小值
    r_min = float(np.min(r_array))
    g_min = float(np.min(g_array))
    b_min = float(np.min(b_array))
    min_value = [r_min, g_min, b_min]
    min = float(np.max(min_value))

    return max, min

# 对单波段影像进行拉伸
def single_max_min(array):
    min = float(np.min(array))
    max = float(np.max(array))
    array = (np.array(array) - min) / (max - min) * 255
    return array

# 读取影像数据
class IMAGE:
    # 读图像文件
    def read_img(self, filename):
        print(filename)
        dataset = gdal.Open(filename)  # 打开文件
        im_bands = dataset.RasterCount  # 波段数
        im_width = dataset.RasterXSize  # 栅格矩阵的列数
        im_height = dataset.RasterYSize  # 栅格矩阵的行数
        del dataset

        return im_bands, im_height, im_width

# 多波段影像的打开方式
def multy_band(filename, bands):
    # 读取遥感影像文件
    dataset = gdal.Open(filename)

    band_list = []
    for i in range(bands):
        band_list.append('Band ' + str(i + 1))
    RGBlist = [0,0,0]
    Create_Loader(RGBlist, band_list)
    R = int(RGBlist[0].split(' ')[-1])
    G = int(RGBlist[1].split(' ')[-1])
    B = int(RGBlist[2].split(' ')[-1])

    # 获取红绿蓝波段
    red_band = dataset.GetRasterBand(R)
    green_band = dataset.GetRasterBand(G)
    blue_band = dataset.GetRasterBand(B)

    # 读取波段数据
    red_data = red_band.ReadAsArray()
    green_data = green_band.ReadAsArray()
    blue_data = blue_band.ReadAsArray()

    # 转换数据格式
    red_data = (red_data).astype('float')
    green_data = (green_data).astype('float')
    blue_data = (blue_data).astype('float')

    band_max, band_min = global_max_min(red_data, green_data, blue_data)


    # 拉伸数据
    red_data = draw(red_data, band_max, band_min)
    green_data = draw(green_data, band_max, band_min)
    blue_data = draw(blue_data, band_max, band_min)

    # 创建RGB数组
    rgb = [red_data, green_data, blue_data]

    # 转换为图像
    rgb_array = np.dstack(rgb).astype(np.uint8)

    image = Image.fromarray(rgb_array.astype(np.uint8))
    display(filename, image, 0)

# 单波段影像的打开方式
def single_band(filename):
    # 读取遥感影像文件
    dataset = gdal.Open(filename)

    # 读取影像数据
    band = dataset.GetRasterBand(1)
    array = band.ReadAsArray()

    array = (array).astype('float')

    array[array == 255.0] = np.nan
    array[array == -255.0] = np.nan

    # 执行最小-最大拉伸
    min_val = np.nanmin(array)
    max_val = np.nanmax(array)
    array = (array - min_val) / (max_val - min_val) * 255

    # 将数组转换为PIL图像对象
    image = Image.fromarray(array.astype(np.uint8))
    display(filename, image, 1)

# 加载影像
def LoadImg(filename):
    # 读取影像信息
    image_grid = IMAGE()
    # 读取波段和宽高信息
    im_band, height, width = image_grid.read_img(filename)
    # 约束宽高
    if height > 800:
        height = 800
    if width > 800:
        width = 600
    # 按波段数返回结果
    if im_band == 1:
        single_band(filename)
        return height, width
    else:
        multy_band(filename, im_band)
        return height, width

# 读取波段数
def GetBands(filename):
    # 读取影像信息
    image_grid = IMAGE()
    # 读取波段和宽高信息
    im_band, height, width = image_grid.read_img(filename)

    return im_band
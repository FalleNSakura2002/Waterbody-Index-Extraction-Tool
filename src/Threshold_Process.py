from osgeo import gdal
import numpy as np
from skimage.filters import threshold_otsu
from src.LoadImg import LoadImg

# 大津法
def OTSU(filename, output):
    # 打开tif图像
    ds = gdal.Open(filename)

    # 读取波段数据
    band = ds.GetRasterBand(1)
    data = band.ReadAsArray()

    # # 清理数据
    # data[data == 255.0] = np.nan
    # data[data == -255.0] = np.nan

    # # 计算大津法阈值
    # try:
    best_threshold = threshold_otsu(data)
    # except:
    #     if float(np.nanmin(data)) < 0 and float(np.nanmax(data)) < 0:
    #         data = np.abs(data)
    #
    #     # 计算图像的直方图
    #
    #     hist, bins = np.histogram(data.flatten(), 256, [0, 256])
    #
    #     # 计算图像的总像素数
    #     total_pixels = data.shape[0] * data.shape[1]
    #
    #     # 初始化最佳阈值和最大类间方差
    #     best_threshold = 0
    #     max_variance = 0
    #
    #     # 遍历所有可能的阈值
    #     for t in range(256):
    #         # 计算当前阈值下的背景和前景像素数量
    #         bg_pixels = np.sum(hist[:t])
    #         fg_pixels = total_pixels - bg_pixels
    #
    #         # 如果背景或前景像素数量为0，则跳过当前阈值
    #         if bg_pixels == 0 or fg_pixels == 0:
    #             continue
    #
    #         # 计算当前阈值下的背景和前景像素均值
    #         bg_mean = np.sum(np.arange(t) * hist[:t]) / bg_pixels
    #         fg_mean = np.sum(np.arange(t, 256) * hist[t:]) / fg_pixels
    #
    #         # 计算当前阈值下的类间方差
    #         variance = bg_pixels * fg_pixels * (bg_mean - fg_mean) ** 2
    #
    #         # 如果当前阈值下的类间方差大于最大类间方差，则更新最佳阈值和最大类间方差
    #         if variance > max_variance:
    #             best_threshold = t
    #             max_variance = variance

    # 应用阈值
    binary = np.zeros_like(data)
    print(best_threshold)
    binary[data >= best_threshold] = 1

    # 创建新的tif图像
    driver = gdal.GetDriverByName('GTiff')
    out_ds = driver.Create(output, ds.RasterXSize, ds.RasterYSize, 1, gdal.GDT_Byte)

    # 设置地理参考信息和投影信息
    out_ds.SetGeoTransform(ds.GetGeoTransform())
    out_ds.SetProjection(ds.GetProjection())

    # 写入数据
    out_band = out_ds.GetRasterBand(1)
    out_band.WriteArray(binary)

    # 关闭图像
    ds = None
    out_ds = None

    # 加载影像
    LoadImg(output)

# 凯勒法
def min_err_threshold(image):
    # 计算输入影像的直方图
    hist = np.histogram(image, bins=range(256))[0].astype(np.float)

    # 计算每个阈值的背景像素数
    w_backg = hist.cumsum()
    w_backg[w_backg == 0] = 1  # 避免分母为0

    # 计算每个阈值的前景像素数
    w_foreg = w_backg[-1] - w_backg
    w_foreg[w_foreg == 0] = 1  # 避免分母为0

    # 计算累计分布函数
    cdf = np.cumsum(hist * np.arange(len(hist)))

    # 计算均值
    b_mean = cdf / w_backg
    f_mean = (cdf[-1] - cdf) / w_foreg

    # 计算标准偏差
    b_std = ((np.arange(len(hist)) - b_mean)**2 * hist).cumsum() / w_backg
    f_std = ((np.arange(len(hist)) - f_mean) ** 2 * hist).cumsum()
    f_std = (f_std[-1] - f_std) / w_foreg

    # 避免结果为0
    b_std[b_std == 0] = 1
    f_std[f_std == 0] = 1

    # 计算结果
    error_a = w_backg * np.log(b_std) + w_foreg * np.log(f_std)
    error_b = w_backg * np.log(w_backg) + w_foreg * np.log(w_foreg)
    error = 1 + 2 * error_a - 2 * error_b

    return np.argmin(error)
def Kittler(filename, output):
    # 读取影像数据
    index_file = filename
    index_dataset = gdal.Open(index_file)
    index_band = index_dataset.GetRasterBand(1)
    index_data = index_band.ReadAsArray()

    # 重置矩阵
    index_data[index_data == 255.0] = np.nan
    index_data[index_data == -255.0] = np.nan
    min = float(np.nanmin(index_data))
    max = float(np.nanmax(index_data))
    index_data = (np.array(index_data) - min) / (max - min) * 100
    opt_thresh = min_err_threshold(index_data)

    # 对index影像进行二值化处理
    index_binary = np.where(index_data > opt_thresh, 1, 0)
    print(index_binary)

    # 创建输出影像
    out_file = output
    driver = gdal.GetDriverByName('GTiff')
    out_ds = driver.Create(out_file, index_dataset.RasterXSize, index_dataset.RasterYSize, 1, gdal.GDT_Byte)
    # 设置投影和地理参考信息
    out_ds.SetProjection(index_dataset.GetProjection())
    out_ds.SetGeoTransform(index_dataset.GetGeoTransform())
    # 将二值化数据写入输出影像
    out_ds.GetRasterBand(1).WriteArray(index_binary)
    # 关闭数据集
    out_ds = None

    LoadImg(output)

# 手动阈值提取
def Manu(filename, output, threshold):
    # 打开index影像
    index_file = filename
    index_ds = gdal.Open(index_file)

    # 读取index数据
    index_data = index_ds.ReadAsArray()

    # 定义阈值
    threshold = float(threshold)
    # 对index数据进行二值化处理
    binary_index = np.where(index_data > threshold, 1, 0)

    # 创建输出影像
    out_file = output
    driver = gdal.GetDriverByName('GTiff')
    out_ds = driver.Create(out_file, index_ds.RasterXSize, index_ds.RasterYSize, 1, gdal.GDT_Byte)
    # 设置投影和地理参考信息
    out_ds.SetProjection(index_ds.GetProjection())
    out_ds.SetGeoTransform(index_ds.GetGeoTransform())
    # 将二值化数据写入输出影像
    out_ds.GetRasterBand(1).WriteArray(binary_index)
    # 关闭数据集
    out_ds = None

    LoadImg(output)

# 总方法
def Threshold_Calculate(filename, output, argu_mainfunc, argu_autofunc, argu_manufunc):
    if argu_mainfunc == '自动阈值提取':
        if argu_autofunc == 'OTSU-大津法':
            OTSU(filename, output)
        elif argu_autofunc == 'Kittler-凯勒法':
            Kittler(filename, output)
        else:
            OTSU(filename, output)
    if argu_mainfunc == '手动阈值提取':
        Manu(filename, output, argu_manufunc)



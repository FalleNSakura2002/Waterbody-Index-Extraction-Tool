from osgeo import gdal
from src.LoadImg import LoadImg
import numpy as np

# 计算NDWI指数
def get_NDWI(img_data, argument, cols, rows):
    # 分解参数
    gre = int(argument[0].split(' ')[-1])
    nir = int(argument[1].split(' ')[-1])
    # 读取数据
    gre_band = img_data.GetRasterBand(gre).ReadAsArray(0, 0, cols, rows)
    nir_band = img_data.GetRasterBand(nir).ReadAsArray(0, 0, cols, rows)
    # 代入计算
    model = (gre_band - nir_band) / (gre_band + nir_band)
    model = np.nan_to_num(model)
    return model

# 计算MNDWI指数
def get_MNDWI(img_data, argument, cols, rows):
    # 分解参数
    gre = int(argument[0].split(' ')[-1])
    swir = int(argument[1].split(' ')[-1])
    # 读取数据
    gre_band = img_data.GetRasterBand(gre).ReadAsArray(0, 0, cols, rows)
    swir_band = img_data.GetRasterBand(swir).ReadAsArray(0, 0, cols, rows)
    # 代入计算
    model = (gre_band - swir_band) / (gre_band + swir_band)
    model = np.nan_to_num(model)
    return model

# 计算NWI指数
def get_NWI(img_data, argument, cols, rows):
    # 分解参数
    blu = int(argument[0].split(' ')[-1])
    nir = int(argument[1].split(' ')[-1])
    swir1 = int(argument[2].split(' ')[-1])
    swir2 = int(argument[3].split(' ')[-1])
    # 读取数据
    blu_band = img_data.GetRasterBand(blu).ReadAsArray(0, 0, cols, rows)
    nir_band = img_data.GetRasterBand(nir).ReadAsArray(0, 0, cols, rows)
    swir1_band = img_data.GetRasterBand(swir1).ReadAsArray(0, 0, cols, rows)
    swir2_band = img_data.GetRasterBand(swir2).ReadAsArray(0, 0, cols, rows)
    # 代入计算
    model = (blu_band - nir_band + swir1_band + swir2_band) / (blu_band + nir_band + swir1_band + swir2_band) * 255
    model = np.nan_to_num(model)
    return model

# 计算FNDWI指数
def get_FNDWI(img_data, argument, cols, rows):
    # 分解参数
    gre = int(argument[0].split(' ')[-1])
    nir = int(argument[1].split(' ')[-1])
    # 读取数据
    gre_band = img_data.GetRasterBand(gre).ReadAsArray(0, 0, cols, rows)
    nir_band = img_data.GetRasterBand(nir).ReadAsArray(0, 0, cols, rows)
    # 代入计算
    model = (gre_band + 1 * (40 - nir_band) - nir_band) / (gre_band + 1 * (40 + nir_band) + nir_band)
    model = np.nan_to_num(model)
    return model

# 计算CIWI指数
def get_CIWI(img_data, argument, cols, rows):
    # 分解参数
    red = int(argument[0].split(' ')[-1])
    nir = int(argument[1].split(' ')[-1])
    swir = int(argument[2].split(' ')[-1])
    # 读取数据
    red_band = img_data.GetRasterBand(red).ReadAsArray(0, 0, cols, rows)
    nir_band = img_data.GetRasterBand(nir).ReadAsArray(0, 0, cols, rows)
    swir_band = img_data.GetRasterBand(swir).ReadAsArray(0, 0, cols, rows)
    # 计算均值
    swir_mean = sum(swir_band) / len(swir_band)
    # 代入计算
    model = (nir_band - red_band) / (nir_band + red_band) + (swir_band) / (swir_mean) + 100
    model = np.nan_to_num(model)
    return model

# 计算NWI指数
def get_NWI(img_data, argument, cols, rows):
    # 分解参数
    blu = int(argument[0].split(' ')[-1])
    nir = int(argument[1].split(' ')[-1])
    swir1 = int(argument[2].split(' ')[-1])
    swir2 = int(argument[3].split(' ')[-1])
    # 读取数据
    blu_band = img_data.GetRasterBand(blu).ReadAsArray(0, 0, cols, rows)
    nir_band = img_data.GetRasterBand(nir).ReadAsArray(0, 0, cols, rows)
    swir1_band = img_data.GetRasterBand(swir1).ReadAsArray(0, 0, cols, rows)
    swir2_band = img_data.GetRasterBand(swir2).ReadAsArray(0, 0, cols, rows)
    print(swir2_band)
    # 代入计算
    model = (blu_band - (nir_band + swir1_band + swir2_band)) / (blu_band + (nir_band + swir1_band + swir2_band)) * 255
    model = np.nan_to_num(model)
    return model

# 计算TNWI指数
def get_TNWI(img_data, argument, cols, rows):
    # 分解参数
    nir = int(argument[0].split(' ')[-1])
    swir1 = int(argument[1].split(' ')[-1])
    swir2 = int(argument[2].split(' ')[-1])
    tmp = int(argument[3].split(' ')[-1])
    # 读取数据
    nir_band = img_data.GetRasterBand(nir).ReadAsArray(0, 0, cols, rows)
    swir1_band = img_data.GetRasterBand(swir1).ReadAsArray(0, 0, cols, rows)
    swir2_band = img_data.GetRasterBand(swir2).ReadAsArray(0, 0, cols, rows)
    tmp_band = img_data.GetRasterBand(tmp).ReadAsArray(0, 0, cols, rows)
    # 代入计算
    model = (tmp_band - (nir_band + swir1_band + swir2_band)) / (tmp_band + (nir_band + swir1_band + swir2_band)) * 255
    model = np.nan_to_num(model)
    return model

# 计算TMBCWI指数
def get_TMBCWI(img_data, argument, cols, rows):
    # 分解参数
    CA = int(argument[0].split(' ')[-1])
    gre = int(argument[1].split(' ')[-1])
    nir = int(argument[2].split(' ')[-1])
    swir1 = int(argument[3].split(' ')[-1])
    swir2 = int(argument[4].split(' ')[-1])
    tmp = int(argument[5].split(' ')[-1])
    # 读取数据
    CA_band = img_data.GetRasterBand(CA).ReadAsArray(0, 0, cols, rows)
    gre_band = img_data.GetRasterBand(gre).ReadAsArray(0, 0, cols, rows)
    nir_band = img_data.GetRasterBand(nir).ReadAsArray(0, 0, cols, rows)
    swir1_band = img_data.GetRasterBand(swir1).ReadAsArray(0, 0, cols, rows)
    swir2_band = img_data.GetRasterBand(swir2).ReadAsArray(0, 0, cols, rows)
    tmp_band = img_data.GetRasterBand(tmp).ReadAsArray(0, 0, cols, rows)
    # 代入计算
    model = 2 * (gre_band + tmp_band + swir2_band) - 2 * (nir_band + swir1_band + CA_band)
    model = np.nan_to_num(model)
    return model

# 计算改进的PTMBCW指数
def get_PTMBCW(img_data, argument, cols, rows):
    # 分解参数
    CA = int(argument[0].split(' ')[-1])
    gre = int(argument[1].split(' ')[-1])
    nir = int(argument[2].split(' ')[-1])
    swir1 = int(argument[3].split(' ')[-1])
    pan = int(argument[4].split(' ')[-1])
    tmp = int(argument[5].split(' ')[-1])
    # 读取数据
    CA_band = img_data.GetRasterBand(CA).ReadAsArray(0, 0, cols, rows)
    gre_band = img_data.GetRasterBand(gre).ReadAsArray(0, 0, cols, rows)
    nir_band = img_data.GetRasterBand(nir).ReadAsArray(0, 0, cols, rows)
    swir1_band = img_data.GetRasterBand(swir1).ReadAsArray(0, 0, cols, rows)
    pan_band = img_data.GetRasterBand(pan).ReadAsArray(0, 0, cols, rows)
    tmp_band = img_data.GetRasterBand(tmp).ReadAsArray(0, 0, cols, rows)
    # 代入计算
    model = 5 * (gre_band + pan_band + tmp_band)-(7 * nir_band + 6*CA_band + swir1_band)
    model = np.nan_to_num(model)
    return model

def Calculate(filename, function, argument, output_path):
    print(filename)
    # 读取影像
    img_data = gdal.Open(filename)

    # 读取影像栅格行列数
    cols = img_data.RasterXSize  # 列数
    rows = img_data.RasterYSize  # 行数
    # 计算结果
    if function == 'NDWI':
        argument =argument[0]
        result = get_NDWI(img_data, argument, cols, rows)
    elif function == 'MNDWI':
        argument = argument[1]
        result = get_MNDWI(img_data, argument, cols, rows)
    elif function == 'NWI':
        argument = argument[2]
        result = get_NWI(img_data, argument, cols, rows)
    elif function == 'FNDWI':
        argument = argument[3]
        result = get_FNDWI(img_data, argument, cols, rows)
    else:
        argument = argument[4]
        result = get_CIWI(img_data, argument, cols, rows)

    # 生成影像
    target_ds = gdal.GetDriverByName('GTiff').Create(output_path, xsize=cols, ysize=rows, bands=1,
                                                     eType=gdal.GDT_Float32)
    target_ds.SetGeoTransform(img_data.GetGeoTransform())
    target_ds.SetProjection(img_data.GetProjection())
    del img_data
    target_ds.GetRasterBand(1).SetNoDataValue(9999)
    target_ds.GetRasterBand(1).WriteArray(result)
    target_ds.FlushCache()

    # 打开影像
    LoadImg(output_path)

def Improve_Calculate(filename, function, argument, output_path):
    print(filename)
    # 读取影像
    img_data = gdal.Open(filename)

    # 读取影像栅格行列数
    cols = img_data.RasterXSize  # 列数
    rows = img_data.RasterYSize  # 行数
    # 计算结果
    if function == 'TNWI':
        argument = argument[0]
        result = get_TNWI(img_data, argument, cols, rows)
    elif function == 'TMBCWI':
        argument = argument[1]
        result = get_TMBCWI(img_data, argument, cols, rows)
    elif function == 'PTMBCW':
        argument = argument[2]
        result = get_PTMBCW(img_data, argument, cols, rows)

    # 生成影像
    target_ds = gdal.GetDriverByName('GTiff').Create(output_path, xsize=cols, ysize=rows, bands=1,
                                                     eType=gdal.GDT_Float32)
    target_ds.SetGeoTransform(img_data.GetGeoTransform())
    target_ds.SetProjection(img_data.GetProjection())
    del img_data
    target_ds.GetRasterBand(1).SetNoDataValue(9999)
    target_ds.GetRasterBand(1).WriteArray(result)
    target_ds.FlushCache()

    # 打开影像
    LoadImg(output_path)
import tkinter as tk
from tkinter import filedialog

from src.Index_Loader import Create_Processor
from src.Improve_Index_Loader import  Improve_Create_Processor
from src.Threshold_Loader import  Create_ThreLoader
from src.LoadImg import LoadImg

root = tk.Tk()
root.title("影像处理小工具")
toolbar = tk.Frame(root)
toolbar.pack(side="top", fill="x")
root.resizable(width=False, height=False)

# 生成工具条按钮
button1 = tk.Button(toolbar, text="打开图像", width=8, height=3)
button2 = tk.Button(toolbar, text="常用指数", width=8, height=3)
button3 = tk.Button(toolbar, text="改进指数", width=8, height=3)
button4 = tk.Button(toolbar, text="阈值提取", width=8, height=3)

button1.pack(side="left")
button2.pack(side="left")
button3.pack(side="left")
button4.pack(side="left")

# 清洗缓存路径
def clean_path(all_path):
    new_paths = []
    for path in all_path:
        if path != '':
            new_paths.append(path)
    return new_paths

# 浏览图像
def Viewer_img(_now_file):
    path = filedialog.askopenfilename(title='请选择文件', filetypes=(("TIFF files", "*.tif"), ("ENVI files", "*.dat"), ("IMAGINE files", "*.img")))
    _now_file.append(path)
    LoadImg(path)
    # 在这里添加新窗口的内容

# 指数计算
def Index_process(_Index_new_file):
    Create_Processor(now_file, _Index_new_file)
    now_file.append(_Index_new_file[-1])

# 指数计算
def Improve_Index_process(_Index_new_file):
    Improve_Create_Processor(now_file, _Index_new_file)
    now_file.append(_Index_new_file[-1])

# 阈值提取
def Index_threshold():
    Create_ThreLoader(now_file)


now_file = []
Index_new_file = []
button1.config(command=lambda: Viewer_img(now_file))
button2.config(command=lambda: Index_process(Index_new_file))
button3.config(command=lambda: Improve_Index_process(Index_new_file))
button4.config(command=lambda: Index_threshold())


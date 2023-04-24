#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from src.Threshold_Process import Threshold_Calculate

# 补全文件名的方法
def supple_path(path):
        pathex = path.split('.')[-1]
        if pathex != 'tif':
                path = path + '.tif'
        return path

# 清洗缓存路径
def clean_path(all_path):
    new_paths = []
    for path in all_path:
        if path != '':
            new_paths.append(path)
    return new_paths

def Create_ThreLoader(filenames):
    filenames = clean_path(filenames)
    ThreLoader = tk.Toplevel()
    ThreLoader.title('按阈值二值化')
    ThreLoader.configure(height=200, width=400)
    ThreLoader.resizable(width=False, height=False)

    # 影像选取部分
    imageselect = ttk.Labelframe(ThreLoader)
    imageselect.configure(height=100, text='影像选取')
    image_path = ttk.Label(imageselect)
    image_path.configure(text='影像')
    image_path.grid(column=0, padx=7, row=0, sticky="w")
    path_combo = ttk.Combobox(imageselect)
    path_combo.configure(justify="center", values=filenames, width=34)
    path_combo.grid(column=1, padx=10, row=0)

    # 导入按钮
    def path_add():
        path = filedialog.askopenfilename(title='请选择文件',
                                          filetypes=(("TIFF files", "*.tif"), ("ENVI files", "*.dat"), ("IMAGINE files", "*.img") ))
        path_combo.set(path)
    add_path = ttk.Button(imageselect)
    add_path.configure(text='导入', width=9, command=path_add)
    add_path.grid(column=2, row=0, sticky="e")
    imageselect.grid(column=0, ipadx=5, ipady=5, row=0, sticky="w")

    # 处理方法部分
    index_process = ttk.Labelframe(ThreLoader)
    index_process.configure(height=200, text='阈值提取', width=300)
    index_notebook = ttk.Notebook(index_process)
    index_notebook.configure(height=80, width=400)
    # 自动阈值
    Auto_frame = ttk.Frame(index_notebook)
    Auto_frame.configure(height=200, width=400)
    Auto_label = ttk.Label(Auto_frame)
    Auto_label.configure(text='方法')
    Auto_label.grid(column=1, padx=20, pady=30, row=0)
    Auto_combo = ttk.Combobox(Auto_frame)
    Auto_combo.grid(column=2, row=0)
    Auto_combo.set('OTSU-大津法')
    Auto_combo.config(values=['OTSU-大津法', 'Kittler-凯勒法'])
    type_label1 = ttk.Label(Auto_frame)
    type_label1.configure(text='                  ')
    type_label1.grid(column=0, row=0)
    Auto_frame.grid(column=0, row=0)
    index_notebook.add(Auto_frame, text='自动阈值提取')
    # 手动阈值
    Manu_frame = ttk.Frame(index_notebook)
    Manu_frame.configure(height=200, width=200)
    Manu_label = ttk.Label(Manu_frame)
    Manu_label.configure(text='阈值')
    Manu_label.grid(column=1, padx=20, pady=30, row=0)
    Manu_entry = ttk.Entry(Manu_frame)
    Manu_entry.grid(column=2, row=0)
    type_label2 = ttk.Label(Manu_frame)
    type_label2.configure(text='                  ')
    type_label2.grid(column=0, row=0)
    Manu_frame.pack(side="top")
    index_notebook.add(Manu_frame, text='手动阈值提取')
    index_notebook.grid(column=0, row=0)
    index_process.grid(column=0, ipadx=5, ipady=5, row=2)

    # 输出参数部分
    output_labelframe = ttk.Labelframe(ThreLoader)
    output_labelframe.configure(height=200, text='输出', width=400)
    output_label = ttk.Label(output_labelframe)
    output_label.configure(text='  输出为…')
    output_label.grid(column=0, row=0)
    def output_path():
        path = filedialog.asksaveasfilename(title='请选择文件', filetypes=(("TIFF files", "*.tif"),))
        path = supple_path(path)
        file_outpath.set(path)
    file_outpath = tk.StringVar(value='')
    output_entry = ttk.Entry(output_labelframe, textvariable=file_outpath)
    output_entry.configure(width=34)
    output_entry.grid(column=1, padx=10, row=0)
    output_path_select = ttk.Button(output_labelframe)
    output_path_select.configure(text='浏览', width=9, command=output_path)
    output_path_select.grid(column=2, row=0)
    output_labelframe.grid(column=0, ipadx=5, ipady=5, row=3)

    # 确认按钮
    process = ttk.Frame(ThreLoader)
    process.configure(height=200, width=200)
    process_button = ttk.Button(process)

    # 开始处理
    def start_Calculate():
        # 读取参数
        filepath = path_combo.get()
        Main_function = index_notebook.tab(index_notebook.select(), "text")
        Auto_argu = Auto_combo.get()
        Manu_argu = Manu_entry.get()
        output = output_entry.get()
        # 关闭窗口
        ThreLoader.destroy()
        # 计算结果
        Threshold_Calculate(filepath, output, Main_function, Auto_argu, Manu_argu)
    process_button.configure(text='确定', command=start_Calculate)
    process_button.grid(column=0, row=0, sticky="e")
    process.grid(column=0, padx=5, pady=5, row=4)

    ThreLoader.wait_window()





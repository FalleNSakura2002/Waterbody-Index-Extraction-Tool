#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

from tkinter import filedialog
from src.LoadImg import GetBands
from src.Index_process import Improve_Calculate as Calculate

# 重组波段名称的方法
def get_bands(filename):
        band_num = GetBands(filename)
        band_list = []
        for i in range(band_num):
                band_list.append('Band ' + str(i + 1))
        return band_list

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

def Improve_Create_Processor(now_file, _Index_new_file):
        now_file = clean_path(now_file)
        Processor = tk.Toplevel()
        Processor.title('改进水体指数计算')
        Processor.resizable(width=False, height=False)
        Processor.configure(height=200, width=400)
        ## 影像选取窗口
        imageselect = ttk.Labelframe(Processor)
        imageselect.configure(height=100, text='影像选取')
        image_path = ttk.Label(imageselect)
        image_path.configure(text='影像')
        image_path.grid(column=0, padx=7, row=0, sticky="w")
        path_combo = ttk.Combobox(imageselect)
        path_combo.configure(justify="center", width=34, values=now_file)
        path_combo.grid(column=1, padx=10, row=0)
        # 定义更新波段选项的方法
        def update_bands(event):
                path = path_combo.get()
                band_list = get_bands(path)
                # 写入改进TNWI波段选择
                TNWI_nir_combo.config(values=band_list)
                TNWI_swir1_combo.config(values=band_list)
                TNWI_swir2_combo.config(values=band_list)
                TNWI_tmp_combo.config(values=band_list)
                # 写入TMBCWI界面
                TMBCWI_CA_combo.config(values=band_list)
                TMBCWI_gre_combo.config(values=band_list)
                TMBCWI_nir_combo.config(values=band_list)
                TMBCWI_swir1_combo.config(values=band_list)
                TMBCWI_swir2_combo.config(values=band_list)
                TMBCWI_tmp_combo.config(values=band_list)
                # 写入PTMBCW波段选择
                PTMBCW_CA_combo.config(values=band_list)
                PTMBCW_gre_combo.config(values=band_list)
                PTMBCW_nir_combo.config(values=band_list)
                PTMBCW_swir1_combo.config(values=band_list)
                PTMBCW_pan_combo.config(values=band_list)
                PTMBCW_tmp_combo.config(values=band_list)
        path_combo.bind('<<ComboboxSelected>>', update_bands)
        # 导入按钮
        def path_add():
                path = filedialog.askopenfilename(title='请选择文件',
                                                  filetypes=(("TIFF files", "*.tif"), ("ENVI files", "*.dat"), ("IMAGINE files", "*.img")))
                path_combo.set(path)
                band_list = get_bands(path)
                # 写入改进TNWI波段选择
                TNWI_nir_combo.config(values=band_list)
                TNWI_swir1_combo.config(values=band_list)
                TNWI_swir2_combo.config(values=band_list)
                TNWI_tmp_combo.config(values=band_list)
                # 写入TMBCWI界面
                TMBCWI_CA_combo.config(values=band_list)
                TMBCWI_gre_combo.config(values=band_list)
                TMBCWI_nir_combo.config(values=band_list)
                TMBCWI_swir1_combo.config(values=band_list)
                TMBCWI_swir2_combo.config(values=band_list)
                TMBCWI_tmp_combo.config(values=band_list)
                # 写入PTMBCW波段选择
                PTMBCW_CA_combo.config(values=band_list)
                PTMBCW_gre_combo.config(values=band_list)
                PTMBCW_nir_combo.config(values=band_list)
                PTMBCW_swir1_combo.config(values=band_list)
                PTMBCW_pan_combo.config(values=band_list)
                PTMBCW_tmp_combo.config(values=band_list)
        add_path = ttk.Button(imageselect)
        add_path.configure(text='导入', width=9, command=path_add)
        add_path.grid(column=2, row=0, sticky="e")
        imageselect.grid(column=0, ipadx=5, ipady=5, row=0, sticky="w")

        ## 指数选取窗口
        # 构建窗体
        index_process = ttk.Labelframe(Processor)
        index_process.configure(height=200, text='水体指数', width=300)
        index_notebook = ttk.Notebook(index_process)
        index_notebook.configure(height=200, width=400)
        # TNWI界面
        TNWI_frame = ttk.Frame(index_notebook)
        TNWI_frame.configure(height=200, width=400)
        TNWI_nir_label = ttk.Label(TNWI_frame)
        TNWI_nir_label.configure(text='近红外波段')
        TNWI_nir_label.grid(column=0, padx=60, pady=5, row=3, sticky="w")
        TNWI_nir_combo = ttk.Combobox(TNWI_frame)
        TNWI_nir_combo.configure(
                justify="center", state="readonly", width=20)
        TNWI_nir_combo.grid(column=1, row=3, sticky="e")
        TNWI_swir1_label = ttk.Label(TNWI_frame)
        TNWI_swir1_label.configure(text='短波红外波段一')
        TNWI_swir1_label.grid(column=0, padx=60, pady=5, row=4, sticky="w")
        TNWI_swir1_combo = ttk.Combobox(TNWI_frame)
        TNWI_swir1_combo.configure(
                justify="center", state="readonly", width=20)
        TNWI_swir1_combo.grid(column=1, row=4, sticky="e")
        TNWI_swir2_label = ttk.Label(TNWI_frame)
        TNWI_swir2_label.configure(text='短波红外波段二')
        TNWI_swir2_label.grid(column=0, padx=60, row=5, pady=5, sticky="w")
        TNWI_swir2_combo = ttk.Combobox(TNWI_frame)
        TNWI_swir2_combo.grid(column=1, row=5, sticky="e")
        TNWI_swir2_combo.configure(
                justify="center", state="readonly", width=20)
        TNWI_tmp_label = ttk.Label(TNWI_frame)
        TNWI_tmp_label.configure(text='地温波段')
        TNWI_tmp_label.grid(column=0, padx=60, pady=5, row=6, sticky="w")
        TNWI_tmp_combo = ttk.Combobox(TNWI_frame)
        TNWI_tmp_combo.configure(
                justify="center", state="readonly", width=20)
        TNWI_tmp_combo.grid(column=1, row=6, sticky="e")

        TNWI_frame.pack(side="top")
        index_notebook.add(TNWI_frame, text='TNWI')
        # TMBCWI界面
        TMBCWI_frame = ttk.Frame(index_notebook)
        TMBCWI_frame.configure(height=200, width=400)
        TMBCWI_CA_label = ttk.Label(TMBCWI_frame)
        TMBCWI_CA_label.configure(text='沿海气溶胶波段')
        TMBCWI_CA_label.grid(column=0, padx=60, pady=5, row=1, sticky="w")
        TMBCWI_CA_combo = ttk.Combobox(TMBCWI_frame)
        TMBCWI_CA_combo.configure(
                justify="center", state="readonly", width=20)
        TMBCWI_CA_combo.grid(column=1, row=1, sticky="e")
        TMBCWI_gre_label = ttk.Label(TMBCWI_frame)
        TMBCWI_gre_label.configure(text='绿光波段')
        TMBCWI_gre_label.grid(column=0, padx=60, pady=5, row=2, sticky="w")
        TMBCWI_gre_combo = ttk.Combobox(TMBCWI_frame)
        TMBCWI_gre_combo.configure(
                justify="center", state="readonly", width=20)
        TMBCWI_gre_combo.grid(column=1, row=2, sticky="e")
        TMBCWI_nir_label = ttk.Label(TMBCWI_frame)
        TMBCWI_nir_label.configure(text='近红外波段')
        TMBCWI_nir_label.grid(column=0, padx=60, pady=5, row=3, sticky="w")
        TMBCWI_nir_combo = ttk.Combobox(TMBCWI_frame)
        TMBCWI_nir_combo.configure(
                justify="center", state="readonly", width=20)
        TMBCWI_nir_combo.grid(column=1, row=3, sticky="e")
        TMBCWI_swir1_label = ttk.Label(TMBCWI_frame)
        TMBCWI_swir1_label.configure(text='短波红外波段一')
        TMBCWI_swir1_label.grid(column=0, padx=60, pady=5, row=4, sticky="w")
        TMBCWI_swir1_combo = ttk.Combobox(TMBCWI_frame)
        TMBCWI_swir1_combo.configure(
                justify="center", state="readonly", width=20)
        TMBCWI_swir1_combo.grid(column=1, row=4, sticky="e")
        TMBCWI_swir2_label = ttk.Label(TMBCWI_frame)
        TMBCWI_swir2_label.configure(text='短波红外波段二')
        TMBCWI_swir2_label.grid(column=0, padx=60, row=5, pady=5, sticky="w")
        TMBCWI_swir2_combo = ttk.Combobox(TMBCWI_frame)
        TMBCWI_swir2_combo.grid(column=1, row=5, sticky="e")
        TMBCWI_swir2_combo.configure(
                justify="center", state="readonly", width=20)
        TMBCWI_tmp_label = ttk.Label(TMBCWI_frame)
        TMBCWI_tmp_label.configure(text='地温波段')
        TMBCWI_tmp_label.grid(column=0, padx=60, row=6, pady=5, sticky="w")
        TMBCWI_tmp_combo = ttk.Combobox(TMBCWI_frame)
        TMBCWI_tmp_combo.grid(column=1, row=6, sticky="e")
        TMBCWI_tmp_combo.configure(
                justify="center", state="readonly", width=20)

        TMBCWI_frame.pack(side="top")
        index_notebook.add(TMBCWI_frame, text='TMBCWI')
        index_notebook.grid(column=0, row=0)
        index_process.grid(column=0, ipadx=5, ipady=5, row=2)
        # PTMBCW界面
        PTMBCW_frame = ttk.Frame(index_notebook)
        PTMBCW_frame.configure(height=200, width=400)
        PTMBCW_CA_label = ttk.Label(PTMBCW_frame)
        PTMBCW_CA_label.configure(text='沿海气溶胶波段')
        PTMBCW_CA_label.grid(column=0, padx=60, pady=5, row=1, sticky="w")
        PTMBCW_CA_combo = ttk.Combobox(PTMBCW_frame)
        PTMBCW_CA_combo.configure(
                justify="center", state="readonly", width=20)
        PTMBCW_CA_combo.grid(column=1, row=1, sticky="e")
        PTMBCW_gre_label = ttk.Label(PTMBCW_frame)
        PTMBCW_gre_label.configure(text='绿光波段')
        PTMBCW_gre_label.grid(column=0, padx=60, pady=5, row=2, sticky="w")
        PTMBCW_gre_combo = ttk.Combobox(PTMBCW_frame)
        PTMBCW_gre_combo.configure(
                justify="center", state="readonly", width=20)
        PTMBCW_gre_combo.grid(column=1, row=2, sticky="e")
        PTMBCW_nir_label = ttk.Label(PTMBCW_frame)
        PTMBCW_nir_label.configure(text='近红外波段')
        PTMBCW_nir_label.grid(column=0, padx=60, pady=5, row=3, sticky="w")
        PTMBCW_nir_combo = ttk.Combobox(PTMBCW_frame)
        PTMBCW_nir_combo.configure(
                justify="center", state="readonly", width=20)
        PTMBCW_nir_combo.grid(column=1, row=3, sticky="e")
        PTMBCW_swir1_label = ttk.Label(PTMBCW_frame)
        PTMBCW_swir1_label.configure(text='短波红外波段一')
        PTMBCW_swir1_label.grid(column=0, padx=60, pady=5, row=4, sticky="w")
        PTMBCW_swir1_combo = ttk.Combobox(PTMBCW_frame)
        PTMBCW_swir1_combo.configure(
                justify="center", state="readonly", width=20)
        PTMBCW_swir1_combo.grid(column=1, row=4, sticky="e")
        PTMBCW_pan_label = ttk.Label(PTMBCW_frame)
        PTMBCW_pan_label.configure(text='全色波段')
        PTMBCW_pan_label.grid(column=0, padx=60, row=5, pady=5, sticky="w")
        PTMBCW_pan_combo = ttk.Combobox(PTMBCW_frame)
        PTMBCW_pan_combo.grid(column=1, row=5, sticky="e")
        PTMBCW_pan_combo.configure(
                justify="center", state="readonly", width=20)
        PTMBCW_tmp_label = ttk.Label(PTMBCW_frame)
        PTMBCW_tmp_label.configure(text='地温波段')
        PTMBCW_tmp_label.grid(column=0, padx=60, row=6, pady=5, sticky="w")
        PTMBCW_tmp_combo = ttk.Combobox(PTMBCW_frame)
        PTMBCW_tmp_combo.grid(column=1, row=6, sticky="e")
        PTMBCW_tmp_combo.configure(
                justify="center", state="readonly", width=20)

        PTMBCW_frame.pack(side="top")
        index_notebook.add(PTMBCW_frame, text='PTMBCW')
        index_notebook.grid(column=0, row=0)
        index_process.grid(column=0, ipadx=5, ipady=5, row=2)

        ## 输出参数窗口
        output_labelframe = ttk.Labelframe(Processor)
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

        ## 确认按钮
        process = ttk.Frame(Processor)
        process.configure(height=200, width=200)
        process_button = ttk.Button(process)

        def start_Calculate():
                # 读取参数
                filepath = path_combo.get()
                function = index_notebook.tab(index_notebook.select(), "text")
                output = output_entry.get()
                band_selected = []
                # TNWI方法的波段选择
                index_band = []
                index_band.append(TNWI_nir_combo.get())
                index_band.append(TNWI_swir1_combo.get())
                index_band.append(TNWI_swir2_combo.get())
                index_band.append(TNWI_tmp_combo.get())
                band_selected.append(index_band)
                # TMBCWI方法的波段选择
                index_band = []
                index_band.append(TMBCWI_CA_combo.get())
                index_band.append(TMBCWI_gre_combo.get())
                index_band.append(TMBCWI_nir_combo.get())
                index_band.append(TMBCWI_swir1_combo.get())
                index_band.append(TMBCWI_swir2_combo.get())
                index_band.append(TMBCWI_tmp_combo.get())
                band_selected.append(index_band)
                # PTMBCW方法的波段选择
                index_band = []
                index_band.append(PTMBCW_CA_combo.get())
                index_band.append(PTMBCW_gre_combo.get())
                index_band.append(PTMBCW_nir_combo.get())
                index_band.append(PTMBCW_swir1_combo.get())
                index_band.append(PTMBCW_pan_combo.get())
                index_band.append(PTMBCW_tmp_combo.get())
                band_selected.append(index_band)
                # 关闭窗口
                Processor.destroy()
                _Index_new_file.append(output)
                # 计算结果
                Calculate(filepath, function, band_selected, output)

        process_button.configure(text='确定', command=start_Calculate)
        process_button.grid(column=0, row=0, sticky="e")
        process.grid(column=0, padx=5, pady=5, row=4)

        path = output_entry.get()

        Processor.wait_window()
        return path


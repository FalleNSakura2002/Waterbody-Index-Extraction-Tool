#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

from tkinter import filedialog
from src.LoadImg import GetBands
from src.Index_process import Calculate

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

def Create_Processor(now_file, _Index_new_file):
        now_file = clean_path(now_file)
        Processor = tk.Toplevel()
        Processor.title('常用水体指数计算')
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
                # 写入NDWI波段选择
                NDWI_gre_combo.config(values=band_list)
                NDWI_nir_combo.config(values=band_list)
                # 写入MNDWI波段选择
                MNDWI_gre_combo.config(values=band_list)
                MNDWI_swir_combo.config(values=band_list)
                # 写入NWI波段选择
                NWI_blu_combo.config(values=band_list)
                NWI_nir_combo.config(values=band_list)
                NWI_swir1_combo.config(values=band_list)
                NWI_swir2_combo.config(values=band_list)
                # 写入FNDWI波段选择
                FNDWI_gre_combo.config(values=band_list)
                FNDWI_nir_combo.config(values=band_list)
                # 写入CIWI波段选择
                CIWI_red_combo.config(values=band_list)
                CIWI_nir_combo.config(values=band_list)
                CIWI_swir_combo.config(values=band_list)
        path_combo.bind('<<ComboboxSelected>>', update_bands)
        # 导入按钮
        def path_add():
                path = filedialog.askopenfilename(title='请选择文件',
                                                  filetypes=(("TIFF files", "*.tif"), ("ENVI files", "*.dat"), ("IMAGINE files", "*.img")))
                path_combo.set(path)
                band_list = get_bands(path)
                # 写入NDWI波段选择
                NDWI_gre_combo.config(values=band_list)
                NDWI_nir_combo.config(values=band_list)
                # 写入MNDWI波段选择
                MNDWI_gre_combo.config(values=band_list)
                MNDWI_swir_combo.config(values=band_list)
                # 写入NWI波段选择
                NWI_blu_combo.config(values=band_list)
                NWI_nir_combo.config(values=band_list)
                NWI_swir1_combo.config(values=band_list)
                NWI_swir2_combo.config(values=band_list)
                # 写入FNDWI波段选择
                FNDWI_gre_combo.config(values=band_list)
                FNDWI_nir_combo.config(values=band_list)
                # 写入CIWI波段选择
                CIWI_red_combo.config(values=band_list)
                CIWI_nir_combo.config(values=band_list)
                CIWI_swir_combo.config(values=band_list)
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
        # NDWI界面
        NDWI_frame = ttk.Frame(index_notebook)
        NDWI_frame.configure(height=200, width=400)
        NDWI_gre_label = ttk.Label(NDWI_frame)
        NDWI_gre_label.configure(text='绿光波段')
        NDWI_gre_label.grid(column=0, padx=60, pady=20, row=1, sticky="w")
        NDWI_gre_combo = ttk.Combobox(NDWI_frame)
        NDWI_gre_combo.configure(
            justify="center", state="readonly", width=20)
        NDWI_gre_combo.grid(column=1, row=1, sticky="e")
        NDWI_nir_label = ttk.Label(NDWI_frame)
        NDWI_nir_label.configure(text='近红外波段')
        NDWI_nir_label.grid(column=0, padx=60, row=2, sticky="w")
        NDWI_nir_combo = ttk.Combobox(NDWI_frame)
        NDWI_nir_combo.grid(column=1, row=2, sticky="e")
        NDWI_nir_combo.configure(
                justify="center", state="readonly", width=20)
        NDWI_frame.pack(side="top")
        index_notebook.add(NDWI_frame, text='NDWI')
        # MNDWI界面
        MNDWI_frame = ttk.Frame(index_notebook)
        MNDWI_frame.configure(height=200, width=400)
        MNDWI_gre_label = ttk.Label(MNDWI_frame)
        MNDWI_gre_label.configure(text='绿光波段')
        MNDWI_gre_label.grid(column=0, padx=60, pady=20, row=1, sticky="w")
        MNDWI_gre_combo = ttk.Combobox(MNDWI_frame)
        MNDWI_gre_combo.configure(
                justify="center", state="readonly", width=20)
        MNDWI_gre_combo.grid(column=1, row=1, sticky="e")
        MNDWI_swir_label = ttk.Label(MNDWI_frame)
        MNDWI_swir_label.configure(text='短波红外波段')
        MNDWI_swir_label.grid(column=0, padx=60, row=2, sticky="w")
        MNDWI_swir_combo = ttk.Combobox(MNDWI_frame)
        MNDWI_swir_combo.grid(column=1, row=2, sticky="e")
        MNDWI_swir_combo.configure(
                justify="center", state="readonly", width=20)
        MNDWI_frame.pack(side="top")
        index_notebook.add(MNDWI_frame, text='MNDWI')
        index_notebook.grid(column=0, row=0)
        index_process.grid(column=0, ipadx=5, ipady=5, row=2)
        # NWI界面
        NWI_frame = ttk.Frame(index_notebook)
        NWI_frame.configure(height=200, width=400)
        NWI_blu_label = ttk.Label(NWI_frame)
        NWI_blu_label.configure(text='蓝光波段')
        NWI_blu_label.grid(column=0, padx=60, pady=10, row=1, sticky="w")
        NWI_blu_combo = ttk.Combobox(NWI_frame)
        NWI_blu_combo.configure(
                justify="center", state="readonly", width=20)
        NWI_blu_combo.grid(column=1, row=1, sticky="e")
        NWI_nir_label = ttk.Label(NWI_frame)
        NWI_nir_label.configure(text='近红外波段')
        NWI_nir_label.grid(column=0, padx=60, pady=10, row=2, sticky="w")
        NWI_nir_combo = ttk.Combobox(NWI_frame)
        NWI_nir_combo.configure(
                justify="center", state="readonly", width=20)
        NWI_nir_combo.grid(column=1, row=2, sticky="e")
        NWI_swir1_label = ttk.Label(NWI_frame)
        NWI_swir1_label.configure(text='短波红外波段一')
        NWI_swir1_label.grid(column=0, padx=60, pady=10, row=3, sticky="w")
        NWI_swir1_combo = ttk.Combobox(NWI_frame)
        NWI_swir1_combo.configure(
                justify="center", state="readonly", width=20)
        NWI_swir1_combo.grid(column=1, row=3, sticky="e")
        NWI_swir2_label = ttk.Label(NWI_frame)
        NWI_swir2_label.configure(text='短波红外波段二')
        NWI_swir2_label.grid(column=0, padx=60, row=4, pady=10, sticky="w")
        NWI_swir2_combo = ttk.Combobox(NWI_frame)
        NWI_swir2_combo.grid(column=1, row=4, sticky="e")
        NWI_swir2_combo.configure(
                justify="center", state="readonly", width=20)

        NWI_frame.pack(side="top")
        index_notebook.add(NWI_frame, text='NWI')
        index_notebook.grid(column=0, row=0)
        index_process.grid(column=0, ipadx=5, ipady=5, row=2)
        # FNDWI界面
        FNDWI_frame = ttk.Frame(index_notebook)
        FNDWI_frame.configure(height=200, width=400)
        FNDWI_gre_label = ttk.Label(FNDWI_frame)
        FNDWI_gre_label.configure(text='绿光波段')
        FNDWI_gre_label.grid(column=0, padx=60, pady=20, row=1, sticky="w")
        FNDWI_gre_combo = ttk.Combobox(FNDWI_frame)
        FNDWI_gre_combo.configure(
                justify="center", state="readonly", width=20)
        FNDWI_gre_combo.grid(column=1, row=1, sticky="e")
        FNDWI_nir_label = ttk.Label(FNDWI_frame)
        FNDWI_nir_label.configure(text='近红外波段')
        FNDWI_nir_label.grid(column=0, padx=60, row=2, sticky="w")
        FNDWI_nir_combo = ttk.Combobox(FNDWI_frame)
        FNDWI_nir_combo.grid(column=1, row=2, sticky="e")
        FNDWI_nir_combo.configure(
                justify="center", state="readonly", width=20)
        FNDWI_frame.pack(side="top")
        index_notebook.add(FNDWI_frame, text='FNDWI')
        # CIWI界面
        CIWI_frame = ttk.Frame(index_notebook)
        CIWI_frame.configure(height=200, width=400)
        CIWI_red_label = ttk.Label(CIWI_frame)
        CIWI_red_label.configure(text='红光波段')
        CIWI_red_label.grid(column=0, padx=60, pady=20, row=1, sticky="w")
        CIWI_red_combo = ttk.Combobox(CIWI_frame)
        CIWI_red_combo.configure(
                justify="center", state="readonly", width=20)
        CIWI_red_combo.grid(column=1, row=1, sticky="e")
        CIWI_nir_label = ttk.Label(CIWI_frame)
        CIWI_nir_label.configure(text='近红外波段')
        CIWI_nir_label.grid(column=0, padx=60, row=2, sticky="w")
        CIWI_nir_combo = ttk.Combobox(CIWI_frame)
        CIWI_nir_combo.grid(column=1, row=2, sticky="e")
        CIWI_nir_combo.configure(
                justify="center", state="readonly", width=20)
        CIWI_swir_label = ttk.Label(CIWI_frame)
        CIWI_swir_label.configure(text='短波红外波段')
        CIWI_swir_label.grid(column=0, padx=60, pady=20, row=3, sticky="w")
        CIWI_swir_combo = ttk.Combobox(CIWI_frame)
        CIWI_swir_combo.grid(column=1, row=3, sticky="e")
        CIWI_swir_combo.configure(
                justify="center", state="readonly", width=20)

        CIWI_frame.pack(side="top")
        index_notebook.add(CIWI_frame, text='CIWI')

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
                # NDWI方法的波段选择
                index_band = []
                index_band.append(NDWI_gre_combo.get())
                index_band.append(NDWI_nir_combo.get())
                band_selected.append(index_band)
                # MNDWI方法的波段选择
                index_band = []
                index_band.append(MNDWI_gre_combo.get())
                index_band.append(MNDWI_swir_combo.get())
                band_selected.append(index_band)
                # NWI方法的波段选择
                index_band = []
                index_band.append(NWI_blu_combo.get())
                index_band.append(NWI_nir_combo.get())
                index_band.append(NWI_swir1_combo.get())
                index_band.append(NWI_swir2_combo.get())
                band_selected.append(index_band)
                # FNDWI方法的波段选择
                index_band = []
                index_band.append(FNDWI_gre_combo.get())
                index_band.append(FNDWI_nir_combo.get())
                band_selected.append(index_band)
                # CIWI方法的波段选择
                index_band = []
                index_band.append(CIWI_red_combo.get())
                index_band.append(CIWI_nir_combo.get())
                index_band.append(CIWI_swir_combo.get())
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


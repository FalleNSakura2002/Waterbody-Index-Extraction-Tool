from tkinter import *
from tkinter import  ttk


def submit(_BL, _comboxlist_R, _comboxlist_G, _comboxlist_B, _return_value):
    # 获取输入框的值存入_return_value中
    _return_value[0] = _comboxlist_R.get()
    _return_value[1] = _comboxlist_G.get()
    _return_value[2] = _comboxlist_B.get()
    # 关闭子窗口
    _BL.destroy()

def Create_Loader(_return_value, band_list):
    BL = Tk()
    BL.title("选择加载波段")
    BL.geometry('250x200')
    BL.resizable(width=False, height=False)

    # 添加一个标签来显示选择的文件
    # R波段选择
    filename_label_R = Label(BL, text="R-")
    filename_label_R.pack()
    R = StringVar()
    comboxlist_R=ttk.Combobox(BL, textvariable=R, state="readonly")
    comboxlist_R["values"]=(band_list)
    comboxlist_R.pack()
    # G波段选择
    filename_label_G = Label(BL, text="G-")
    filename_label_G.pack()
    G = StringVar()
    comboxlist_G=ttk.Combobox(BL, textvariable=G, state="readonly")
    comboxlist_G["values"]=(band_list)
    comboxlist_G.pack()
    # B波段选择
    filename_label_B = Label(BL, text="B-")
    filename_label_B.pack()
    B = StringVar()
    comboxlist_B=ttk.Combobox(BL, textvariable=B, state="readonly")
    comboxlist_B["values"]=(band_list)
    comboxlist_B.pack()
    check_button = Button(BL, text='确认', width=10, command=lambda: submit(BL, comboxlist_R, comboxlist_G, comboxlist_B, _return_value))
    check_button.pack()

    BL.wait_window()


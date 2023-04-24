import matplotlib.pyplot as plt

def display(filename, image, argu):
    # 创建一个包含单个Axes对象的Figure
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title(filename)
    fig.set_size_inches(10, 8)

    # 显示图像
    if argu == 1:
        im = ax.imshow(image, cmap='gray')
    else:
        im = ax.imshow(image)

    # 设置纵横比
    ax.axis('off')

    # 开启滚轮缩放
    plt.connect('scroll_event', lambda event: zoom(event, ax))


    # 定义缩放函数
    def zoom(event, ax):
        base_scale = 1.1
        cur_xlim = ax.get_xlim()
        cur_ylim = ax.get_ylim()
        xdata = event.xdata  # 获得当前鼠标位置的数据值
        ydata = event.ydata
        if event.button == 'up':
            # 缩小
            scale_factor = 1 / base_scale
        elif event.button == 'down':
            # 放大
            scale_factor = base_scale
        else:
            # 忽略其他情况
            scale_factor = 1
        # 计算新的范围
        new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
        new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor
        relx = (cur_xlim[1] - xdata) / (cur_xlim[1] - cur_xlim[0])
        rely = (cur_ylim[1] - ydata) / (cur_ylim[1] - cur_ylim[0])
        new_left = xdata - new_width * (1 - relx)
        new_right = xdata + new_width * relx
        new_bottom = ydata - new_height * (1 - rely)
        new_top = ydata + new_height * rely
        # 设置新的范围
        ax.set_xlim(new_left, new_right)
        ax.set_ylim(new_bottom, new_top)
        plt.draw()

    plt.tight_layout()
    plt.show()

import tkinter as tk

from FormalProject.data1 import data1


def analysis():
    page = tk.Tk()
    page.geometry('900x600')
    page.title('车辆连续跟踪与跨境识别系统')
    # page.config(background='white')
    # 标题文字
    headText = tk.Label(page, text='结果分析', bg='pink', width=30, height=2)
    headText.place(x=10, y=10)
    # 长段文字
    text = tk.Label(page, text='测试视频数量\n\n测试照片数量\n\n每辆车平均检测时长\n\n需要重识别车辆数\n\n每辆车平均匹配车辆数')
    text.place(x=20, y=100)
    # 按钮
    btn = tk.Button(page, text='Ctrl + s\n导出最终相似度结果', bg='pink', command=data1)
    btn.place(x=600, y=200)
    # 文字
    selectText = tk.Label(page, text='选择路径')
    selectText.place(x=550, y=300)
    # 选择框
    inputURL = tk.Entry(page)
    inputURL.insert(0, 'C:/myFolder')
    inputURL.place(x=620, y=300)
    page.mainloop()

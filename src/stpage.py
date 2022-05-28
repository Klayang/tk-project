import tkinter as tk

from FormalProject.data import data


def stpage():
    page = tk.Toplevel()
    page.geometry('900x600')
    page.title('车辆连续跟踪与跨境识别系统')
    # page.config(background='white')
    # 标题文字
    headText = tk.Label(page, text='单镜头下的车辆检测与连续跟踪', bg='pink', width=30, height=2, font=('仿宋', 15, 'bold'))
    headText.place(x=10, y=10)
    # 输入视频界面
    inputVideo = tk.Label(page, bg='black', width=50, height=15)
    inputVideo.place(x=10, y=120)
    # 提示文字
    commandText = tk.Label(page, text='请选择要检测的视频', width=20, height=1)
    commandText.place(x=0, y=450)
    # 创建用户输入框
    inputVideo = tk.Entry(page)
    inputVideo.insert(0, 'C:/users/max/Desktop/河北/视频1.mp4')
    inputVideo.place(x=150, y=450)
    # 创建“选择”按钮
    selectBtn = tk.Button(page, bg='pink', width=6, height=1, text='选择')
    selectBtn.place(x=300, y=450)
    # 提示文字2
    resultText = tk.Label(page, text='检测结果', width=10, height=1)
    resultText.place(x=640, y=80)
    # 输出视频
    outputVideo = tk.Label(page, bg='black', width=50, height=15)
    outputVideo.place(x=500, y=120)
    # 开始播放按钮
    play = tk.Button(page, text='按enter以开始', bg='pink', command=data)
    play.place(x=630, y=450)
    page.mainloop()

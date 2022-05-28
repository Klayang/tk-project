import tkinter as tk

from FormalProject.mtpage1 import mtpage1


def mtpage():
    page = tk.Toplevel()
    page.geometry('900x600')
    page.title('车辆连续跟踪与跨境识别系统')
    # 标题文字
    headText = tk.Label(page, text='跨镜头下的车辆重识别', bg='pink', width=30, height=2)
    headText.place(x=10, y=10)
    # 输入视频界面
    inputVideo = tk.Label(page, bg='black', width=50, height=15)
    inputVideo.place(x=10, y=120)
    # 提示文字
    commandText = tk.Label(page, text='请选择要检测的视频', width=20, height=1)
    commandText.place(x=0, y=450)
    # 创建用户输入框
    inputVideo = tk.Entry(page)
    inputVideo.insert(0, 'C:/users/video1.mp4')
    inputVideo.place(x=150, y=450)
    # 创建“选择”按钮
    selectBtn = tk.Button(page, bg='pink', width=6, height=1, text='选择')
    selectBtn.place(x=300, y=450)
    # 创建5个输出视频
    for i in range(0, 5):
        outputVideo = tk.Label(page, bg='black', width=10, height=4)
        outputVideo.place(x=480, y=20 + i * 100)
    # 设置画布
    cv = tk.Canvas(page, width=120, height=500)
    cv.place(x=360, y=20)
    # 画箭头
    for i in range(0, 5):
        line = cv.create_line([(0, 260), (120, 20 + i * 105)], arrow=tk.LAST)
    # 创建输出小图
    carIg = tk.PhotoImage(file='car.gif')
    carImage = tk.Label(page, image=carIg)
    carImage.place(x=700, y=200)
    # 小图文字
    imageText = tk.Label(page, text='图片1')
    imageText.place(x=750, y=150)
    # 开始按钮
    startBtn = tk.Button(page, text='按Enter以开始', bg='pink', command=mtpage1)
    startBtn.place(x=730, y=350)
    # 设置第二块画布
    cv1 = tk.Canvas(page, width=150, height=500)
    cv1.place(x=550, y=20)
    # 设置箭头
    line1 = cv1.create_line([(0, 30), (150, 250)], arrow=tk.LAST)
    page.mainloop()

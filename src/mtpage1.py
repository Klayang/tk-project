import tkinter as tk


def mtpage1():
    page = tk.Toplevel()
    page.geometry('900x600')
    page.title('车辆连续跟踪与跨境识别系统')
    # 标题文字
    headText = tk.Label(page, text='跨镜头下的车辆重识别', bg='pink', width=30, height=2)
    headText.place(x=10, y=10)
    # 界面1
    inputVideo = tk.Label(page, bg='black', width=20, height=8)
    inputVideo.place(x=10, y=200)
    # 源视频
    sourceVideo = tk.Label(page, bg='black', width=20, height=8)
    sourceVideo.place(x=200, y=200)
    # 提示文字
    commandText = tk.Label(page, text='源视频', width=20, height=1)
    commandText.place(x=200, y=170)
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
    carImage = tk.Label(page, width=20, height=8, bg='black')
    carImage.place(x=700, y=200)
    # 小图文字
    imageText = tk.Label(page, text='下一个')
    imageText.place(x=750, y=360)
    # # 开始按钮
    # startBtn = tk.Button(page, text='按Enter以开始', bg='pink')
    # startBtn.place(x=730, y=350)
    # 设置第二块画布
    cv1 = tk.Canvas(page, width=150, height=500)
    cv1.place(x=100, y=50)
    # 设置箭头
    line1 = cv1.create_line([(0, 220), (150, 220)], arrow=tk.BOTH, width=5)
    page.mainloop()

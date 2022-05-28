import tkinter as tk

# from FormalProject.mtpage import mtpage
# from FormalProject.stpage import stpage


def mtpage1():
    page = tk.Toplevel()
    page.geometry('900x600')
    page.title('车辆连续跟踪与跨境识别系统')
    # 标题文字
    headText = tk.Label(page, text='跨镜头下的车辆重识别', bg='pink', width=30, height=2)
    headText.place(x=10, y=10)
    # 界面1
    image = tk.PhotoImage(file='p7.gif')
    inputVideo = tk.Label(page, image=image, width=100, height=100)
    inputVideo.place(x=10, y=200)
    # 源视频
    image1 = tk.PhotoImage(file='p8.gif')
    sourceVideo = tk.Label(page, image=image1, width=250, height=100)
    sourceVideo.place(x=200, y=200)
    # 提示文字
    commandText = tk.Label(page, text='源视频', width=20, height=1)
    commandText.place(x=200, y=170)
    # 创建5个输出视频
    image2 = tk.PhotoImage(file='p9.gif')
    outputVideo = tk.Label(page, image=image2, width=80, height=80)
    outputVideo.place(x=480, y=20)

    image3 = tk.PhotoImage(file='p10.gif')
    outputVideo1 = tk.Label(page, image=image3, width=80, height=80)
    outputVideo1.place(x=480, y=120)

    image4 = tk.PhotoImage(file='p11.gif')
    outputVideo2 = tk.Label(page, image=image4, width=80, height=80)
    outputVideo2.place(x=480, y=220)

    image5 = tk.PhotoImage(file='p12.gif')
    outputVideo3 = tk.Label(page, image=image5, width=80, height=80)
    outputVideo3.place(x=480, y=320)

    # 设置画布
    cv = tk.Canvas(page, width=120, height=500)
    cv.place(x=360, y=10)
    # 画箭头
    for i in range(0, 4):
        line = cv.create_line([(0, 260), (120, 20 + i * 120)], arrow=tk.LAST)
    # 创建输出小图
    image6 = tk.PhotoImage(file='p13.gif')
    carImage = tk.Label(page, width=180, height=150, image=image6)
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


def data2():
    page = tk.Toplevel()
    page.geometry('900x600')
    page.title('车辆连续跟踪与跨境识别系统')
    # 标题文字
    headText = tk.Label(page, text='检测数据统计', bg='pink', width=30, height=2)
    headText.place(x=10, y=10)
    # 数据统计图
    ig = tk.PhotoImage(file='graph2.gif')
    graph = tk.Label(page, image=ig)
    graph.place(x=10, y=150)
    # 提示文字
    text = tk.Label(page, text='选择路径')
    text.place(x=600, y=100)
    # 输入框
    inputURL = tk.Entry(page)
    inputURL.insert(0, 'C:/myFolder')
    inputURL.place(x=680, y=100)
    # 保存按钮
    btn = tk.Button(page, width=12, height=2, text='保存并导出结果', bg='pink')
    btn.place(x=660, y=30)
    page.mainloop()

def data1():
    page = tk.Toplevel()
    page.geometry('900x600')
    page.title('车辆连续跟踪与跨境识别系统')
    # 标题文字
    headText = tk.Label(page, text='检测数据统计', bg='pink', width=30, height=2)
    headText.place(x=10, y=10)
    # 数据统计图
    ig = tk.PhotoImage(file='graph1.gif')
    graph = tk.Label(page, image=ig)
    graph.place(x=10, y=150)
    # 提示文字
    text = tk.Label(page, text='选择路径')
    text.place(x=600, y=100)
    # 输入框
    inputURL = tk.Entry(page)
    inputURL.insert(0, 'C:/myFolder')
    inputURL.place(x=680, y=100)
    # 保存按钮
    btn = tk.Button(page, width=12, height=2, text='保存并导出结果', bg='pink', command=data2)
    btn.place(x=660, y=30)
    page.mainloop()

def statistics3():
    page = tk.Toplevel()
    page.geometry('1000x600')
    page.title('车辆连续跟踪与跨境识别系统')
    # 标题文字
    headText = tk.Label(page, text='检测数据统计', bg='pink', width=30, height=2, font=('仿宋', 15, 'bold'))
    headText.place(x=10, y=10)
    # 图片1
    ig = tk.PhotoImage(file='type1.gif')
    graph = tk.Label(page, image=ig)
    graph.place(x=10, y=200)
    # 图片2
    ig1 = tk.PhotoImage(file='type.gif')
    graph1 = tk.Label(page, image=ig1)
    graph1.place(x=500, y=200)
    # 提示文字
    text = tk.Label(page, text='选择路径')
    text.place(x=600, y=520)
    # 输入框
    inputURL = tk.Entry(page)
    inputURL.insert(0, 'C:/myFolder')
    inputURL.place(x=680, y=520)
    # 保存按钮
    btn = tk.Button(page, width=12, height=2, text='保存并导出结果', bg='pink', command=similarity)
    btn.place(x=660, y=450)
    page.mainloop()


def statistics2():
    page = tk.Toplevel()
    page.geometry('1000x600')
    page.title('车辆连续跟踪与跨境识别系统')
    # 标题文字
    headText = tk.Label(page, text='检测数据统计', bg='pink', width=30, height=2, font=('仿宋', 15, 'bold'))
    headText.place(x=10, y=10)
    # 图片1
    ig = tk.PhotoImage(file='color1.gif')
    graph = tk.Label(page, image=ig)
    graph.place(x=10, y=200)
    # 图片2
    ig1 = tk.PhotoImage(file='color.gif')
    graph1 = tk.Label(page, image=ig1)
    graph1.place(x=500, y=200)
    # 提示文字
    text = tk.Label(page, text='选择路径')
    text.place(x=600, y=550)
    # 输入框
    inputURL = tk.Entry(page)
    inputURL.insert(0, 'C:/myFolder')
    inputURL.place(x=680, y=550)
    # 保存按钮
    btn = tk.Button(page, width=12, height=2, text='保存并导出结果', bg='pink', command=statistics3)
    btn.place(x=660, y=480)
    page.mainloop()


def statistics1():
    page = tk.Toplevel()
    page.geometry('1000x600')
    page.title('车辆连续跟踪与跨境识别系统')
    # 标题文字
    headText = tk.Label(page, text='检测数据统计', bg='pink', width=30, height=2, font=('仿宋', 15, 'bold'))
    headText.place(x=10, y=10)
    # 文字1
    headText = tk.Label(page, text='检测到的不同颜⾊的⻋辆数随时间变化', width=30, height=2)
    headText.place(x=60, y=130)
    # 图片1
    ig = tk.PhotoImage(file='dataGraph1.gif')
    graph = tk.Label(page, image=ig)
    graph.place(x=10, y=200)
    # 文字2
    headText1 = tk.Label(page, text='检测到的不同类型的⻋辆数随时间变化', width=30, height=2)
    headText1.place(x=550, y=130)
    # 图片2
    ig1 = tk.PhotoImage(file='dataGraph3.gif')
    graph1 = tk.Label(page, image=ig1)
    graph1.place(x=500, y=200)
    # 提示文字
    text = tk.Label(page, text='选择路径')
    text.place(x=600, y=500)
    # 输入框
    inputURL = tk.Entry(page)
    inputURL.insert(0, 'C:/myFolder')
    inputURL.place(x=680, y=500)
    # 保存按钮
    btn = tk.Button(page, width=12, height=2, text='保存并导出结果', bg='pink', command=statistics2)
    btn.place(x=660, y=420)
    page.mainloop()


def analysis():
    page = tk.Tk()
    page.geometry('900x600')
    page.title('车辆连续跟踪与跨境识别系统')
    # page.config(background='white')
    # 标题文字
    headText = tk.Label(page, text='结果分析', bg='pink', width=30, height=2)
    headText.place(x=10, y=10)
    # 长段文字
    text = tk.Label(page, text='测试视频数量: 10\n\n测试照片数量: 100\n\n每辆车平均检测时长: 2s\n\n需要重识别车辆数: 5\n\n每辆车平均匹配车辆数: 10')
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

def similarity():
    page = tk.Toplevel()
    page.geometry('900x600')
    page.title('车辆连续跟踪与跨境识别系统')
    # page.config(background='white')
    # 标题文字
    headText = tk.Label(page, text='最终相似度', bg='pink', width=30, height=2)
    headText.place(x=10, y=10)
    # 文字
    text = tk.Label(page, text='相似度判别机制公开\n\n最终相似度=0.15*Sift相似度+0.7*颜色相似度+0.15*孪生网络相似度\n\n若最大相似度<60%，则认为匹配失败\n\n如需了解更多请联系我们')
    text.place(x=500, y=20)
    # Top5s
    topText = tk.Label(page, text='Top5s')
    topText.place(x=400, y=200)
    # 5张图片
    filename = ['p14.gif', 'p15.gif', 'p16.gif', 'p17.gif', 'p18.gif']

    ig = tk.PhotoImage(file='p14.gif')
    image = tk.Label(page, width=100, height=100, image=ig)
    image.place(x=50, y=300)

    ig1 = tk.PhotoImage(file='p15.gif')
    image1 = tk.Label(page, width=100, height=100, image=ig1)
    image1.place(x=200, y=300)

    ig2 = tk.PhotoImage(file='p16.gif')
    image2 = tk.Label(page, width=100, height=100, image=ig2)
    image2.place(x=350, y=300)

    ig3 = tk.PhotoImage(file='p17.gif')
    image3 = tk.Label(page, width=100, height=100, image=ig3)
    image3.place(x=500, y=300)

    ig4 = tk.PhotoImage(file='p18.gif')
    image4 = tk.Label(page, width=100, height=100, image=ig4)
    image4.place(x=650, y=300)

    # # 结果分析按钮
    # btn = tk.Button(page, text='按Enter进行结果分析', bg='pink', command=statistics1)
    # btn.place(x=650, y=460)
    page.mainloop()



def data():
    page = tk.Toplevel()
    page.geometry('900x600')
    page.title('车辆连续跟踪与跨境识别系统')
    # 标题文字
    headText = tk.Label(page, text='检测数据统计', bg='pink', width=30, height=2)
    headText.place(x=10, y=10)
    # 数据统计图
    ig = tk.PhotoImage(file='graph.gif')
    graph = tk.Label(page, image=ig)
    graph.place(x=10, y=100)
    # 提示文字
    text = tk.Label(page, text='选择路径')
    text.place(x=600, y=300)
    # 输入框
    inputURL = tk.Entry(page)
    inputURL.insert(0, 'C:/myFolder')
    inputURL.place(x=680, y=300)
    # 保存按钮
    btn = tk.Button(page, width=12, height=2, text='保存并导出结果', bg='pink', command=similarity)
    btn.place(x=660, y=220)
    page.mainloop()

def mtpage():
    page = tk.Toplevel()
    page.geometry('900x600')
    page.title('车辆连续跟踪与跨境识别系统')
    # 标题文字
    headText = tk.Label(page, text='跨镜头下的车辆重识别', bg='pink', width=30, height=2)
    headText.place(x=10, y=10)
    # 输入视频界面
    ig1 = tk.PhotoImage(file='p3.gif')
    inputVideo = tk.Label(page, image=ig1, width=400, height=300)
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

    # # 创建5个输出视频
    # filename = ['p4.gif', 'p5.gif']
    # for i in range(0, 5):
    #     if i < 2:
    #         ig = tk.PhotoImage(file=filename[i])
    #         outputVideo = tk.Label(page, image=ig, width=80, height=60)
    #         outputVideo.place(x=480, y=20 + i * 100)
    #     else:
    #         outputVideo = tk.Label(page, bg='yellow', width=10, height=4)
    #         outputVideo.place(x=480, y=20 + i * 100)

    # 插入两张图片
    ig2 = tk.PhotoImage(file='p4.gif')
    outputvideo1 = tk.Label(page, image=ig2, width=80, height=60)
    outputvideo1.place(x=480, y=20)

    ig3 = tk.PhotoImage(file='p5.gif')
    outputvideo2 = tk.Label(page, image=ig3, width=80, height=60)
    outputvideo2.place(x=480, y=100)

    # 插入三张背景
    for i in range(0, 3):
        outputVideo = tk.Label(page, bg='yellow', width=10, height=4)
        outputVideo.place(x=480, y=200 + i * 100)
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

def stpage():
    page = tk.Toplevel()
    page.geometry('900x600')
    page.title('车辆连续跟踪与跨境识别系统')
    # page.config(background='white')
    # 标题文字
    headText = tk.Label(page, text='单镜头下的车辆检测与连续跟踪', bg='pink', width=30, height=2, font=('仿宋', 15, 'bold'))
    headText.place(x=10, y=10)
    # 输入视频界面
    ig1 = tk.PhotoImage(file="p1.gif")
    inputVideo = tk.Label(page, image=ig1, width=400, height=300)
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
    ig2 = tk.PhotoImage(file="p2.gif")
    outputVideo = tk.Label(page, image=ig2, width=400, height=300)
    outputVideo.place(x=460, y=120)
    # 开始播放按钮
    play = tk.Button(page, text='按enter以开始', bg='pink', command=statistics1)
    play.place(x=630, y=450)
    page.mainloop()


page = tk.Tk()
page.geometry('900x540')
page.title('车辆连续跟踪与跨境识别系统')
# # 背景图片
bg = tk.PhotoImage(file='bg.gif')
canvas = tk.Canvas(page, width=900, height=540)
canvas.create_image(0, 0, anchor='nw', image=bg)
canvas.pack()
# page.config(background='white')
# 标题文字
# headText = tk.Label(page, text='单镜头下的车辆检测与连续跟踪', bg='pink', width=30, height=2, font=('仿宋', 15, 'bold'))
# headText.place(x=10, y=10)
# 两个按钮
btn1 = tk.Button(page, text='单镜头下的车辆检测与连续跟踪', font=('仿宋', 15, 'bold'), bg='pink', command=stpage)
btn1.place(x=100, y=150)
btn2 = tk.Button(page, text='跨镜头下的车辆重识别', font=('仿宋', 15, 'bold'), bg='pink', command=mtpage)
btn2.place(x=600, y=150)
page.mainloop()






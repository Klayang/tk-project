import tkinter as tk
page = tk.Tk()
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
# 按钮
btn = tk.Button(page, text='继续')
btn.place(x=900, y=500)
page.mainloop()

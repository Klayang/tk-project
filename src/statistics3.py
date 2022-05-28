import tkinter as tk
page = tk.Tk()
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
# 按钮
btn = tk.Button(page, text='继续')
btn.place(x=900, y=500)
page.mainloop()
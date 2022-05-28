import tkinter as tk
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

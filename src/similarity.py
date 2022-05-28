import tkinter as tk

from FormalProject.analysis import analysis


def similarity():
    page = tk.Toplevel()
    page.geometry('900x600')
    page.title('车辆连续跟踪与跨境识别系统')
    # page.config(background='white')
    # 标题文字
    headText = tk.Label(page, text='最终相似度', bg='pink', width=30, height=2)
    headText.place(x=10, y=10)
    # 文字
    text = tk.Label(page, text='相似度判别机制公开\n最终相似度=9*相似度1 + 8*相似度2 + 7*相似度3\n若最大相似度<60%，则认为匹配失败\n如需了解更多请联系我们')
    text.place(x=500, y=20)
    # Top5s
    topText = tk.Label(page, text='Top5s')
    topText.place(x=400, y=200)
    # 5张图片
    for i in range(0, 5):
        image = tk.Label(page, width=15, height=6, bg='grey')
        image.place(x=50 + 150 * i, y=300)
    # 结果分析按钮
    btn = tk.Button(page, text='按Enter进行结果分析', bg='pink', command=analysis)
    btn.place(x=650, y=460)
    page.mainloop()

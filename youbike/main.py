import datasource  # 呼叫datasource.py model
import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        topFrame = ttk.LabelFrame(self, text='台北市行政區')

        #要取區的值+索引，要先取長度
        length = len(datasource.sarea_list)
        self.radioStringVar = tk.StringVar()  # StringVar是負責取我點選的值
        for i in range(length):
            cols= i % 3 #3欄
            rows= i//3 #列
            ttk.Radiobutton(topFrame,text=datasource.sarea_list[i],value=datasource.sarea_list[i],variable=self.radioStringVar,command=self.radio_Event).grid(column=cols,row=rows,sticky=tk.W,padx=10,pady=10) #datasource.sarea_list[i]取索引編號；sticky=tk.W靠左對齊；value的值傳給variable

        topFrame.pack()
        self.radioStringVar.set('信義區')
        self.area_data = datasource.getInfoFromArea('信義區')  # self.area_data是list

        buttonFrame = ttk.LabelFrame(self, text='信義區')
        buttonFrame.pack()

        columns=('#1','#2','#3','#4','#5','#6','#7')
        tree = ttk.Treeview(buttonFrame, columns=columns,show='headings')
        tree.heading('#1',text='站點')
        tree.column('#1', minwidth=0, width=150)  # minwidth欄位最小寬度
        tree.heading('#2', text='時間')
        tree.column('#2', minwidth=0, width=150)
        tree.heading('#3', text='車數')
        tree.column('#3', minwidth=0, width=35)
        tree.heading('#4', text='可借')
        tree.column('#4', minwidth=0, width=35)
        tree.heading('#5', text='可還')
        tree.column('#5', minwidth=0, width=35)
        tree.heading('#6', text='地址')
        tree.column('#6', minwidth=0, width=200)
        tree.heading('#7', text='狀態')
        tree.column('#7', minwidth=0, width=15)
        tree.pack()

        for item in self.area_data:
            tree.insert('', tk.END, values=[item['sna'][11:],item['mday'], item['tot'], item['sbi'], item['bemp'], item['ar'], item['act']])
            



    def radio_Event(self):
        area_name=self.radioStringVar.get() #點選哪個從這裡取得
        self.area_data=datasource.getInfoFromArea(area_name)
        #print(area_data) #list
        for item in self.area_data:
            print(item)




def main():
    window = Window()
    window.title("台北市youbike2.0資訊")
    window.mainloop()


if __name__ == "__main__":
    main()


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

        
        self.radioStringVar.set('信義區') #上方radiobutton的預設值
        self.area_data = datasource.getInfoFromArea(self.radioStringVar.get())  # self.area_data是list ；下方grid內容預設哪一區

        self.bottomFrame = ttk.LabelFrame(self, text=self.radioStringVar.get()) #grid上方顯示的字
        self.bottomFrame.pack()

        columns=('#1','#2','#3','#4','#5','#6','#7')
        self.tree = ttk.Treeview(self.bottomFrame, columns=columns,show='headings')
        self.tree.heading('#1',text='站點')
        self.tree.column('#1', minwidth=0, width=130)  # minwidth欄位最小寬度
        self.tree.heading('#2', text='時間')
        self.tree.column('#2', minwidth=0, width=130)
        self.tree.heading('#3', text='車數')
        self.tree.column('#3', minwidth=0, width=35)
        self.tree.heading('#4', text='可借')
        self.tree.column('#4', minwidth=0, width=35)
        self.tree.heading('#5', text='可還')
        self.tree.column('#5', minwidth=0, width=35)
        self.tree.heading('#6', text='地址')
        self.tree.column('#6', minwidth=0, width=150)
        self.tree.heading('#7', text='狀態')
        self.tree.column('#7', minwidth=0, width=35)
        self.tree.pack(side=tk.LEFT) #把scrollbar加在treeview右邊

        for item in self.area_data:
            self.tree.insert('', tk.END, values=[item['sna'][11:],item['mday'], item['tot'], item['sbi'], item['bemp'], item['ar'], item['act']])
            
        #新增scrollbar
        scrollbar = ttk.Scrollbar(self.bottomFrame,command=self.tree.yview) 
        scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

    #建立事件Event: 依所選行政區顯示站點資訊
    def radio_Event(self):
        #area_name=self.radioStringVar.get() #點選哪個從這裡取得
        #self.area_data=datasource.getInfoFromArea(area_name)

        # 清空treeview資料
        #tree.delete(*tree.get_children())
        for child in self.tree.get_children():
            self.tree.delete(child)

        # 取得點選行政區值
        self.area_data = datasource.getInfoFromArea(self.radioStringVar.get())
        self.bottomFrame.config(text=self.radioStringVar.get())

        # 更新treeview資料
        for item in self.area_data:
            self.tree.insert('',tk.END,values=[item['sna'][11:],item['mday'],item['tot'],item['sbi'],item['bemp'],item['ar'],item['act']])

        
        #print(self.area_data) #list
        # for item in self.area_data:
        #     print(item) #dict




def main():
    window = Window()
    window.title("台北市youbike2.0資訊")
    window.mainloop()


if __name__ == "__main__":
    main()


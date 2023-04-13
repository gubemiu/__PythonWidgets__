import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog  # Dialog是單一視窗跳出後就不能點其他筆資料開另一視窗，必須先關掉
import tkintermapview as tkmap  # 要安裝tkintermapview=> pip install tkintermapview




class MapDisplay(Dialog):  # 繼承Dialog，tk.Toplevel是開啟一個視窗還沒關又可以點另一個開新的視窗
    def __init__(self, master, data_dict, **kwargs):
        self.site_info = data_dict
        print(self.site_info)
        super().__init__(master, **kwargs)  # 呼叫，self可以不用寫
        
    
    #Dialog-override
    def body(self, master):  # 內容要寫在body裡
        map_widget = tkmap.TkinterMapView(self,width=800,height=600,corner_radius=0)
        map_widget.pack()
        marker_1 = map_widget.set_position(self.site_info['lat'],self.site_info['lng'],marker=True) #台北市位置
        map_widget.set_zoom(20) #設定顯示大小
        marker_1.set_text(self.site_info['sna'][11:])
        
        # # 新增站點搜尋欄位
        # search_frame = tk.Frame(master)
        # search_label = tk.Label(search_frame, text="站點搜尋：")
        # search_label.pack(side=tk.LEFT, padx=5, pady=5)
        # self.search_entry = tk.Entry(search_frame, width=30)
        # self.search_entry.pack(side=tk.LEFT, padx=5, pady=5)
        # search_frame.pack()
        


    # Dialog-override
    def buttonbox(self) -> None:
        '''add standard button box.
        override if you do not want the standard buttons
        '''
        boxFrame=tk.Frame(self)
        button=tk.Button(boxFrame,text='關閉',width=10,command=self.ok,default=tk.ACTIVE) #self.ok方法是繼承來的
        button.pack(side=tk.LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        boxFrame.pack()

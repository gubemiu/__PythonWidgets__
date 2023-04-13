import datasource  # 呼叫datasource.py model
import tkinter as tk
from tkinter import ttk
import datetime
from tkinter.simpledialog import askinteger, askstring
from PIL import Image,ImageTk
from messageWindow import MapDisplay



# 新增全域的變數
sbi_numbers = 3
bemp_numbers = 3


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

# add menubar => 建立一個 Menubar
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)
    # add command menu in menubar => 在Menubar建立一個 command menu
        self.command_menu = tk.Menu(self.menubar)
        self.command_menu2 = tk.Menu(self.menubar)

    # 在command menu裡面放一個實體list，destroy=>把window關掉
        self.command_menu.add_command(label='設定', command=self.menu_setting_click)
        self.command_menu.add_command(label='離開', command=self.destroy)
        self.menubar.add_cascade(label='File', menu=self.command_menu)
    
    
        self.command_menu2.add_command(label='搜尋', command=self.menu_search_click)
        self.menubar.add_cascade(label='serch', menu=self.command_menu2)

    # mainFrame包在最外面self(top_wrapperFrame、self.bottomFrame放裡面)
        mainFrame=ttk.Frame(self)
        mainFrame.pack(padx=30,pady=50)
    
    #logoLabel top of top_wrapperFrame
        logoImage=Image.open('logo.png')
        resizeImage=logoImage.resize((270,68),Image.LANCZOS)
        self.logoTkimage=ImageTk.PhotoImage(resizeImage)
        logoLabel=ttk.Label(mainFrame,image=self.logoTkimage)
        logoLabel.pack(pady=(0,20))


# 建立一個top_wrapperFrame(包在topFrame外的包裝紙)==============
        top_wrapperFrame = ttk.Frame(mainFrame)
        top_wrapperFrame.pack(fill=tk.X)

# topFrame start =========================================
        topFrame = ttk.LabelFrame(top_wrapperFrame, text='台北市行政區')

        # 要取區的值+索引，要先取長度
        length = len(datasource.sarea_list)
        self.radioStringVar = tk.StringVar()  # StringVar是負責取我點選的值
        for i in range(length):
            cols = i % 3  # 3欄
            rows = i//3  # 列
            ttk.Radiobutton(topFrame, text=datasource.sarea_list[i], value=datasource.sarea_list[i], variable=self.radioStringVar, command=self.radio_Event).grid(
                column=cols, row=rows, sticky=tk.W, padx=10, pady=10)  # datasource.sarea_list[i]取索引編號；sticky=tk.W靠左對齊；value的值傳給variable
        topFrame.pack(side=tk.LEFT)
        # value=datasource.sarea_list[i]裡面是全部資料

        self.radioStringVar.set('信義區')  # 上方radiobutton的預設值
        self.area_data = datasource.getInfoFromArea(
            self.radioStringVar.get())  # self.area_data是list ；下方grid內容預設哪一區
# topFrame end =========================================

# sbi_warningFrame_start=====================================
        self.sbi_warningFrame = ttk.LabelFrame(top_wrapperFrame)
        columns = ('#1', '#2', '#3')
        self.sbi_tree = ttk.Treeview(
            self.sbi_warningFrame, columns=columns, show='headings')
        self.sbi_tree.heading('#1', text='站點')
        self.sbi_tree.column('#1', minwidth=0, width=100)
        self.sbi_tree.heading('#2', text='可借')
        self.sbi_tree.column('#2', minwidth=0, width=35)
        self.sbi_tree.heading('#3', text='可還')
        self.sbi_tree.column('#3', minwidth=0, width=35)
        self.sbi_tree.pack(side=tk.LEFT)  # side=tk.LEFT這個沒寫好像沒差
        self.sbi_warning_data = datasource.filter_sbi_warning_data(
            self.area_data, sbi_numbers)
        sbi_site_numbers = len(self.sbi_warning_data)
        self.sbi_warningFrame.configure(text=f'可借不足站點數:{sbi_site_numbers}')
        for item in self.sbi_warning_data:
            self.sbi_tree.insert('', tk.END, values=[item['sna'][11:], item['sbi'], item['bemp']])
        self.sbi_warningFrame.pack(side=tk.LEFT)
# sbi_warningFrame_end=====================================

# bemp_warningFrame_start=====================================
        self.bemp_warningFrame = ttk.LabelFrame(top_wrapperFrame)
        columns = ('#1', '#2', '#3')
        self.bemp_tree = ttk.Treeview(
            self.bemp_warningFrame, columns=columns, show='headings')
        self.bemp_tree.heading('#1', text='站點')
        self.bemp_tree.column('#1', minwidth=0, width=100)
        self.bemp_tree.heading('#2', text='可借')
        self.bemp_tree.column('#2', minwidth=0, width=35)
        self.bemp_tree.heading('#3', text='可還')
        self.bemp_tree.column('#3', minwidth=0, width=35)
        self.bemp_tree.pack(side=tk.LEFT)  # side=tk.LEFT這個沒寫好像沒差
        self.bemp_warning_data = datasource.filter_bemp_warning_data(
            self.area_data, bemp_numbers)
        bemp_site_numbers = len(self.bemp_warning_data)
        self.bemp_warningFrame.configure(text=f'可還不足站點數:{bemp_site_numbers}')

        for item in self.bemp_warning_data:
            self.bemp_tree.insert('', tk.END, values=[item['sna'][11:], item['sbi'], item['bemp']])
        self.bemp_warningFrame.pack(side=tk.LEFT)
# bemp_warningFrame_end=====================================

# bottomFrame
        now = datetime.datetime.now()
        nowString = now.strftime("%Y-%m-%d %H:%M:%S")
        self.bottomFrame = ttk.LabelFrame(mainFrame, text=f"{self.radioStringVar.get()}-{nowString}")  # grid上方顯示的字
        # self.bottomFrame = ttk.LabelFrame(self, text=self.radioStringVar.get()) #grid上方顯示的字
        self.bottomFrame.pack()

        columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7')
        self.tree = ttk.Treeview(
            self.bottomFrame, columns=columns, show='headings')
        self.tree.heading('#1', text='站點')
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
        self.tree.pack(side=tk.LEFT)  # 把scrollbar加在treeview右邊

        #self.tree,addItem
        for item in self.area_data:
            self.tree.insert('', tk.END, values=[item['sna'][11:], item['mday'], item['tot'],item['sbi'], item['bemp'], item['ar'], item['act']], tags=item['sna'])


        # self.tree.bind event (<<TreeviewSelect>>,後面要加事件)=>用在Treeview，要點選的時候用<<TreeviewSelect>>
            self.tree.bind('<<TreeviewSelect>>', self.treeSelected)



        # 幫 treeview 新增scrollbar
        scrollbar = ttk.Scrollbar(self.bottomFrame, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)
        '''
        還有另外兩種寫法
        self.tree.config(yscrollcommand=scrollbar.set)
        self.tree['yscrollcommand']=scrollbar.set
        '''

        bemp_scrollbar = ttk.Scrollbar(self.bemp_warningFrame, command=self.bemp_tree.yview)
        bemp_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.bemp_tree.config(yscrollcommand=bemp_scrollbar.set)

        sbi_scrollbar = ttk.Scrollbar(
            self.sbi_warningFrame, command=self.sbi_tree.yview)
        sbi_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.sbi_tree.config(yscrollcommand=sbi_scrollbar.set)

    '''
    # 排序??============================================================
            # self.tree.bind('<ButtonRelese-1>',self.sortby)
    # 排序??============================================================
    '''


    # def treeSelected 點list其中一筆時傳回值
    def treeSelected(self, event):
        selectedTree=event.widget
        #print(selectedTree.selection()) #傳回tupple->像這樣('I004',)
        if len(selectedTree.selection())==0: return #如果抓到空值直接return不做

        itemTag = selectedTree.selection()[0]  # itemTag是字串I004
        #print(selectedTree.item(itemTag))  # 傳回dictionary，是item(I004)裡面的資訊
        itemDic=selectedTree.item(itemTag) 
        #print(itemDic['tags'][0]) #傳回list
        siteName = itemDic['tags'][0]  # siteName就是list

        for item in datasource.data_list:  # datasource.data_list(可查全區) /self.area_data(只能查一區)
            if siteName == item['sna']:
                selected_data = item
                break
        
        #顯示地圖Window
        mapDisplay = MapDisplay(self, selected_data)  # self是display.py裡面class MapDisplay的master，selected_data是data_dict
        




    # 點擊 menubar 裡面的選項時

    #設定
    def menu_setting_click(self):
        global sbi_numbers, bemp_numbers  # 呼叫最前面的sbi_numbers，bemp_numbers
        retVal = askinteger(f'目前設定不足數量:{sbi_numbers}', '請輸入不足可借可還數量0~5', minvalue=0, maxvalue=5) #會檢核=>minvalue=0, maxvalue=5
        print(retVal)
        sbi_numbers = retVal  # 把input值變更到sbi_numbers，bemp_numbers
        bemp_numbers = retVal

    
    #搜尋
    def menu_search_click(self):
        siteStr = askstring('查詢站點', '請輸入要查詢的站點')
        #print(siteStr)
        #先清掉
        for item in self.tree.get_children():
            self.tree.delete(item)
        #再新增
        for item in datasource.data_list:  # datasource.data_list(可查全區，可是地圖出不來) /self.area_data(只能查一區，但地圖可出來)
            if siteStr in item['sna'] or siteStr in (item['ar']):
                self.tree.insert('',tk.END,values=[item['sna'][11:], item['mday'], item['tot'], item['sbi'], item['bemp'], item['ar'], item['act']],tags=item['sna'])



    # 建立事件Event: 依所選行政區顯示站點資訊
    def radio_Event(self):
        # 點擊時間
        now = datetime.datetime.now()
        nowString = now.strftime("%Y-%m-%d %H:%M:%S")

        # 清空treeview資料
        # tree.delete(*tree.get_children())
        for child in self.tree.get_children():
            self.tree.delete(child)

        for child in self.sbi_tree.get_children():
            self.sbi_tree.delete(child)

        for child in self.bemp_tree.get_children():
            self.bemp_tree.delete(child)

        # 取得點選行政區值
        # print(type(self.tree.get_children()))
        area_name = self.radioStringVar.get()  # 點選哪個從這裡取得
        # print(area_name) #可以用這樣驗證取出哪個區(debug可以不寫)
        self.area_data = datasource.getInfoFromArea(area_name)
        # self.area_data=datasource.getInfoFromArea(self.radioStringVar.get()) #如果這樣寫，就可以不用寫area_name=self.radioStringVar.get()
        self.bottomFrame.config(
            text=f'{self.radioStringVar.get()}-{nowString}')  # grid上方的字
        # self.bottomFrame.config(text=f"{area_name}-{nowString}")也可以這樣寫

        # 取得警示區符合條件的資料
        self.sbi_warning_data = datasource.filter_sbi_warning_data(
            self.area_data, sbi_numbers)
        sbi_site_numbers = len(self.sbi_warning_data)
        self.sbi_warningFrame.config(text=f'可借不足站點數:{sbi_site_numbers}')

        self.bemp_warning_data = datasource.filter_bemp_warning_data(
            self.area_data, bemp_numbers)
        bemp_site_numbers = len(self.bemp_warning_data)
        self.bemp_warningFrame.config(text=f'可還不足站點數:{bemp_site_numbers}')

        # 更新treeview資料
        for item in self.area_data:
            self.tree.insert('', tk.END, values=[item['sna'][11:], item['mday'], item['tot'], item['sbi'], item['bemp'], item['ar'], item['act']],tags=item['sna'])


        for item in self.sbi_warning_data:
            self.sbi_tree.insert('', tk.END, values=[item['sna'][11:], item['sbi'], item['bemp']])


        for item in self.bemp_warning_data:
            self.bemp_tree.insert('', tk.END, values=[item['sna'][11:], item['sbi'], item['bemp']])

        # print(self.area_data) #list
        # for item in self.area_data:
        #     print(item) #dict


def main():
    window = Window()
    window.title("台北市youbike2.0資訊")
    window.mainloop()


if __name__ == "__main__":
    main()

import tkinter as tk
#from tkinter import ttk
from parts import TopFrame,MedianFrame,BottomFrame   # 可以這樣寫from parts import * (但這樣寫比較不好，容易造成命名衝突)


class Window(tk.Tk): #class裡面的self代表的都是我自己的實體，所有東西都放在Window裡面
    def __init__(self):
        super().__init__()  # super代表父類別
        topFrame = TopFrame(self, borderwidth=0)  # TopFrame子類別繼承LabelFrame父類別，用topFrame實體子容器去接，裡面有一個borderwidth，所以這裡可以用
        #print(topFrame.flowerPhoto1)
        topFrame.pack()  # topFrame裡面有attribute、property、method
        medianFrame=MedianFrame(self,borderwidth=0)
        medianFrame.pack(fill=tk.X)  # 讓radioButton的畫布靠左對齊
        bottomFrame = BottomFrame(self)  # 這裡的self是Window(CLASS)，老師習慣實體(遙控器)用小寫，大寫的是calss
        bottomFrame.pack(fill=tk.X)
    
    # 建了這個window的實體method，使用者按了按鈕windows才會知道
    def radioButtonEvenOfMedianFrame(self, radioButtonValue):
        print(radioButtonValue) 

    def listBoxEventOfBottomFrame(self, listBoxValue):  # listBoxValue(自己命名)去接parts.py的selectedValue
        print(listBoxValue)

    def comboBoxEventOfBottomFrame(self, comboValue):
        print(comboValue)



#實體在main裡面(主程式)
def main():
    window=Window()
    window.title('widgets')
    window.mainloop() #要讓主程式一直執行


if __name__=='__main__':
    main()
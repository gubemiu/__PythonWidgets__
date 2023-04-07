import requests

sarea_list=None #先給空的，下面執行會取值
data_list = None


def getInfo():
    global sarea_list  # 要在getInfo function裡面用外面的sarea_list，要加這行，否則裡面的sarea_list執行完就消滅了
    global data_list
    url='https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response=requests.get(url)
    data_list=response.json()  #property，print(type(response.json()))看他的資料結構顯示是list
    

    # 要知道jason的資料格式可以到這個網站把jason檔內容貼上：https://jsonviewer.stack.hu/
    # 取data_list裡面的很多dictionary    
    sarea_temp = set()  # 因為item['sarea']取出來有很多重複區，所以要用set()取distinct值，但set沒有索引編號，所以下面要轉成list
    for item in data_list:  # data_list抓出來的dictionary是給item
        sarea_temp.add(item['sarea'])
    sarea_list = sorted(list(sarea_temp))   #把set取出來的值轉成list，因為每次取的值排序都不同，所以用sorted排序

#取得點選區域的所有資料
def getInfoFromArea(areaName):
    filter_data= filter(lambda n:n['sarea']==areaName, data_list)  # filter是built-in function，裡面要放function=>lambda n:n['sarea']==areaName
    return list(filter_data)


getInfo()


# 區 sarea
# 站點 sna

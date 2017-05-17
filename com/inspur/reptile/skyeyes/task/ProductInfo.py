# 产品信息
# http://www.tianyancha.com/expanse/appbkinfo.json?id=6923813&ps=5&pn=1
from com.inspur.reptile.skyeyes.task.Info import Info
contentUrl= "expanse/appbkinfo.json?id="

class ProductInfo(Info):
    def __init__(self,comId):
        url=super().getBaseUrl()+contentUrl+comId+"&pn=1&ps=1000"#ps=1000 mean of pagezie,eg.how many item per page.
        super().__init__(url)

if __name__ == '__main__':
    ProductInfo("6923813").crawl()
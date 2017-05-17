#股东信息
#http://www.tianyancha.com/expanse/holder.json?id=2315740&ps=20&pn=1

from com.inspur.reptile.skyeyes.task.Info import Info

contentUrl= "expanse/holder.json?id="

class Holder(Info):
    def __init__(self,comId):
        url=super().getBaseUrl()+contentUrl+comId+"&pn=1&ps=1000"#ps=1000 mean of pagezie,eg.how many item per page.
        super().__init__(url)

if __name__ == '__main__':
    Holder("2344338651").crawl()
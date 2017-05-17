#专利
#http://www.tianyancha.com/expanse/patent.json?id=2344338651&pn=1&ps=1000
from com.inspur.reptile.skyeyes.task.Info import Info


contentUrl= "expanse/patent.json?id="

class PatentInfo(Info):
    def __init__(self,comId):
        url=super().getBaseUrl()+contentUrl+comId+"&pn=1&ps=1000"#ps=1000 mean of pagezie,eg.how many item per page.
        super().__init__(url)

if __name__ == '__main__':
    PatentInfo("2344338651").crawl()
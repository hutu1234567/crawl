#税务
# http://www.tianyancha.com/expanse/taxcredit.json?id=2344338651&ps=5&pn=1

from com.inspur.reptile.skyeyes.task.Info import Info

class TaxRatingInfo(Info):
    def __init__(self,comId):
        super().__init__("%sexpanse/taxcredit.json?id=%s&ps=1000&pn=1"%(super().getBaseUrl(),comId))
if __name__ == '__main__':
    TaxRatingInfo("2344338651").crawl()
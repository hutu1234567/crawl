#税务
# http://www.tianyancha.com/expanse/taxcredit.json?id=2344338651&ps=5&pn=1

from com.inspur.reptile.skyeyes.task.Info import Info
from com.inspur.reptile.skyeyes.domain.TaxRatingEntity import TaxRatingEntity

ps = 1000
class TaxRatingInfo(Info):
    def __init__(self,comId,pn=1):
        self.comid=comId
        self.pn=pn
        super().__init__("%sexpanse/taxcredit.json?id=%s&ps=1000&pn=1"%(super().getBaseUrl(),comId))
    def run(self):
        ret=self.crawl()
        for data in ret["data"]["items"]:
            data["comid"]=self.comid
            TaxRatingEntity(data,self.taskid)
        if (int( ret["data"]["count"] ) > self.pn * ps):
            TaxRatingInfo(self.comid, self.pn+1 )
if __name__ == '__main__':
    comid="2344338651"
    TaxRatingInfo(comid)
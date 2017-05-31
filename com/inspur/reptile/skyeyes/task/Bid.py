# 招投标
# http://www.tianyancha.com/expanse/bid.json?id=6923813&pn=1&ps=10
from com.inspur.reptile.skyeyes.task.Info import Info
from com.inspur.reptile.skyeyes.domain.BidEntity import BidEntity

contentUrl= "expanse/bid.json?id="
ps = 1000
class Bid(Info):
    def __init__(self, comId, pn=1):
        #url=super().getBaseUrl()+contentUrl+comId+"&pn=1&ps=100"#ps=1000 mean of pagezie,eg.how many item per page.
        self.comid=comId
        self.pn=pn
        url="%s%s%s&pn=%s&ps=%s"%(super().getBaseUrl(), contentUrl, comId, pn, ps)
        super().__init__(url)
    def run(self):
        ret = self.crawl()
        for data in (ret["data"]["items"]):
            data["comid"] = self.comid
            BidEntity( data ,self.taskid)
        if (int( ret["data"]["viewtotal"] ) > self.pn * ps):
            newpn=self.pn + 1
            newbid=Bid(self.comid,newpn)
if __name__ == '__main__':
    comid = "14990231"
    Bid(comid)

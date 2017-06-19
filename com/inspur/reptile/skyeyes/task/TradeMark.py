#商标
# http://www.tianyancha.com/tm/getTmList.json?id=2315740&pageNum=1&ps=1000
from com.inspur.reptile.skyeyes.task.Info import Info
from com.inspur.reptile.skyeyes.domain.TradeMarkEntity import TradeMarkEntity
#urlDemo="http://www.tianyancha.com/v2/IcpList/2344338651.json"
#baseUrl="http://www.tianyancha.com/v2/IcpList/"
contentUrl= "tm/getTmList.json?id="
ps = 1000

class TradeMark(Info):
    def __init__(self,comId,pn=1):
        #url= super().getBaseUrl() + contentUrl + comId + "&pageNum=1&ps=1000"
        self.comid=comId
        self.pn=pn
        url="%s%s%s&pageNum=%s&ps=%s"%(super().getBaseUrl(), contentUrl, comId, pn, ps)
        super().__init__(url)
    # def icrawl(self):
    #     ret = request(self.url)
    #     print(ret)
    def run(self):
        ret=self.crawl()
        for data in ret["data"]["items"]:
            data["comid"]=self.comid
            TradeMarkEntity(data)
        if (int( ret["data"]["viewtotal"] ) >self. pn * ps):
            TradeMark(self.comid,self.pn+1)
if __name__ == '__main__':
    comid="2344338651"
    TradeMark(comid)
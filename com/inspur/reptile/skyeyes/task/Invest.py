#对外投资
#http://www.tianyancha.com/expanse/inverst.json?id=2315740&ps=20&pn=1
from com.inspur.reptile.skyeyes.task.Info import Info
from com.inspur.reptile.skyeyes.domain.InvestEntity import InvestEntity
#urlDemo="http://www.tianyancha.com/v2/IcpList/2344338651.json"
#baseUrl="http://www.tianyancha.com/v2/IcpList/"
contentUrl= "expanse/inverst.json?id="
ps = 1000
class Invest(Info):
    def __init__(self,comId,pn=1):
        # url= super().getBaseUrl() + contentUrl + comId + "&ps=1000&pn=1"
        self.comid=comId
        self.pn=pn
        url="%s%s%s&pn=%s&ps=%s"%(super().getBaseUrl(), contentUrl, comId, pn, ps)
        super().__init__(url)
    def run(self):
        ret = self.crawl()
        for data in (ret["data"]["result"]):
            data["comid"]=self.comid
            InvestEntity( data,self.taskid )
        if (int( ret["data"]["total"] ) > self.pn * ps):
            Invest( self.comid,self.pn+1 )

if __name__ == '__main__':
    comid="2344338651"
    Invest( comid)
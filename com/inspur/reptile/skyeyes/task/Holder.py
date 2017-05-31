#股东信息
#http://www.tianyancha.com/expanse/holder.json?id=2315740&ps=20&pn=1

from com.inspur.reptile.skyeyes.task.Info import Info
from com.inspur.reptile.skyeyes.domain.HolderEntity import HolderEntity
contentUrl= "expanse/holder.json?id="
ps = 1000


class Holder(Info):
    def __init__(self,comId,pn=1):
        #url=super().getBaseUrl()+contentUrl+comId+"&pn=1&ps=1000"#ps=1000 mean of pagezie,eg.how many item per page.
        self.comid=comId
        self.pn=pn
        url="%s%s%s&pn=%s&ps=%s"%(super().getBaseUrl(), contentUrl, comId, pn, ps)
        super().__init__(url)
    def run(self):
        ret =self .crawl()
        for data in (ret["data"]["result"]):
            data["comid"] =self.comid
            HolderEntity( data )
        if (int( ret["data"]["total"] ) > self.pn * ps):
            Holder(self.comid ,self.pn+1)

if __name__ == '__main__':
    comid="2344338651"
    Holder( comid)
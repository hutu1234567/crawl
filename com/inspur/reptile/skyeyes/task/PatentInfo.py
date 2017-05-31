#专利
#http://www.tianyancha.com/expanse/patent.json?id=2344338651&pn=1&ps=1000
from com.inspur.reptile.skyeyes.task.Info import Info
from com.inspur.reptile.skyeyes.domain.PatentInfoEntity import PatentInfoEntity

contentUrl= "expanse/patent.json?id="
ps = 1000

class PatentInfo(Info):
    def __init__(self,comId,pn=1):
        #url=super().getBaseUrl()+contentUrl+comId+"&pn=1&ps=1000"#ps=1000 mean of pagezie,eg.how many item per page.
        self.comid=comId
        self.pn=pn
        url="%s%s%s&pn=%s&ps=%s"%(super().getBaseUrl(), contentUrl, comId, pn, ps)
        super().__init__(url)

    def run(self):
        ret=self.crawl()
        for data in (ret["data"]["items"]):
            data["comid"]=self.comid
            PatentInfoEntity(data,self.taskid)
        if (int( ret["data"]["viewtotal"] ) > self.pn * ps):
            PatentInfo(self.comid,self.pn+1)
if __name__ == '__main__':
    comid="14776042"
    PatentInfo(comid)
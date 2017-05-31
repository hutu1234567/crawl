#主要人员
#http://www.tianyancha.com/expanse/staff.json?id=2315740&ps=20&pn=1
from com.inspur.reptile.skyeyes.task.Info import Info
from com.inspur.reptile.skyeyes.domain.StaffEntity import StaffEntity
contentUrl= "expanse/staff.json?id="
ps = 1000
class Staff(Info):
    def __init__(self,comId, pn=1):
        #url=super().getBaseUrl()+contentUrl+comId+"&pn=%&ps=%"#ps=1000 mean of pagezie,eg.how many item per page.
        self.pn=pn
        self.comid=comId
        url="%s%s%s&pn=%s&ps=%s"%(super().getBaseUrl(), contentUrl, comId, pn, ps)
        super().__init__(url)
    def run(self):
        ret=self.crawl()
        for data in ret["data"]["result"]:
            data["comid"]=self.comid
            StaffEntity(data,self.taskid)
        if (int( ret["data"]["total"] ) > self.pn * ps):
            Staff(self.comid,self.pn+1)
if __name__ == '__main__':
    comid="2344338651"
    Staff(comid)
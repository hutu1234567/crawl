#法律案件，诉讼
#http://www.tianyancha.com/v2/getlawsuit/%E6%B5%AA%E6%BD%AE%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8.json?page=1&ps=10
import urllib

from com.inspur.reptile.skyeyes.task.Info import Info
from com.inspur.reptile.skyeyes.domain.LawCaseEntity import LawCaseEntity

ps = 1000
class LawCase(Info):
    def __init__(self,comid,comName,pn=1 ):
        comName = urllib.parse.quote( comName )
        self.comName=comName
        self.comid=comid
        self.pn=pn
        url = "%sv2/getlawsuit/%s.json?page=%s&ps=%s"%(super().getBaseUrl(),comName,pn,ps )
        super().__init__(url)
    def run(self):
        ret=self.crawl()
        for data in (ret["data"]["items"]):
            data["comid"]=self.comid
            LawCaseEntity(data,self.taskid)
        if (int( ret["data"]["total"] ) > self.pn * ps):
            LawCase(self.comName,self.pn+1)
if __name__ == '__main__':
    comid="1261378417"
    comName="济南明鑫制药股份有限公司"
    LawCase(comid,comName)

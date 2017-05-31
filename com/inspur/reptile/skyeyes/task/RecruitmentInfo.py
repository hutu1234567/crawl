#招聘
#http://www.tianyancha.com/extend/getEmploymentList.json?companyName=山东伊莱特重工股份有限公司8&pn=1&ps=10
import urllib

from com.inspur.reptile.skyeyes.task.Info import Info
from com.inspur.reptile.skyeyes.domain.RecuitmentEntity import RecuitmentEntity

ps = 1000

class RecuitmentInfo(Info):
    def __init__(self,comid,comName,pn=1):
        # print("aaaaaa"*8,comName)
        self.comid=comid
        self.comName=comName
        self.pn=pn
        comNameEncode = urllib.parse.quote( comName)
        super().__init__(url="%s/extend/getEmploymentList.json?companyName=%s&pn=%s&ps=%s"%(super().getBaseUrl(),comNameEncode,pn,ps))
    def run(self):
        ret=self.crawl()
        for data in ret["data"]["companyEmploymentList"]:
            data["comid"]=self.comid
            print("print"*8, data["comid"])
            RecuitmentEntity(data,self.taskid)
        if (int( ret["data"]["totalRows"] ) > self.pn * ps):
            RecuitmentInfo(self.comid,self.comName,self.pn+1)
if __name__ == '__main__':
    comName="山东伊莱特重工股份有限公司"
    comid="2344338651"
    RecuitmentInfo(comid,comName)
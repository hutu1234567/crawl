# 网站备案
# http://www.tianyancha.com/v2/IcpList/6923813.json
from com.inspur.reptile.skyeyes.task.Info import Info
from com.inspur.reptile.skyeyes.domain.SiteRecordEntity import SiteRecordEntity
contentUrl= "v2/IcpList/"

class SitRecord(Info):
    def __init__(self,comId):
        self.comid=comId
        url=super().getBaseUrl()+contentUrl+comId+".json"#ps=1000 mean of pagezie,eg.how many item per page.
        super().__init__(url)
    def run(self):
        ret=self.crawl()
        for data in ret["data"]:
            data["comid"]=self.comid
            SiteRecordEntity(data,self.taskid)
if __name__ == '__main__':
    SitRecord("6923813")
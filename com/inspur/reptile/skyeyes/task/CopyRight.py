# 著作权
from com.inspur.reptile.skyeyes.task.Info import Info
from com.inspur.reptile.skyeyes.domain.CopyRightEntity import CopyRightEntity
#http://www.tianyancha.com/expanse/copyReg.json?id=2315740&pn=1&ps=5
#baseUrl="http://www.tianyancha.com/v2/IcpList/"
contentUrl= "expanse/copyReg.json?id="
ps = 1000

class CopyRight(Info):
    def __init__(self, comId, pn=1):
        url="%s%s%s&pn=%s&ps=%s"%(super().getBaseUrl(), contentUrl, comId, pn, ps)
        self.comid=comId
        self.pn=pn
        super().__init__(url)
    # def icrawl(self):
    #     ret = request(self.url)
    #     print(ret)

    def run(self):
        ret = self.crawl()
        # 此处需要实现总数超过本页数量的时候
        for data in (ret["data"]["items"]):
            data["comid"] = self.comid
            CopyRightEntity(data,self.taskid)
        if(int(ret["data"]["viewtotal"])>self.pn*ps):
            CopyRight( self.comid, self.pn+1 )
if __name__ == '__main__':
    comid = "6923813"
    CopyRight(comid)
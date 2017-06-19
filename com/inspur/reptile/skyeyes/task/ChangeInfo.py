#变更记录
#http://www.tianyancha.com/expanse/changeinfo.json?id=2315740&ps=5&pn=1
from com.inspur.reptile.skyeyes.task.Info import Info
from com.inspur.reptile.skyeyes.domain.ChangeInfoEntity import ChangeInfoEntity
#urlDemo="http://www.tianyancha.com/v2/IcpList/2344338651.json"
#baseUrl="http://www.tianyancha.com/v2/IcpList/"
contentUrl= "expanse/changeinfo.json?id="
ps = 1000

class ChangeInfo(Info):
    def __init__(self, comId, pn=1):
        #url= super().getBaseUrl() + contentUrl + comId + "&ps=1000&pn=1"
        self.comid=comId
        self.pn=pn
        url="%s%s%s&pn=%s&ps=%s"%(super().getBaseUrl(), contentUrl, comId, pn, ps)
        super().__init__(url)
    # def icrawl(self):
    #     ret = request(self.url)
    #     print(ret)
    def run(self):
        ret =self.crawl()
        for data in (ret["data"]["result"]):
            data["comid"] = self.comid
            ChangeInfoEntity( data, self.taskid )
        if (int( ret["data"]["total"] ) > self.pn * ps):
            #pn += 1
            ChangeInfo( self.comid, self.pn+1 )
if __name__ == '__main__':
    comid="554491155"
    ChangeInfo(comid)
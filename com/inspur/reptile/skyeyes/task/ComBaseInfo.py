#公司基本信息
#http://www.tianyancha.com/v2/company/2315740.json
from com.inspur.reptile.skyeyes.common.Token import getToken
from com.inspur.reptile.skyeyes.domain.ComBaseInfoEntity import ComBaseInfoEntity
from com.inspur.reptile.skyeyes.task.Info import Info
#baseUrl="http://www.tianyancha.com/v2/IcpList/"
contentUrl= "v2/company/"
class ComBaseInfo(Info):
    def __init__(self,comId):
        url= super().getBaseUrl() + contentUrl + comId + ".json"
        super().__init__(url)
    # def crawl(self):
    #     ret = request(self.url)
    #     print(ret)

    def run(self):

        #print( Info.getBaseUrl( comBase ) )
        session, headers = getToken( Info.getBaseUrl( self ) )
        ret = self.crawl( session=session, headers=headers )
        self.comName=ret["data"]["name"]
        #print( ret )
        comBaseEntity = ComBaseInfoEntity( ret["data"] ,self.taskid)
        #comBaseEntity.save()
        print(ret["data"])
if __name__ == '__main__':
    #for i in range (1,100):
    comBase = ComBaseInfo(  "441475765" )

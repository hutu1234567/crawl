#{"state":"ok","message":"","totalPage":1,"humanCount":0,"companyCount":1,"total":1,"data":[
# {"id":612873785,"name":"<em>章丘东汉铁艺有限公司</em>","type":1,"matchType":null

from com.inspur.reptile.skyeyes.common.Token import getToken
from com.inspur.reptile.skyeyes.domain.ComBaseInfoEntity import ComBaseInfoEntity
from com.inspur.reptile.skyeyes.task.Info import Info
import urllib
#baseUrl="http://www.tianyancha.com/v2/IcpList/"
#http://www.tianyancha.com/v2/search/%E7%AB%A0%E4%B8%98%E4%B8%9C%E6%B1%89%E9%93%81%E8%89%BA%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8.json?
contentUrl= "v2/search/"
class HumanSearch(Info):
    def __init__(self,comName):
        comNameDecode = urllib.parse.quote( comName )
        self.comName=comName
        url= super().getBaseUrl() + contentUrl + comNameDecode + ".json"
        super().__init__(url)
    # def crawl(self):
    #     ret = request(self.url)
    #     print(ret)

    def run(self):

        #print( Info.getBaseUrl( comBase ) )
        session, headers = getToken( Info.getBaseUrl( self ) )
        ret = self.crawl( session=session, headers=headers )
        if(ret["total"]==0):
            self.data = None
            raise Exception(self.comName+":未查询到数据")
        else:
            self.data=ret["data"]
if __name__ == '__main__':
    #for i in range (1,100):
    comBase = HumanSearch(  "中国重汽集团济南商用车有限公司" )

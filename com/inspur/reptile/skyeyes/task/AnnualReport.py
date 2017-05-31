#企业年报
#http://www.tianyancha.com/expanse/annu.json?id=2344338651&ps=5&pn=1
#年报明细信息
#http://www.tianyancha.com/annualreport/newReport.json?id=2344338651&year=2016
from com.inspur.reptile.skyeyes.task.Info import Info
#import com.inspur.reptile.skyeyes.domain.AnualReportEntity as AnualReportEntity
from com.inspur.reptile.skyeyes.domain.AnualReportEntity import AnualReportDetailEntity
from com.inspur.reptile.base.BaseTask import BaseTask
import pymysql

class AnualReport(Info):
    def __init__(self,comid):
        self.comid=comid
        super().__init__(url="%sexpanse/annu.json?id=%s&pn=1&ps=1000"%(super().getBaseUrl(),comid))
        #CrawlTask.__init__(self)
    def run(self):
        ret = self.crawl()
        datas = ret["data"]
        print( "datas", "=" * 8, datas )
        if (datas == None):
            return
        for data in datas:
            #print("data"*8,data)
            AnualReportDetail( self.comid, data["reportYear"],data )
class AnualReportDetail(Info):
    def __init__(self,comid,year,data):
        self.data=data
        self.year=year
        self.comid=comid
        super().__init__(url="%sannualreport/newReport.json?id=%s&year=%s"%(super().getBaseUrl(),comid,year))
    def run(self):
        yearDetail = self.crawl()
        curdata = yearDetail["data"]
        curdata["url"] = "http://www.tianyancha.com/reportContent/%s/%s" % (self.comid, curdata["baseInfo"]["reportYear"])
        curdata["context"] = pymysql.escape_string( str( curdata ) )
        curdata["name"] = curdata["baseInfo"]["companyName"]
        curdata["comid"] = self.comid
        curdata["reportYear"] = self.year
        #print("asfdsadfdasfadsfdasf"*98)
        AnualReportDetailEntity( curdata ,self.taskid)
if __name__ == '__main__':
    comId="2344338651"
    AnualReport(comId)

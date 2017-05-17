#企业年报
#http://www.tianyancha.com/expanse/annu.json?id=2344338651&ps=5&pn=1
#年报明细信息
#http://www.tianyancha.com/annualreport/newReport.json?id=2344338651&year=2015,不仅是这一链接，该链接下的html也是通过json分段拼连的，暂不实现
from com.inspur.reptile.skyeyes.task.Info import Info
import com.inspur.reptile.skyeyes.domain.AnualReportEntity as AnualReportEntity
import uuid
import pymysql

class AnualReport(Info):
    def __init__(self,comId):
        super().__init__(url="%sexpanse/annu.json?id=%s&pn=1&ps=1000"%(super().getBaseUrl(),comId))
class AnualReportDetail(Info):
    def __init__(self,comId,year):
        super().__init__(url="%sannualreport/newReport.json?id=%s&year=%s"%(super().getBaseUrl(),comId,year))

if __name__ == '__main__':
    comId="2344338651"
    ret=AnualReport(comId).crawl()
    datas=ret["data"]
    for data in datas:
        yearDetail=AnualReportDetail(comId,data["reportYear"]).crawl()
        curdata=yearDetail["data"]
        curdata["url"]="http://www.tianyancha.com/reportContent/%s/%s"%(comId,curdata["baseInfo"]["reportYear"])
        curdata["context"]=pymysql.escape_string(str(data))
        curdata["uuid"]=str(uuid.uuid1())
        curdata["name"]=curdata["baseInfo"]["companyName"]
        curdata["comid"] = comId
        curdata["reportYear"] = data["reportYear"]

        AnualReportEntity.AnualReportDetailEntity(curdata).save()
        print(data)
    # for year in  (years):
    #     print(year)
    #     ret=AnualReportDetail("2344338651",year).crawl(False)
    #     html=ret.read()
    #     print(html.decode("utf-8"))

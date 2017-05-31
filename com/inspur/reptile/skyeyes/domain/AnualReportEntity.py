#{"state":"ok","message":"","special":"","vipMessage":"","isLogin":0,"data":{"baseInfo":{
# "reportYear":"2015","companyName":"山东伊莱特重工有限公司","creditCode":"913701007874076393","regNumber":"","phoneNumber":"0531-83806707","postcode":"250207",
# "postalAddress":"济南市章丘市官庄镇济王路9001号","email":"sdyltcw@163.com","manageState":"开业","employeeNum":"企业选择不公示","operatorName":"",
# "totalAssets":"企业选择不公示","totalEquity":"企业选择不公示","totalSales":"企业选择不公示","totalProfit":"企业选择不公示","primeBusProfit":"企业选择不公示",
# "retainedProfit":"企业选择不公示","totalTax":"企业选择不公示","totalLiability":"企业选择不公示"},"changeRecordList":[],"equityChangeInfoList":[],
# "outGuaranteeInfoList":[],"outboundInvestmentList":[],"shareholderList":[{"investorName":"牛余刚","subscribeAmount":"12925","subscribeTime":"2006-04-20",
# "subscribeType":"货币","paidAmount":"12925","paidTime":"2006-04-20","paidType":"货币"},{"investorName":"FORJAS IRAETA HEAVY INDUSTRY S.L.","subscribeAmount":"12925",
# "subscribeTime":"2006-04-20","subscribeType":"货币","paidAmount":"12925","paidTime":"2006-04-20","paidType":"货币"}],"webInfoList":[]}}

# <table id="CWL_ANNUAL_REPORT" name="企业年报">
# 						<column id="ID" primaryKey="true" required="true" type="varchar(30)"   name="ID"/>
# 						<column id="NAME"  type="varchar(128)"  name="年报名称" />
# 						<column id="URL"  type="varchar(512)" name="年报链接"/>
# 						<column id="CONTEXT" type="TEXT" name="年报内容" />
# 						<column	id="COM_ID"   required="true" type="varchar(30)"  name="所属企业ID"/>
# 					</table>
import com.inspur.reptile.base.MySQLTool as mysql
from com.inspur.reptile.skyeyes.domain.Entity import Entity
class AnualReportEntity(Entity):
    def __init__(self,dataStr={},taskid=None):
        self.dataStr=dataStr
        super(AnualReportEntity, self).__init__(taskid)
class AnualReportDetailEntity(Entity):
    tableName="CWL_ANNUAL_REPORT"
    map={"ID":'uuid',"Name":'name',"YEAR":'reportYear',"URL":'url',"CONTEXT":'context',"COM_ID":'comid'}
    def __init__(self,dataStr={},resource=None):
        self.dataStr=dataStr
        self.dataStr["uuid"]=Entity.createUUID()
        super().__init__(resource)



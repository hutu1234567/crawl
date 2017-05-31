#{"state":"ok","message":"","special":"","vipMessage":"","isLogin":0,"data":{"page":{"total":34,"pageNo":1,"pageSize":10,"rows":[
# {"id":null,"productId":null,"product":"卓数大数据交易平台","jingpinProductId":null,"jingpinProduct":"京东万象","sourceWeb":null,"createTime":null,"updateTime":null,
# "isDeleted":0,"companyName":"北京京东叁佰陆拾度电子商务有限公司","graphId":19191697,"companyId":400689,
# "icon":"http://img.798youxi.com/product/upload/575e4fcdcd696.png","iconOssPath":"logo/product/32564b89567bc69fe9d28d2a84de17dd.png","yewu":"数据交易平台",
# "setupDate":1175616000000,"date":1483113600000,"round":"战略融资","value":"","hangye":"企业服务","location":"北京"},

# <table id="CWL_CP" name="竞品信息表">
# 						<column id="ID" primaryKey="true" required="true" type="varchar(30)"   name="ID"/>
# 						<column id="JCOM_ID"  type="varchar(30)"  name="竞品公司ID" />
# 						<column id="JPRO_NAME"  type="varchar(128)" name="竞品名称"/>
#                       <column id="PRO_NAME"  type="varchar(128)" name="产品名称"/>
# 						<column id="REGION" type="varchar(32)" name="地区" />
# 						<column id="CUR_ROUND" type="varchar(32)" name="当前轮次" />
# 						<column id="IND_TYPE" type="varchar(32)" name="行业" />
# 						<column id="BUSINESS" type="varchar(32)" name="业务" />
# 						<column id="CDATE" type="varchar(8)" name="成立时间" />
# 						<column id="VALUATION" type="varchar(32)" name="估值" />
# 						<column	id="COM_ID"   required="true" type="varchar(30)"  name="所属企业ID"/>
# </table>
import com.inspur.reptile.skyeyes.common.DateTool as DateTool
from com.inspur.reptile.skyeyes.domain.Entity import Entity
import pymysql

class CompetingGoodsEntity(Entity):
    map={"ID":'uuid',
         "JCOM_ID":'companyId',
         "JPRO_NAME":'jingpinProduct',
         "PRO_NAME":'product',
         "REGION":'location',
         "CUR_ROUND":'round',
         "IND_TYPE":'hangye',
         "BUSINESS":'yewu',
         "CDATE":'setupDate',
         "VALUATION": 'VALUATION',
         "COM_ID":'comid'
         }
    tableName="CWL_CP"
    def __init__(self,dataStr={},source=None):
        dataStr["uuid"]=Entity.createUUID()
        if('setupDate' in dataStr.keys()):
            dataStr['setupDate']=DateTool.transDataFormat(dataStr['setupDate'],"%Y%m%d")
        #dataStr["content"]=pymysql.escape_string(dataStr["content"])
        self.dataStr=dataStr
        super().__init__(source)
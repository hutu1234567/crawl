#{"state":"ok","message":"","special":"","vipMessage":"","isLogin":0,"data":{"total":4,"result":[
# {"business_scope":"钢坯、圆钢、钢板、合金钢、不锈钢、钢材、法兰、管件、钢球、衬板、锻件的销售；货物进出口。（依法须经批准的项目，经相关部门批准后方可开展经营活动）",
# "percent":"100%","estiblishTime":1477929600000,"regStatus":"在营","legalPersonName":"牛余刚","type":1,"pencertileScore":8616,"amount":8000.0,"id":2944051738,
# "category":"批发业","regCapital":"8000万","name":"济南伊莱特国际贸易有限公司","base":"sd"},
# {"business_scope":"热锻环件、热锻轴件、锻件支承、管道连接件、合金热锻件、船舶锻件产品的研发、生产，销售；货物进出口；房屋、设备租赁服务。(依法须经批准的项目，经相关部门批准后方可开展经营活动)","percent":"100%","estiblishTime":1219075200000,"regStatus":"在营","legalPersonName":"牛余刚","type":1,"pencertileScore":7739,"amount":2000.0,"id":1650676760,"category":"通用设备制造业","regCapital":"2000万","name":"山东金鲁阳重工有限公司","base":"sd"},{"business_scope":"数控车床、数控机床、专用机床、普通机床的研发、生产及售后服务；机床配件的销售。(依法须经批准的项目，经相关部门批准后方可开展经营活动)","percent":"100%","estiblishTime":1394726400000,"regStatus":"在营","legalPersonName":"牛余刚","type":1,"pencertileScore":6176,"amount":200.0,"id":169728266,"category":"通用设备制造业","regCapital":"200万","name":"济南西马特数控机械有限公司","base":"sd"},{"amount":0.0,"id":1530185955,"business_scope":"热锻环件、锻轴件、管件、热锻配件、风电法兰锻件产品的销售。","category":"通用设备制造业","regCapital":"500万元人民币","name":"哈密伊莱特重工有限公司","base":"xj","estiblishTime":1395072000000,"regStatus":"注销","legalPersonName":"牛余刚","type":1,"pencertileScore":6680}]}}

# <table id="CWL_INVEST" name="对外投资表">
#     <column id="ID" primaryKey="true" required="true" type="varchar(30)"   name="ID"/>
#     <column id="COM_NAME"  type="varchar(128)" required="true" name="被投资企业名称"/>
#     <column id="LEGAL_REPRESENT"  type="varchar(128)"  name="被投资法定代表人"/>
#     <column id="REGIST_CAPITAL" type="varchar(32)"  name="注册资本"  />
#     <column id="RATE" type="varchar(32)"  name="投占比例"  />
#     <column id="AMT" type="varchar(32)"  name="投资数额"  />
#     <column id="REGIST_DATE" type="varchar(8)" name="注册时间" />
#     <column	id="STATUS"    type="varchar(32)"  name="状态"/>
#     <column	id="COM_ID"   required="true" type="varchar(30)"  name="所属企业ID"/>
# </table>

import com.inspur.reptile.skyeyes.common.DateTool as DateTool
from com.inspur.reptile.skyeyes.domain.Entity import Entity
class InvestEntity(Entity):
    tableName="CWL_INVEST"
    map={"ID":'uuid',
         "COM_NAME":'name',
         "LEGAL_REPRESENT":'legalPersonName',
         "REGIST_CAPITAL":'regCapital',
         "RATE":'percent',
         "AMT": 'amount',
         "REGIST_DATE":'estiblishTime',
         "STATUS":'regStatus',
         "COM_ID": 'comid'
         }
    def __init__(self,dataStr={},source=None):
        # DateTool.transDataFormat(dataStr,"fromTime","%Y%m%d")
        if("estiblishTime" in dataStr.keys()):
            dataStr["estiblishTime"] = DateTool.transDataFormat(dataStr["estiblishTime"],"%Y%m%d")
        dataStr["uuid"]=Entity.createUUID()
        if("regtime" in dataStr.keys()):
            dataStr['regtime']=DateTool.transDataFormat(dataStr['regtime'],"%Y%m%d")

        self.dataStr=dataStr
        super().__init__(source)
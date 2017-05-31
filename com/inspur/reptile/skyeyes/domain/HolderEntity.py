#{"state":"ok","message":"","special":"","vipMessage":"","isLogin":0,"data":{"total":2,"result":[
# {"amount":12925.0,"id":2061601839,"capitalActl":[{"amomon":"12,925.00万元","paymet":"货币"}],"type":2,"capital":[{"amomon":"12,925.00万元","paymet":"货币","percent":"50.00%"}],"name":"牛余刚"},
# {"id":247748468,"amount":12925.0,"name":"FORJAS IRAETA HEAVY INDUSTRY,S.L","capitalActl":[{"amomon":"12,925.00万元","paymet":"货币"}],"type":1,"capital":[{"amomon":"12,925.00万元","paymet":"货币","percent":"50.00%"}],"pencertileScore":4333}]}}

# <table id="CWL_HOLDER" name="股东信息表">
#     <column id="ID" primaryKey="true" required="true" type="varchar(30)"   name="ID"/>
#     <column id="NAME"  type="varchar(128)" required="true" name="股东名称"/>
#     <column id="RATE" type="varchar(32)"  name="出资比例"  />
#     <column id="AMT" type="varchar(32)" name="认缴出资" />
#     <column	id="COM_ID"   required="true" type="varchar(30)"  name="所属企业ID"/>
# </table>

# import com.inspur.reptile.skyeyes.common.DateTool as DateTool
from com.inspur.reptile.skyeyes.domain.Entity import Entity
class HolderEntity(Entity):
    tableName="CWL_HOLDER"
    map={"ID":'uuid',
         "NAME":'name',
         "RATE":'rate',
         "AMT":'amt',
         "COM_ID": 'comid'
         }
    def __init__(self,dataStr={},source=None):
        # DateTool.transDataFormat(dataStr,"fromTime","%Y%m%d")
        # DateTool.transDataFormat(dataStr,"toTime","%Y%m%d")
        dataStr["uuid"]=Entity.createUUID()
        #print(dataStr["capital"][0]["amomon"])
        dataStr["amt"]=dataStr["capital"][0]["amomon"]
        dataStr["rate"]=dataStr["capital"][0]["percent"]
        self.dataStr=dataStr
        super().__init__(source)
#{"state":"ok","message":"","special":"","vipMessage":"","isLogin":0,"data":{"count":1,"items":[
# {"grade":"A","year":"2015","evalDepartment":"国家税务总局","type":"国税","idNumber":"913701007874076393","name":"山东伊莱特重工股份有限公司"}]}}

# <table id="CWL_TAX_RATING" name="税务评级">
#     <column id="ID" primaryKey="true" required="true" type="varchar(30)"   name="ID"/>
#     <column id="YEAR"  type="varchar(4)"  name="年份" />
#     <column id="RATING"  type="varchar(32)" required="true" name="评级"/>
#     <column id="TYPE" type="varchar(32)" name="类型" />
#     <column id="ID_NUM" type="varchar(32)" name="纳税人识别号" />
#     <column id="RATING_ORGAN" type="varchar(128)" name="评价单位" />
#     <column	id="COM_ID"   required="true" type="varchar(30)"  name="所属企业ID"/>
# </table>

from com.inspur.reptile.skyeyes.domain.Entity import Entity
class TaxRatingEntity(Entity):
    tableName="CWL_TAX_RATING"
    map={"ID":'uuid',
         "YEAR":'year',
         "RATING":'grade',
         "TYPE":'type',
         "ID_NUM":'idNumber',
         "RATING_ORGAN": 'evalDepartment',
         "COM_ID": 'comid'
         }
    def __init__(self,dataStr={},source=None):
        dataStr["uuid"]=Entity.createUUID()
        self.dataStr=dataStr
        super().__init__(source)
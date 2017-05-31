#{"state":"ok","message":"","special":"","vipMessage":"","isLogin":0,"data":{"viewtotal":"9","items":[
# {"id":"22470724","intCls":"07-机械设备","tmPic":"http://cache.tianyancha.com/wap/images/tm_error.png","status":"不定","regNo":"23208372","appDate":"1489939200000",
# "applicantCn":"山东伊莱特重工股份有限公司"},
# {"id":"19795024","intCls":"06-金属材料器具",
# "tmPic":"http://tm-image.tianyancha.com/tm/310d238954c4acbbf9a7c9c225412573.jpg","status":"不定","regNo":"20356183","appDate":"1466352000000",
# "applicantCn":"山东伊莱特重工股份有限公司","tmName":"伊莱特 IRAETA SI"}],"pageSize":"2"}}

# <table id="CWL_TM" name="商标信息">
#     <column id="ID" primaryKey="true" required="true" type="varchar(30)"   name="ID"/>
#     <column id="APPLY_DATE"  type="varchar(8)"  name="申请日期" />
#     <column id="MARK_URL"  type="varchar(512)" name="商标"/>
#     <column id="NAME" type="varchar(256)" name="名称" />
#     <column id="REGIST_CODE" type="varchar(32)" name="注册号" />
#     <column id="TYPE" type="varchar(32)" name="类别" />
#     <column id="STATUS" type="varchar(32)" name="状态"/>
#     <column	id="COM_ID"   required="true" type="varchar(30)"  name="所属企业ID"/>
# </table>

import com.inspur.reptile.skyeyes.common.DateTool as DateTool
from com.inspur.reptile.skyeyes.domain.Entity import Entity
class TradeMarkEntity(Entity):
    tableName="CWL_TM"
    map={"ID":'id',
         "APPLY_DATE":'appDate',
         "MARK_URL":'tmPic',
         "NAME":'applicantCn',
         "REGIST_CODE":'regNo',
         "TYPE": 'intCls',
         "STATUS":'status',
         "COM_ID": 'comid'
         }
    def __init__(self,dataStr={}):
        if ("appDate" in dataStr.keys()):
            dataStr['appDate'] = DateTool.transDataFormat( dataStr['appDate'], "%Y%m%d" )
        self.dataStr=dataStr
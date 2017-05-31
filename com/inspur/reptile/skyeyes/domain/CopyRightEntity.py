#{"state":"ok","message":"","special":"","vipMessage":"","isLogin":0,"data":{"viewtotal":"12","items":[
# {"createTime":"1467308094000","regtime":"1467216000000","publishtime":"1432224000000","authorNationality":"浪潮集团有限公司:中国","updateTime":"1467308094000",
# "regnum":"2016SR161717","catnum":"10100-0000","pid":"1175196","fullname":"浪潮网络机顶盒软件系统","version":"V1.0"},

# <table id="CWL_COPYRIGHT" name="著作权">
# 						<column id="ID" primaryKey="true" required="true" type="varchar(30)"   name="ID"/>
# 						<column id="APPROVE_DATE"  type="varchar(8)"  name="批准日期" />
# 						<column id="FULL_NAME"  type="varchar(256)" name="名称全称"/>
# 						<column id="SHORT_NAME" type="varchar(256)" name="名称简称" />
# 						<column id="REGIST_CODE" type="varchar(32)" name="登记号" />
# 						<column id="TYPE_CODE" type="varchar(32)" name="分类号" />
# 						<column id="VERSION" type="varchar(32)" name="版本号" />
# 						<column id="DETAIL_URL" type="varchar(512)" name="详情" />#即现拼出来的所有内容，已经包括在所有字段中。
# 						<column	id="COM_ID"   required="true" type="varchar(30)"  name="所属企业ID"/>
# </table>

import com.inspur.reptile.skyeyes.common.DateTool as DateTool
from com.inspur.reptile.skyeyes.domain.Entity import Entity
class CopyRightEntity(Entity):
    tableName="CWL_COPYRIGHT"
    map={"ID":'uuid',
         "APPROVE_DATE":'regtime',
         "FULL_NAME":'fullname',
         "SHORT_NAME":'simplename',
         "REGIST_CODE":'regnum',
         "TYPE_CODE":'catnum',
         "VERSION":'version',
         "COM_ID": 'comid'
         }
    def __init__(self,dataStr={},source=None):
        # DateTool.transDataFormat(dataStr,"fromTime","%Y%m%d")
        # DateTool.transDataFormat(dataStr,"toTime","%Y%m%d")
        dataStr["uuid"]=Entity.createUUID()
        if("regtime" in dataStr.keys()):
            dataStr['regtime']=DateTool.transDataFormat(dataStr['regtime'],"%Y%m%d")

        self.dataStr=dataStr
        super().__init__(source)
#{'state': 'ok', 'message': '', 'special': '', 'vipMessage': '', 'isLogin': 0, 'data': {'total': 13,
    # 'result': [{'changeItem': '住所变更', 'createTime': '2017-03-11',
#                 'contentBefore': '<em>山东省</em>济南章丘市官庄<em>乡三赵村西首鲁阳工业园8</em>号',
#               'contentAfter': '济南<em>市</em>章丘市官庄<em>镇济王路9001</em>号', 'changeTime': '2016-01-18'},
#               {'changeItem': '企业类型变更', 'createTime': '2017-03-11', 'contentBefore': '5<em>1</em>10', 'contentAfter': '5<em>2</em>10', 'changeTime': '2016-01-18'}]}}
# <table id="CWL_CHANGE" name="变更记录表">
# 						<column id="ID" primaryKey="true" required="true" type="varchar(30)"   name="ID"/>
# 						<column id="DATE"  type="varchar(8)"  name="变更时间"/>
# 						<column id="ITEM"  type="varchar(128)" name="变更项目"/>
# 						<column id="BEFORE" type="TEXT"  name="变更前"  />
# 						<column id="AFTER" type="TEXT"  name="变更后"  />
# 						<column	id="COM_ID"   required="true" type="varchar(30)"  name="所属企业ID"/>
# 					</table>

from com.inspur.reptile.skyeyes.domain.Entity import Entity
import com.inspur.reptile.skyeyes.common.DateTool as DateTool
import pymysql
class ChangeInfoEntity( Entity ):
    tableName="CWL_CHANGE"
    map={
        "ID":'uuid',
        "DATE":'changeTime',
        "ITEM":'changeItem',
        "BE_CONTENT":'contentBefore',
        "AF_CONTENT":'contentAfter',
        "COM_ID":'comid'
    }
    def __init__(self,dataStr,source=None):
        dataStr["uuid"]=Entity.createUUID()
        # print(dataStr["uuid"],(len(dataStr["uuid"])))
        # print("aaaaaaaa",str(dataStr["changeTime"]).replace("-",""))
        dataStr["changeTime"]=str(dataStr["changeTime"]).replace("-","")
        dataStr["contentBefore"] = pymysql.escape_string( str(dataStr["contentBefore"] ))
        dataStr["contentAfter"] = pymysql.escape_string( str( dataStr["contentAfter"] ) )
        self.dataStr=dataStr
        #print(self.dataStr["changeTime"])
        super().__init__(source)
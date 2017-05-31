#{"state":"ok","message":"","special":"","vipMessage":"","isLogin":0,"data":{"total":7,"result":[
# {"id":2215384706,"typeJoin":["董事"],"type":2,"name":"郑伟"},{"id":2061601839,"typeJoin":["未知"],"type":2,"name":"牛余刚"},
# {"id":2269498528,"typeJoin":["监事"],"type":2,"name":"韩增强"},{"id":2116916839,"typeJoin":["董事"],"type":2,"name":"翟庆彬"},
# {"id":1751105922,"typeJoin":["董事"],"type":2,"name":"Francisco Javier Urios Rodriguez"},{"id":1752545838,"typeJoin":["董事"],"type":2,"name":"Mario Ruiz Escribano"},
# {"id":1751656609,"typeJoin":["董事长"],"type":2,"name":"Javier Ignacio Rubalcaba"}]}}

# <table id="CWL_MAIN_STAFF" name="主要人员">
#     <column id="ID" primaryKey="true" required="true" type="varchar(30)"   name="ID"/>
#     <column id="NAME" type="varchar(128)" required="true"  name="名字"/>
#     <column id="DUTY" type="varchar(32)" required="true" name="职务"/>
#     <column	id="COM_ID"   required="true" type="varchar(30)"  name="所属企业ID",note="同一个人在多个企业任职存放多条数据"/>
# </table>
from com.inspur.reptile.skyeyes.domain.Entity import Entity
import pymysql
class StaffEntity(Entity):
    tableName="CWL_MAIN_STAFF"
    map={"ID":'id',
         "NAME":'name',
         "DUTY":'typeJoin',
         "COM_ID": 'comid',
         }
    def __init__(self,dataStr={},source=None):
        dataStr["typeJoin"]=pymysql.escape_string( str(dataStr["typeJoin"]))
        self.dataStr=dataStr
        super().__init__(source)
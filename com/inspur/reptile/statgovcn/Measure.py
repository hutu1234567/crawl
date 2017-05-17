from com.inspur.reptile.tools.MySQLTool import *
conn = getcon( "10.10.10.32", "root", "123456", "macro", 3306 )
class Measure:
    def __init__(self,id,dbcode,wdcode,isParent):
        self.dbcode = dbcode
        self.id=id
        self.wdcode=wdcode
        self.isParent=isParent
def getAllLeafMeasures(dbcode):
    sql="select id,wd_code,db_code,name,is_parent,pid,memo from macro.MACRO_ZB_TREE_XX where db_code='"+dbcode+"' and wd_code='zb' and is_parent='0' order by id"
    ret=query(conn,sql)
    return ret
def getMeasureByID(id):
    sql = "select id,wd_code,db_code,name,is_parent,pid,memo from macro.MACRO_ZB_TREE_XX where db_code='hgnd' and wd_code='zb' and is_parent='0' and id='" + id +"'"
    ret = query( conn, sql )
    return ret
def getAllTopMeasures():
    sql = "select id,wd_code,db_code,name,is_parent from MACRO_ZB_TREE_XX where pid=''"
    ret = query( conn, sql )
    return ret
def saveMeasure(datas):
    sql = "insert into MACRO_ZB_TREE_XX(id,wd_code,db_code,name,is_parent,pid) values (%s,%s,%s,%s,%s,%s)"
    executes( conn, sql, datas )
def saveMemo(data):
    sql="update macro.MACRO_ZB_TREE_XX set memo=%s where id=%s"
    execute(conn,sql,data)
if __name__ == '__main__':
    print( getAllTopMeasures())
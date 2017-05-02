from com.inspur.reptile.statgovcn.MySQLTool import *
class Measure:
    def __init__(self,id,dbcode,wdcode,isParent):
        self.dbcode = dbcode
        self.id=id
        self.wdcode=wdcode
        self.isParent=isParent
def getAllLeafMeasures():
    conn = getcon( "10.10.10.32", "root", "123456", "macro", 3306 )
    sql="select id,wd_code,db_code,name,is_parent,pid,memo from macro.MACRO_ZB_TREE_XX where db_code='hgnd' and wd_code='zb' and is_parent='0' and id > 'a0304' order by id"
    ret=query(conn,sql)
    return ret
def getMeasureByID(id):
    conn = getcon( "10.10.10.32", "root", "123456", "macro", 3306 )
    sql = "select id,wd_code,db_code,name,is_parent,pid,memo from macro.MACRO_ZB_TREE_XX where db_code='hgnd' and wd_code='zb' and is_parent='0' and id='" + id +"'"
    ret = query( conn, sql )
    return ret
def getAllTopMeasures():
    conn = getcon( "10.10.10.32", "root", "123456", "macro", 3306 )
    sql = "select id,wd_code,db_code,name,is_parent from MACRO_ZB_TREE_XX where pid=''"
    ret = query( conn, sql )
    return ret
if __name__ == '__main__':
    print( getAllTopMeasures())
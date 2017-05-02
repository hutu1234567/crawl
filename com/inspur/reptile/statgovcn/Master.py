from com.inspur.reptile.statgovcn.Measure import *
from com.inspur.reptile.statgovcn.HttpTool import request_ajax_data
from com.inspur.reptile.statgovcn.MySQLTool import *
from com.inspur.reptile.statgovcn.MeasureData import *
import json
import sys
from com.inspur.reptile.statgovcn.CKan import *

url = 'http://data.stats.gov.cn/easyquery.htm?'#url常量，国家统计局的查询基本都通过此url
#tree=[];
def traceTree(curmeasure,tree,leafs,i):#遍历树结构

    if(curmeasure.isParent):#如果是父节点，则把子节点取出，并追加至树末端
        tree += getChildMeasureList( curmeasure )
        #print(tree)
        #print( len( tree ) )
    else:
        leafs + getLeafMeasure( curmeasure )#如果是子节点，则把指标明细取出，暂预留，以后实现
        #print("leafs")
    i+=1
    if(i==len(tree)):#表示走到末端了
        print("len====")
        print(i)
        return ;
    else:
        print(i)
        print( tree[i]["id"])
        current=Measure(tree[i]["id"], "hgnd", "zb",tree[i]["isParent"])
        traceTree(current,tree,leafs,i)
def getChildMeasureList(curmeasure):#获得一个父节点下的子节点列表
    ajaxRequestBody={"id":curmeasure.id,"dbcode":curmeasure.dbcode,"wdcode":curmeasure.wdcode,"m":"getTree"}
    #ajaxRequestBody={"id":"","dbcode":"hgnd","dbcode":"zb","m":"getTree"}

    return request_ajax_data(url,ajaxRequestBody)

def getLeafMeasure(curmeasure):#获得叶子节点下的所有指标，把指标明细取出，暂预留，以后实现
    #print("getLeafMeasure")
    return []

def saveTree(tree):
    datas = []
    for i in range( 0, len( tree ) ):
        measure = tree[i]
        data = (measure["id"], measure["wdcode"], measure["dbcode"], measure["name"], 1 if measure["isParent"] else 0,
                measure["pid"]),
        datas += data
    print( len( tree ) )
    print( "datas===" )
    print( datas )
    conn = getcon( "10.10.10.32", "root", "123456", "macro", 3306 )
    sql = "insert into MACRO_ZB_TREE_XX(id,wd_code,db_code,name,is_parent,pid) values (%s,%s,%s,%s,%s,%s)"
    inserts( conn, sql, datas )

def crawl(measures,startYear,endYear):
    for i in range(len(measures)):
        zb= measures[i][0]
        md = MeasureData( "hgnd", "sj", "zb", "[]",zb, startYear, endYear );
        ret = md.crawl()
        saveData( "zb/", zb, ret )

def getTree():
    sys.setrecursionlimit( 100000001 )
    root = Measure( "", "hgnd", "zb", True )
    tree = []
    leafs = []
    traceTree( root, tree, leafs, -1 )
    saveTree( tree )


if __name__ == '__main__':
    measures=getAllTopMeasures()
    print(measures)
    create_datasets(measures)
    #crawl(measures,1960,2017)
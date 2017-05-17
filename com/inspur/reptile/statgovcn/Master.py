import sys

from com.inspur.reptile.statgovcn.CKan import *
from com.inspur.reptile.statgovcn.MeasureData import *

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
        current=Measure(tree[i]["id"], curmeasure.dbcode, "zb",tree[i]["isParent"])
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
    saveMeasure(datas)

def crawl(measures,startdate,enddate=0):
    for i in range(len(measures)):
        zb= measures[i][0]
        dbcode = measures[i][2]
        md = MeasureData( dbcode, "sj", "zb", "[]",zb, startdate, enddate );
        ret = md.crawl()
        saveData( "D:\\work\\crawl\\statsgovcn\\zb\\test\\", zb, ret )

def getTree():#把指标树爬下来
    sys.setrecursionlimit( 100000001 )
    root = Measure( "", "hgyd", "zb", True )#此处指明是取年度还是月度指标
    tree = []
    leafs = []
    traceTree( root, tree, leafs, -1 )
    saveTree( tree )


if __name__ == '__main__':
    measures=getAllLeafMeasures("hgyd")
    print(measures)
    crawl(measures,"190001-")
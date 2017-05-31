import uuid
import time
import com.inspur.reptile.base.MySQLTool as mysql
import traceback
import pymysql
projectName="20170531-1"
tableName="js_crawl_log"
keymap={
    "flag":'flag',
    "id":'id',
    "source":'source',
    "action": 'action',
    "content": 'content',
    "starttime": 'starttime',
    "endtime": 'endtime',
    "status": 'status',
    "exception": 'exception',
    "projectName":'projectName'
}
class BaseTask:
    def __init__(self,source=None):
        self.taskid=str(uuid.uuid1())
        self.source=source
        #print(self.taskid)
        run(self)

def run(self):
    starttime=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    endtime=""
    data={"projectName":projectName,"flag":self.task_flag,"id":self.taskid,"source":self.source,"action":self.action,"content":"","starttime":starttime,"endtime":endtime,"status":"01","exception":""}
    insertLog(data)
    #print("self"*3,data)
    try:
        time.sleep(self.seelptime)
        self.run()
        data["endtime"]=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        data["status"]="00"
        data["exception"] = ""
    except Exception as e:
        #print("wrong!!!"*8,e)
        data["exception"]=traceback.format_exc()
        data["status"]="99"
        if(hasattr(self,"content") and self.content!=None):
            data["content"]=pymysql.escape_string(str(self.content))
        traceback.print_exc()
        #print("exception data:::",e)
        updateLog(data)
        return
    data["content"]=pymysql.escape_string(str(self.content))
    #print("content"*8,data["content"])
    updateLog(data)
def updateLog(datas):
    sql = "update js_crawl_log set content=%s,endtime=%s,status=%s,exception=%s where id=%s"
    values=[datas["content"],datas["endtime"],datas["status"],datas["exception"],datas["id"]]
    #print("values"*7,values)
    ret=""
    # ret = mysql.execute( getcon(), sql, values )

    try:
        ret= mysql.execute(getcon(),sql,values)
    except:
        values = [str(datas["content"])[0:65535], datas["endtime"], datas["status"], datas["exception"], datas["id"]]
        ret= mysql.execute(getcon(),sql,values)

    return ret
def insertLog(datas):
    mysql.insert( getcon(), tableName, datas, keymap )
def getcon():
    return mysql.getcon( "10.110.1.245", "root", "v6root", "v6db", 3306 )
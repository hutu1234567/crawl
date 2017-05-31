import com.inspur.reptile.base.MySQLTool as mysql
from com.inspur.reptile.base.BaseTask import BaseTask
import uuid

class Entity( BaseTask ):
    def __init__(self,source):
        self.action = "dbsave"
        self.seelptime =0 # 保存数据库为本地操作，不需要延时
        self.content=self.dataStr
        self.task_flag=self.__class__.__name__
        super().__init__(source)
    @staticmethod
    def createUUID():
        ret = str( uuid.uuid1() ).replace( "-", "" )
        #print( (ret), len( ret ) )
        return ret
    def save(self):
        con = mysql.getcon( "10.110.1.245", "root", "v6root", "v6db", 3306 )
        #print("asdsadffadsadsfdasfdasf",self.dataStr)
        mysql.insert( con, self.tableName, self.dataStr, keymap=self.map)

    def run(self):
        self.save()

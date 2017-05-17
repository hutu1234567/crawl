import com.inspur.reptile.tools.MySQLTool as mysql
class Entity:
    def save(self):
        con = mysql.getcon( "10.110.1.245", "root", "v6root", "v6db", 3306 )
        print("asdsadffadsadsfdasfdasf",self.dataStr)
        mysql.excute( con, self.tableName, self.dataStr, keymap=self.map )

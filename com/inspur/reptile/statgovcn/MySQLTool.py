import pymysql
def getcon(host,user,pw,db,port):
    conn = pymysql.connect( host, user, pw, db, port )
    conn.set_charset("utf8")
    return conn

def insert(conn,sql,data):
    cursor=conn.cursor()
    cursor.execute(sql,data)
    conn.commit()
    cursor.close();
def inserts(conn,sql,datas):
    cursor = conn.cursor()
    cursor.executemany( sql, datas )
    conn.commit()
    cursor.close();
def query(conn,sql):
    cursor = conn.cursor()
    ret=cursor.execute( sql )
    list=[]
    list=cursor.fetchmany(ret)
    #print(cursor.fetchone())

    #for i in range (ret):
        #print[cursor[ret]]
    cursor.close();
    return  list;
if __name__ == '__main__':
    conn=getcon("10.10.10.32","root","123456","macro",3306)
    list=query("select id,id,id,wd_code wd from macro.MACRO_ZB_TREE_XX where db_code='hgnd' and wd_code='zb'")
    for i in range(len(list)):
        print(list[i][3])
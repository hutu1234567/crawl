import pymysql
def insert(conn, tablename, datas, keymap):
    keyword="insert into "
    keys = ""
    values = ""
    #print( datas )
    for sqlKey, sqlValueName in keymap.items():
        keys += sqlKey + ","
        sqlValue = datas[sqlValueName] if sqlValueName in datas.keys() else ""
        values += "'" + str( sqlValue ) + "',"
        pass
    keys = keys[:-1]  # 去除最后一个逗号
    values = values[:-1]  # 去除最后一个逗号
    sql = keyword + tablename + "(" + keys + ") values(" + values + ")"
    #print( sql )
    #print(conn)
    execute( conn, sql, None )

def getcon(host,user,pw,db,port):
    conn = pymysql.connect( host, user, pw, db, port )
    conn.set_charset("utf8")
    return conn

def execute(conn,sql,data):
    cursor=conn.cursor()
    ret=cursor.execute(sql,data)
    conn.commit()
    cursor.close();
    return  ret
def executes(conn,sql,datas):
    cursor = conn.cursor()
    cursor.executemany( sql, datas )
    conn.commit()
    cursor.close();
def query(conn,sql):
    cursor = conn.cursor()
    ret=cursor.execute( sql )
    #list=[]
    #list=cursor.fetchmany(ret)
    list=cursor.fetchall()

    #print(cursor.fetchone())

    #for i in range (ret):
        #print[cursor[ret]]
    cursor.close();
    return  list;
if __name__ == '__main__':
    conn=getcon("10.110.1.245", "root", "v6root", "v6db", 3306 )
    sql = "update js_crawl_log set status=%s,source=%s where id=%s"
    data=["00","2","c3b23292-4044-11e7-9f5e-f0d5bf49ff6f"]
    print(execute(conn,sql,data))
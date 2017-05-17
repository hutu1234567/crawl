from datetime import datetime

def transDataFormat(datas={},keyname="",dateformat=""):
    if (keyname in datas.keys()):
        dt = datetime.fromtimestamp( int(datas[keyname]) / 1000 )
        datas[keyname] = dt.strftime(dateformat )
        print( datas[keyname] )
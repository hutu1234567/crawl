from datetime import datetime

# def transDataFormat(datas={},keyname="",dateformat=""):
#     if (keyname in datas.keys()):
#         dt = datetime.fromtimestamp( int(datas[keyname]) / 1000 )
#         datas[keyname] = dt.strftime(dateformat )
#         print( datas[keyname] )

def transDataFormat(dateStr,dateformat=""):
        if(dateStr!=None and str(dateStr)!="0"):
                dt = datetime.fromtimestamp( int(dateStr) / 1000)
                return dt.strftime( dateformat )
        else:
                return ""
if __name__ == '__main__':
        transDataFormat(0,"%Y%m%d")
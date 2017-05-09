import csv

def saveData(folder,zb,data):

    print( data )
    csvfile = open( folder + zb + ".csv", 'w',newline="",encoding='utf_8_sig' )
    #f = codecs.open(csvfile,'w', 'utf_8_sig')
    writer = csv.writer( csvfile )
    writer.writerows( data )
    csvfile.close();
datas=[]
data1=["201702-","100.9171446","100.80201168"]
data2=["a001","a0034"]
datas.append(data1)
datas.append(data2)
print (datas)
print(tuple(datas))
saveData("test","aa",datas)

from com.inspur.reptile.skyeyes.task.Info import Info
import com.inspur.reptile.skyeyes.domain.AnualReportEntity as AnualReportEntity
from com.inspur.reptile.base.BaseTask import BaseTask
import pymysql

if __name__ == '__main__':
    for i in range(0,10):
        try:
            if (i == 4):
                raise Exception
            print(i)

        except:
            print("error")

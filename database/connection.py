import pymysql
class connection:
    def con(self):
        con = pymysql.connect(host='localhost', user='root', password='neha1611', database='bankGUI')
        cursor = con.cursor()
        return cursor,con

""" Connect to MySQL """

import MySQLdb
from datetime import date

class MySQLConnector:
    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.database = None
        self.cur = None
        self.result = None
    
    def _connect(self):
        self.database = MySQLdb.connect(host=self.host,
                                        user=self.user,
                                        passwd=self.passwd,
                                        db=self.db)
        self.cur = self.database.cursor()

    def _close(self):
        self.cur.close()
        self.database.close()
    
    def _query(self, strquery: str, dataQuery=None):
        if dataQuery:
            self.cur.execute(strquery, dataQuery)
        else:
            self.cur.execute(strquery)
        self.database.commit() # need to commit data to the database
        self.result = self.cur.fetchall()
        return self.result # return to see if the result is empty

    def __str__(self):
        sol = "\n"
        for row in self.result:
            for col in row:
                sol += str(col) + " "
            sol += "\n"
        return sol

    def __len__(self):
        return len(self.cur.fetchall())

# db = MySQLConnector('127.0.0.1', 'test','MyPassword1!', 'BirthdayTracker' )

# db._connect()
# createTable = ("CREATE TABLE IF NOT EXISTS Birthday "
#         "(FName VARCHAR(15) NOT NULL, "
#         "Lname VARCHAR(15) NOT NULL, "
#         "Bdate DATE NOT NULL, "
#         "PhoneNum CHAR(10) NOT NULL, "
#         "CONSTRAINT PK_BDAY PRIMARY KEY(Fname,Bdate,PhoneNum)); ")

# insertData = ("INSERT " "INTO Birthday "
#             "(Fname, Lname, Bdate, PhoneNum) "
#             "VALUES (%s, %s, %s, %s);")

# data = ('Hao', 'Doan', '1997-12-05', '8609609397')
# sample2 = ('SELECT' '*' "FROM Birthday")

# birthday = ("SELECT *, YEAR(CURDATE()) - YEAR(Bdate) AS age FROM Birthday;")
# # db._query(birthday)
# age = ("SELECT Fname, Lname, YEAR(CURDATE()) - YEAR(Bdate) AS age "
#                     "FROM Birthday "
#                     "WHERE Fname=%s AND Lname=%s;")
# name = ('Hao', 'Doan')
# db._query(sample2)
# print(db)

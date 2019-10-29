""" Birthday Class """
from MySQLConnector import *
class Birthday:
    def __init__(self):
        self.name = ""
        self.db = MySQLConnector('localhost', 'isthattyler','#####', 'BirthdayTracker' )
        self.db._connect()
        self.age = ("SELECT Fname, Lname, YEAR(CURDATE()) - YEAR(Bdate) AS age "
                    "FROM Birthday "
                    "WHERE Fname=%s AND Lname=%s;")

    def run(self):
        print("Welome to the program.")
        print("\nThis program will tell you the year the person is born, their age.")
        print("\n If the person you mentioned is not available on our database, you can choose to add the person in.")
        self.name = input("\nPlease input their Fname and their Lname separated by whitespace: ")
        name = tuple(self.name.split())
        self.search(name)
        if len(self.db) == 0:
            pass
        temp = str(self.db)
        print("\nHere's the info of the person you requested for: " + temp)

    def search(self, name):
        self.db._query(self.age, name)

a = Birthday()
a.run()

""" Birthday Class """
from MySQLConnector import *
import socket

class Birthday:
    def __init__(self):
        self.config = ""
        # get host address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        host = s.getsockname()[0]

        self.db = MySQLConnector(host, 'test','MyPassword1!', 'BirthdayTracker' )
        self.db._connect()

    def run(self):
        choice = 1
        print("Welome to the program.")
        print("\nThis program will tell you their birthday or their age.")
        print("\nIf the person you mentioned is not available on our database, you can choose to add the person in.")
        print("\n1. Look for age    2. Look for birthday")
        option = int(input("What do you want to do today? "))
        while choice:
            if option == 1:
                self.getAge()
            else:
                self.getBirthday()
            print("\n0. No   1. Yes")
            choice = int(input("\nDo you want to look for another person? "))
        print("\nHave a good day!")
        exit()

    def getBirthday(self):
        self.config = input("\nPlease input their Fname and their Lname separated by whitespace(* to show everyone in database): ")
        if self.config == '*':
            self.searchBirthday(self.config, all=1)
            temp = str(self.db)
            print("\nHere's the info of everyone you requested for: \n" + temp)
        else:
            name = tuple(self.config.split())
            result = self.searchBirthday(name)
            if not result:
                self.__noName()
            else:
                temp = str(self.db)
                print("\nHere's the info of the person you requested for: \n" + temp)
    
    def getAge(self):
        self.config = input("\nPlease input their Fname and their Lname separated by whitespace(* to show everyone in database): ")
        if self.config == '*':
            self.searchAge(self.config, all=1)
            temp = str(self.db)
            print("\nHere's the info of everyone you requested for: \n" + temp)
        else:
            name = tuple(self.config.split())
            result = self.searchAge(name)
            if not result:
                self.__noName()
            else:
                temp = str(self.db)
                print("\nHere's the info of the person you requested for: \n" + temp)

    def __noName(self):
        print("The person appears to not be on our database.")
        print("\n0. No   1. Yes")
        choice = int(input("\nDo you want to put this person into our database for future reference? "))
        if choice:
            self.config = input("\nPlease input the person Fname, Lname, Bdate(YYYY-MM-DD), and Phone number separated by whitespace: ")
            print(self.config)
            print("Thank you. The data has been inserted.")
            config = tuple(self.config.split())
            print(config)
            self.insert(config)
        else:
            print("\nOkay no worries! Have a good day!")
            exit()

    def insert(self, config):
        query = ("""INSERT INTO Birthday
                    (Fname, Lname, Bdate, PhoneNum)
                    VALUES (%s, %s, %s, %s);""")
        return self.db._query(query, config)

    def searchBirthday(self, name, all=0):
        if not all:
            query = ("""SELECT Fname, Lname, Bdate
                        FROM Birthday
                        WHERE Fname=%s AND Lname=%s;""")
            return self.db._query(query, name)
        else:
            query = ("""SELECT Fname, Lname, Bdate
                        FROM Birthday;""")
            return self.db._query(query)

    def searchAge(self, name, all=0):
        if not all:
            query = ("""SELECT Fname, Lname, YEAR(CURDATE()) - YEAR(Bdate) AS age
                        FROM Birthday
                        WHERE Fname=%s AND Lname=%s;""")
            return self.db._query(query, name)
        else:
            query = ("""SELECT Fname, Lname, YEAR(CURDATE()) - YEAR(Bdate) AS age
                        FROM Birthday;""")
            return self.db._query(query)

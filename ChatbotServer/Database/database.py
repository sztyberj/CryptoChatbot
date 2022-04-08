import pyodbc

SERVER = 'tcp:serverforchatbot.database.windows.net,1433'
DATABASE = 'chatbot_db'
USERNAME = ''
PASSWORD = ''

cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server='+SERVER+';Database='+DATABASE+';Uid='+USERNAME+';Pwd={'+PASSWORD+'};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cursor = cnxn.cursor()

class Database:
    def __init__(self):
        Database.create_database(self)

    def create_database(self):
        try:
            cursor.execute('CREATE TABLE Glossary (key_desc varchar(50), val_desc varchar(MAX));')
            cursor.commit()
        except:
            pass

        try:
            cursor.execute('CREATE TABLE Cryptocurrency (Name varchar(25), ShortName varchar(8), Price money, Date date);')
            cursor.commit()
        except:
            pass

if __name__ == '__main__':
    new = Database()

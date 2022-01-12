import ChatbotServer.Database.database as db

class Database:
    def __init__(self):
        Database.create_database(self)


    def create_database(self):
        try:
            db.cursor.execute('CREATE TABLE Glossary (key_desc varchar(50), val_desc varchar(MAX));')
            db.cursor.commit()
        except:
            pass

        try:
            db.cursor.execute('CREATE TABLE Cryptocurrency (Name varchar(25), ShortName varchar(8), Price money NULL, Date date);')
            db.cursor.commit()
        except:
            pass


def insert_prices(name, data):
    query = "INSERT INTO dbo."+name+" VALUES (?, ?, ?, ?);"
    db.cursor.executemany(query, data)
    db.cursor.commit()

def select_newest_date():
    query = "SELECT TOP(1) Date FROM dbo.Cryptocurrency ORDER BY Date DESC;"
    db.cursor.execute(query)
    row = db.cursor.fetchone()
    for i in row:
        return i

def insert_glossary(name, data):
    query = "INSERT INTO dbo." + name + " VALUES (?, ?);"
    db.cursor.executemany(query, data)
    db.cursor.commit()

def count_glossary():
    query = "SELECT COUNT(*) FROM dbo.Glossary;"
    db.cursor.execute(query)
    result = db.cursor.fetchone()
    for i in result:
        return i

def delete_all(name):
    query = f"DELETE FROM dbo.{name};"
    db.cursor.execute(query)
    db.cursor.commit()

def select_all(name):
    query = f"SELECT key_desc, val_desc FROM dbo.{name};"
    db.cursor.execute(query)
    result = db.cursor.fetchall()
    return(result)


if __name__ == '__main__':
    new = Database()

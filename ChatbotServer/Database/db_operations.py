import ChatbotServer.Database.database as db

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

def select_all_gloss(name):
    query = f"SELECT key_desc, val_desc FROM dbo.{name};"
    db.cursor.execute(query)
    result = db.cursor.fetchall()
    return(result)

def select_all_prices(name, date):
    query = f"SELECT Name, ShortName, Price FROM dbo.{name} WHERE Date = '{date}';"
    db.cursor.execute(query)
    result = db.cursor.fetchall()
    return(result)



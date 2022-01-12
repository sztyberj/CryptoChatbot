import pyodbc

SERVER = 'tcp:serverforchatbot.database.windows.net,1433'
DATABASE = 'chatbot_db'
USERNAME = 'user'
PASSWORD = ''

cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server='+SERVER+';Database='+DATABASE+';Uid='+USERNAME+';Pwd={'+PASSWORD+'};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cursor = cnxn.cursor()

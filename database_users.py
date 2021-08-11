import sqlite3 as sql3

with sql3.connect('databases/users.db') as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL);
''')

cursor.execute('''
INSERT INTO users(userID,username,password) VALUES(0,"admin","admin");
''')

cursor.execute('''
INSERT INTO users(userID,username,password) VALUES(1,"guest","guest");
''')

db.commit()
db.close()
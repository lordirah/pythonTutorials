import mysql.connector
import csv

conn = mysql.connector.connect(host = 'localhost', database = 'employees', user = 'root' , password = 'root')
cur = conn.cursor()
cur.execute("show tables;")
out = cur.fetchall()
fs = open('/home/lordirah/Documents/table_list.csv', 'w')

c = csv.writer(fs)
for x in out:
    c.writerow(x)
fs.close()

fs = open('/home/lordirah/Documents/table_list.csv', 'r')
for table in fs:
    cur.execute(f"select * from {table};")
    out = cur.fetchall()
    fs = open(f'/home/lordirah/Documents/{table}.csv', 'w')
    c = csv.writer(fs)
    for x in out:
        c.writerow(x)
    fs.close()
    #Test comment
import csv
import MySQLdb

conn = MySQLdb.connect(host='*****', user='****', passwd='****', db='**')
with open('C:/Users/New User/Desktop/tmp.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        print(row['email'])
        conn = MySQLdb.connect(host='*****', user='****', passwd='****', db='**')
        sql_statement = "INSERT INTO yuvi_test VALUES (%s)"
        cur = conn.cursor()
        cur.executemany(sql_statement,[(row['email'])])
        conn.escape_string(sql_statement)
        conn.commit()
print("CSV has been imported into the database")
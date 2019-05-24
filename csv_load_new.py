import csv
import MySQLdb
from datetime import datetime

conn = MySQLdb.connect(host='*****', user='****', passwd='****', db='**')
with open('C:/Users/New User/Desktop/tmp.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        print(row['call_date'], row['source'], row['appointment_id'])
        row['call_date'] = datetime.strptime(row['call_date'], '%m/%d/%Y %H:%M').strftime('%Y-%m-%d')
        print(row['call_date'])
        conn = MySQLdb.connect(host='*****', user='****', passwd='****', db='**')
        sql_statement = "INSERT IGNORE INTO cc_yuvi_test VALUES (%s,%s,%s)"
        cur = conn.cursor()
        cur.executemany(sql_statement,[(row['call_date'], row['source'], row['appointment_id'])])
        conn.escape_string(sql_statement)
        conn.commit()
print("CSV has been imported into the database")

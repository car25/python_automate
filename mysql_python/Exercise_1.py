import mysql.connector


conn = mysql.connector.connect(host='*****', user='****', passwd='****', db='**')

#To fetch data using mysql connection
#cur = conn.cursor()
#cur.execute("select * from DATABASE.TABLE where date(date) = '2019-06-19'")

#To store data directly in Dataframe from mysql connection


df = pd.read_sql("select * from DATABASE.TABLE where date(date) = '2019-06-19'",con=conn)
df = df.reset_index(drop = True)
print(df)

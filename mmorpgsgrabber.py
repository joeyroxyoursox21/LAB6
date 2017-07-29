#LAB1 Python starter code
#Based upon manual at http://mysql-python.sourceforge.net/MySQLdb.html

#imports go here
import MySQLdb
#import _mysql

#code goes here

#1

#db = _mysql.connect(host="localhost",user="root",passwd="cherry",db="wine")
#db.query("""SELECT * FROM wine;""")
#r = db.store_result()
#nR = r.num_rows()
#while(nR > 0):
#	print(r.fetch_row())
#	nR = nR - 1
#db.close()

#2

db = MySQLdb.connect(host="localhost", user="root",passwd="password123",db="mmorpgs")
db.query("""SELECT * FROM games;""")
r = db.store_result()
nR = r.num_rows()
while(nR > 0):
	print(r.fetch_row())
	nR = nR - 1
db.close()
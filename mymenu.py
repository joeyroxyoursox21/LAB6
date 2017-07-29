#LAB6 Python starter code
#imports go here
#import MySQLdb
import _mysql

#code goes here

buffer = "true"



def oneQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="password123",db="mmorpgs")
	db.query("""SELECT * FROM games;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def twoQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="password123",db="mmorpgs")
	db.query("""SELECT * FROM developer;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	db.close()

def threeQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="password123",db="mmorpgs")
	#db.query("""SELECT * FROM genre WHERE genreID NOT IN (SELECT * FROM genre as a, ownership AS b WHERE  
	#	a.genreID = b.genreID;)""")
	db.query("""SELECT genreID FROM genre WHERE genreID not in (select genreID from ownership)""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row())
		nR = nR - 1
	if nR == 0:
		print("""all genres have at least 1 developer and game title""")
	db.close()
	
while buffer:
	print("""
	0.Exit
	1.See games
	2.See developers
	3.See if a genre has no current listing of games
	""")
	buffer=input("what would you like to do? ")
	if buffer == 1:
		oneQuery()
	if buffer == 2:
		twoQuery()
	if buffer == 3:
		threeQuery()
#!/usr/bin/python
#database stuff
#includes code for getting data from table on heroku
import psycopg2, json

def create_db():
	conn = psycopg2.connect(database = "d6feqf5qisicl6", user = "okscvkvnefgxow",
                            password = "5b233bf7e422a825065c12b53eae0d59048358e5ac518cb71e7cf3233107e3c6",
                            host = "ec2-54-221-192-231.compute-1.amazonaws.com", port = "5432")
	#print("Opened database successfully")
	cur = conn.cursor()
	cur.execute('''CREATE TABLE location (latitude double precision     NOT NULL,longitude double precision    NOT NULL);''')
	conn.commit()


#to insert to database
def insert_db():
	conn = psycopg2.connect(database = "d6feqf5qisicl6", user = "okscvkvnefgxow",
                            password = "5b233bf7e422a825065c12b53eae0d59048358e5ac518cb71e7cf3233107e3c6",
                            host = "ec2-54-221-192-231.compute-1.amazonaws.com", port = "5432")
	cur = conn.cursor()
	cur.execute("INSERT INTO public.location(latitude, longitude) VALUES (77.64562511, 12.87829352)")
	cur.execute("INSERT INTO public.location(latitude, longitude) VALUES (77.64540342, 12.87832982)")
	cur.execute("INSERT INTO public.location(latitude, longitude) VALUES (77.64391553, 12.87897244)")
	cur.execute("INSERT INTO public.location(latitude, longitude) VALUES (77.64359296, 12.87916801)")
	cur.execute("INSERT INTO public.location(latitude, longitude) VALUES (77.64339224, 12.87928266)")
	cur.execute("INSERT INTO public.location(latitude, longitude) VALUES (77.64189524, 12.88110895)")
	conn.commit()

def insert_location(loc):

    conn = psycopg2.connect(database = "d6feqf5qisicl6", user = "okscvkvnefgxow",
                            password = "5b233bf7e422a825065c12b53eae0d59048358e5ac518cb71e7cf3233107e3c6",
                            host = "ec2-54-221-192-231.compute-1.amazonaws.com", port = "5432")
    cur = conn.cursor()

    l1 = loc[1]
    l2 =loc[0]
    print(l1,l2)
    cur.execute("INSERT INTO public.location(latitude, longitude) VALUES (" + str(l1) + "," + str(l2) + ")")
    conn.commit()   

# to collect data from database
def myrecords():
    conn = psycopg2.connect(database = "d6feqf5qisicl6", user = "okscvkvnefgxow",
                            password = "5b233bf7e422a825065c12b53eae0d59048358e5ac518cb71e7cf3233107e3c6",
                            host = "ec2-54-221-192-231.compute-1.amazonaws.com", port = "5432")
    cur = conn.cursor()
    data = {}
    data_json =[]
    cur.execute("SELECT latitude, longitude from location")
    rows = cur.fetchall()
    for row in rows:
    	data['latitude'] = row[0]
    	data['longitude'] = row[1]
    	data_json.append(json.loads(json.dumps(data)))
    return data_json

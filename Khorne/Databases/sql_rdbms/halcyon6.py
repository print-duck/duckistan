''' Intro to py - databases using sqlite3  '''
import sqlite3
####
####coon=sqlite3.connect("halcyon.db")
####curs=coon.cursor()
#####Create table and attributes(columns)
####curs.execute('''CREATE TABLE IF NOT EXISTS station_alpha
####                        ( access_key INTEGER PRIMARY KEY,
####                        crew_member TEXT,
####                        faction TEXT,
####                        clearance INTEGER )''')
####
#####Creating data tuples (rows)
##curs.execute('''INSERT INTO station_alpha
##                        (crew_member,faction,clearance)
##                        VALUES
##                        ("Gerhard","Overseer",5),
##                        ("Jurgen","Overseer",5),
##                        ("Richard","Overseer",5),
##                        ("Saito","Overseer",5),
##                        ("Sherwood","Overseer",5)''')
##
####curs.execute('''INSERT INTO station_alpha
####                        (crew_member,faction,clearance)
####                        VALUES
####                        ("Heilich","First_officer",4),
####                        ("Kenway","Cadet",2),
####                        ("Ernest","Cadet",2),
####                        ("Huy","Cadet",2),
####                        ("Pavlov","Cadet",2)''')
####
#####Reading data tuples (rows)
####print("Print all details of all crew of clearance level 2")
####curs.execute('''SELECT *
####                        FROM station_alpha
####                        WHERE clearance=2''')
####outrows= curs.fetchall()
####print(outrows,'\n')
####
####print("Print all details of one crew of clearance level 5")
####curs.execute('''SELECT *
####                        FROM station_alpha
####                        WHERE clearance=5''')
####outrow= curs.fetchone()
####print(outrow,'\n')
####
####print("Print only faction details of all crew")
####curs.execute('''SELECT faction
####                        FROM station_alpha''')
####outrows= curs.fetchall()
####print(outrows,'\n')
####
####print("Print name and faction details of all crew")
####curs.execute('''SELECT crew_member, faction
####                         FROM station_alpha''')
####outrows= curs.fetchall()
####print(outrows,'\n')
####
####print("Print faction, faction, name and faction details in that particular order of all crew with clearance level 2")
####curs.execute('''SELECT faction, faction, crew_member, faction
####                         FROM station_alpha
####                         WHERE clearance=2''')
####outrows= curs.fetchall()
####print(outrows,'\n')
####
####curs.execute('''DROP TABLE station_alpha''')
######Deletes the table
####coon.commit()
####coon.close()
####
####
####
####print("completed")
####
def con_curs_1():
    global  con1
    global curs1
    con1=sqlite3.connect("halcyon.db")
    curs1=con1.cursor()

def commit_close():
    con1.commit()
    con1.close()

def station_relation():
    global station
    station=input("Enter Station callsign: ")
    curs1.execute(f'''CREATE TABLE IF NOT EXISTS {station}
                                (access_key INTEGER PRIMARY KEY,
                                crew_member TEXT,
                                faction TEXT,
                                clearance INTEGER)''')

def get_crew_data():
    global details
    details=[]
    detail=[]
    prompt=int(input("Please enter number of crew members to be added: "))
    for i in range(prompt):
        detail.append(input("Name: "))
        detail.append(input("Faction: "))
        detail.append(int(input("Clearance: ")))
        detail=tuple(detail)
        details.append(detail)
        detail=[]

def multicrew_add():
    curs1.executemany(f'''INSERT INTO {station}
                            (crew_member, faction, clearance)
                            VALUES ( ? , ? , ?)''', details)
def get_data():
    station=input("Enter Station Name: ")
    curs1.execute(f'''SELECT *
                            FROM {station}''')
    mydat=curs1.fetchall()
    print(mydat)

con_curs_1() #Create a connection to the database and cursor to the connection
station_relation() #Create a relation (table) with attributes (columns with data type)
get_crew_data() #Get crew data (tuples (rows) ) in real time
multicrew_add() #Add the crew data to the station 
get_data() #get all data from a station
commit_close() #Save and close the database connection

print("completed")



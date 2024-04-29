import sqlite3
import q1
import q2

con=sqlite3.connect(':memory:')

if con:

    try:
        cur=con.cursor()
        cur.execute('create table locations(location_id int primary key, street_address varchar(100), postal_code varchar(50), city varchar(50), state_province varchar(50), country_id char(2))')
        cur.execute('insert into locations values(1000,"1297 Via Cola di Rie","989", "Roma",null,"IT"),\
                    (1100,"93091 Calle della Te","10934","Vennice",null,"IT"),\
                    (1200,"2017 Shinjiku-ku","1689","Tokyo","Tokyo Perfectu","JP"),\
                    (1300,"9450 Kamiya-cho","6823","Hiroshima",null,"JP"),\
                    (1400,"2014 Jaberwocky Rd","26192","Southlake","Texas","US"),\
                    (1500,"2011 Interiors Blvd","99236","South San","California","US"),\
                    (1600,"2007 Zagora St","50090","South Brun","New Jersey","US"),\
                    (1700,"2004 Charade Rd","98199","Seattle","Washington","US"),\
                    (1800,"147 Spadina Ave","MSV 2L7","Toronto","Ontario","CA")')
        
        cur.execute('create table countries(country_id int primary key, country_name varchar(50),region_id int)')
        cur.execute('insert into countries values("AR","Argentina",2),\
                    ("AU","Australia",3),("BE","Belgium",1),("BR","Brazil",2),("CA","Canada",2),\
                    ("CH","Switzerland",1),("CN","China",3),("DE","Germany",1)')
        
        #Query1
        print('\nQUERY 1')
        q1.Query1.q1(con)

        #Query2
        print('\nQUERY2')
        q2.Query2.q2(con)


    except Exception as e:
        print('connection error: ',e)

else:
    print('in memory connection not successful, please try later')


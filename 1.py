

#1- Create a database. Create the following tables:
1. Book
    2. Titles
    3. Publishers
    4. Zipcodes
    5. AuthorsTitles
    6. Authors
import pymysql as pm

try:
    con = pm.connect(host='localhost', database='library', user='root',password='R00t_mnl')
    cursor = con.cursor()
    
    query1 = 'create table zip_codes(zipcode_id int(6) primary key,city varchar(10),state varchar(20),zip_code varchar(6))'
    query2 = 'create table publishers (pub_id varchar(5) primary key ,pub_name varchar(20),street_add varchar(20),suite_num varchar(5), zipcode_id int(6),foreign key(zipcode_id) references zip_codes(zipcode_id))'
    query3 ='create table title(title varchar(50),ISBN int(10),pub_id varchar(5),publication_yr year,title_id varchar(5) primary key, foreign key(pub_id) references publishers(pub_id))'
    query4 ='create table books (book_id int(5) primary key,title_id varchar(5) ,location varchar(20), genre varchar(10),foreign key(title_id) references title(title_id))'
    query5 = 'create table authors(author_id varchar(5) primary key,first_name varchar(10),middle_name varchar(10),last_name varchar(10))'
    query6 = 'create table authors_title (aut_tiltle_id int(5) primary key, author_id varchar(5),title_id varchar(5),foreign key(title_id) references title(title_id),foreign key(author_id) references authors(author_id))'
  
       
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    cursor.execute(query4)
    cursor.execute(query5)
    cursor.execute(query6)

  
    print("table made")
   
except pm.DatabaseError as e:
    if con:
        con.rollback()
        print("problem",e)
finally:
   cursor.close()
   con.close()'''

'''#2- Insert values in the tables.
import pymysql as pm

try:
    con = pm.connect(host='localhost', database='library', user='root',password='R00t_mnl')
    cursor = con.cursor()

    query_mul1 = "insert into zip_codes values(%s,%s,%s,%s)"
    data1 = [(999,'city1','state1','zc1'),
            (998,'city2','state2','zc2'),
            (997,'city3','state3','zc3'),
            (996,'city4','state4','zc4')]

    query_mul2 = "insert into publishers values(%s,%s,%s,%s,%s)"
    data2 = [('P01','jai','street x','sn11',999),
            ('P02','vijay','street y','sn12',998),
            ('P03','ajay','street z','sn13',997),
            ('P04','sanjay','street u','sn14',996)]

    query_mul3 = "insert into title values(%s,%s,%s,%s ,%s)"
    data3 = [('ABC',100001,'P01','2001','T0001'),
            ('CDE',100002,'P01','2002','T0002'),
            ('EFG',100003,'P01','2003','T0003'),
            ('GHI',100004,'P01','2004','T0004')]
    
    query_mul4 = "insert into books values(%s,%s,%s,%s)"
    data4 = [(10001,'T0001','A1','comedy'),
            (20002,'T0002','B1','fiction'),
            (30003,'T0003','C1','drama'),
            (40004,'T0004','D1','satire')]
    
    query_mul5 = "insert into authors values(%s,%s,%s,%s)"
    data5 = [('AU01','meenal','','goel'),
            ('AU02','riya','',',malik'),
            ('AU03','anshul','','gupta'),
            ('AU04','gauri','xy','agarwal')]

    query_mul6 = "insert into authors_title values(%s,%s,%s)"
    data6 = [(11,'AU01','T0001'),
            (22,'AU02','T0002'),
            (33,'AU03','T0003'),
            (44,'AU04','T0004')]

    
    
    cursor.executemany(query_mul1, data1)
    cursor.executemany(query_mul2, data2)
    cursor.executemany(query_mul3, data3)
    cursor.executemany(query_mul4, data4)
    cursor.executemany(query_mul5, data5)
    cursor.executemany(query_mul6, data6)

    con.commit()
    
    print("data inserted")
except pm.DatabaseError as e:
    if con:
        con.rollback()
        print("problem",e)
finally:
   cursor.close()
   con.close()

#3- Update any values in any of the tables. Print the original and updated values.

import pymysql as pm

try:
    con = pm.connect(host='localhost', database='library', user='root',password='R00t_mnl')
    cursor = con.cursor()
    
    query_select = 'select * from books'
    cursor.execute(query_select)
    
    data1 = cursor.fetchall()
    for row in data1:
        print("book_id: {}, title_id: {}, location: {}, genre: {} ".format(row[0],row[1],row[2],row[3]))

    #update
    query = "update books set genre = 'satire' where book_id= 10001"
    cursor.execute(query)

    query_select = 'select * from books'
    cursor.execute(query_select)
    
    data1 = cursor.fetchall()
    for row in data1:
        print("book_id: {}, title_id: {}, location: {}, genre: {} ".format(row[0],row[1],row[2],row[3]))

except pm.DatabaseError as e:
    if con:
        con.rollback()
        print("problem",e)

finally:
   con.close()
   
dbs.py
Displaying dbs.py.

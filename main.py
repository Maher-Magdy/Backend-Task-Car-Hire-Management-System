import flask
import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="9999",
    database="carDB"
)
the_cursor=db.cursor()

# MySQL commands to create the DB schema
# the_cursor.execute("CREATE TABLE customer (cuid INTEGER PRIMARY KEY , name varchar(50))")
# the_cursor.execute("CREATE TABLE car (cid int PRIMARY KEY,car_type varchar(50),price_per_day int,cuid int ,available_date DATE , date_of_hire DATE , date_to_be_returned DATE, no_of_days int  ,foreign key (cuid) REFERENCES customer(cuid) ON DELETE RESTRICT ON UPDATE CASCADE)")



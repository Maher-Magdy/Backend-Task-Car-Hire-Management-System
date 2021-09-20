from flask import Flask ,render_template,request
import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="9999",
    database="car_DB"
)
the_cursor=db.cursor()

# MySQL commands to create the DB schema
# the_cursor.execute("CREATE TABLE customer (cuid INTEGER PRIMARY KEY AUTO_INCREMENT, name varchar(50))")
# the_cursor.execute("CREATE TABLE car (cid int PRIMARY KEY AUTO_INCREMENT,car_type varchar(50),price_per_day int,cuid int ,available_date DATE , date_of_hire DATE , date_to_be_returned DATE, no_of_days int  ,foreign key (cuid) REFERENCES customer(cuid) ON DELETE RESTRICT ON UPDATE CASCADE)")

# create endpoints
app =Flask(__name__)
# show customer list
@app.route("/",methods=["GET","POST"])
@app.route("/customers",methods=["GET","POST"])
def add_customers():
    if  request.method=="POST":
        data=request.form
        name=data["name"]
        the_cursor.execute("insert into customer(name) values(%s)",(name,))
        db.commit()
        # the_cursor.close()
        # print the db content
        the_cursor.execute("select * from customer")
        customers_list=the_cursor.fetchall()
        # read from an html file to display the webpage
    return render_template("customers.html",customers_list=customers_list)


# add a customer
@app.route("/customers/add",methods=["GET","POST"])
def func():
    # read from an html file to display the webpage
    return render_template("add_customer.html")

# run in debug mode
if __name__ =="__main__":
    app.run(debug=True)


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
@app.route("/",methods=["GET","POST","delete","get","put"])
@app.route("/customers",methods=["GET","POST","delete","get","put"])
def add_customers():
    customers_list=[]
    if  request.method=="POST":
        data=request.form
        name=data["name"]
        the_cursor.execute("insert into customer(name) values(%s)",(name,))
        db.commit()
        # the_cursor.close()

    elif request.method=="put":
        data = request.form
        updatedname = data["updatedname"]
        oldname = data["oldname"]
        the_cursor.execute("UPDATE customer set name = %s where name = %s", (updatedname,oldname,))
        db.commit()
        print(update,oldname)

    elif request.method == "delete":
        data = request.form
        name = data["name"]
        the_cursor.execute("delete from customer where name = %s", (name,))
        db.commit()

    elif request.method == "get":
        data = request.form
        name = data["name"]
        the_cursor.execute("select from customer where name = %s",(name,))
        customers_list = the_cursor.fetchall()


    if request.method != "get":
        # select the db content
        the_cursor.execute("select * from customer")
        customers_list = the_cursor.fetchall()

        # read from an html file to display the webpage
    return render_template("customers.html",customers_list=customers_list)


# add a customer
@app.route("/customers/add",methods=["GET","POST","delete","get","put"])
def add():
    # read from an html file to display the webpage
    return render_template("add_customer.html")

@app.route("/customers/update",methods=["GET","POST","delete","get","put"])
def update():
    # read from an html file to display the webpage
    return render_template("update_customer.html")

@app.route("/customers/delete",methods=["GET","POST","delete","get","put"])
def delete():
    # read from an html file to display the webpage
    return render_template("delete_customer.html")

@app.route("/customers/get",methods=["GET","POST","delete","get","put"])
def get():
    # read from an html file to display the webpage
    return render_template("get_customer.html")

# run in debug mode
if __name__ =="__main__":
    app.run(debug=True)


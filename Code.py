import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="mysql", database="kashmir_tourism")
cur=mydb.cursor()

def View_Activities(): 
    cur.execute("select * from Activities")
    rec=cur.fetchall()
    for i in rec:
        print(i)

def View_Customers():
    cur.execute("select * from Customers")
    rec=cur.fetchall()
    for i in rec:
        print(i)
        
def Add_Activity():
    L=[]
    a=input("Enter Activity ID: ")
    L.append(a)
    b=input("Enter Name: ")
    L.append(b)
    c=input("Enter Location: ")
    L.append(c)
    d=input("Enter Price: ")
    L.append(d)
    Activity=(L)
    cur.execute("insert into Activities(Act_ID, Act_Name, Location, Price) values(%s,%s,%s,%s)",Activity)
    mydb.commit()
    print("1 record inserted")

def Add_Customer():
    L=[]
    a=input("Enter Customer ID: ")
    L.append(a)
    b=input("Enter Name: ")
    L.append(b)
    c=input("Enter Age: ")
    L.append(c)
    d=input("Enter Contact Number: ")
    L.append(d)
    e=input("Enter Activity ID: ")
    L.append(e)
    Customer=(L)
    cur.execute("insert into Customers(Cust_ID, Name, Age, Cont_Number, Act_ID) values(%s,%s,%s,%s,%s)",Customer)
    mydb.commit()
    print("1 record inserted")

def Del_Customer():
    c_id=input("Enter Customer ID to be deleted: ")
    t=(c_id,)
    cur.execute("delete from Customers where Cust_ID=%s",t)
    mydb.commit()
    print("1 record deleted")
c="y"
while c=="y":
    print("1. To Display the Activities")
    print("2. To Display the Customers")
    print("3. To Add new Activity")
    print("4. To Add new Customer")
    print("5. To Delete a Customer")
    ch=int(input("Enter your choice: "))
    if (ch==1):
        View_Activities()
    elif (ch==2):
        View_Customers()
    elif (ch==3):
        Add_Activity()
    elif (ch==4):
        Add_Customer()
    elif (ch==5):
        Del_Customer()
    else:
        print("Enter a valid choice")
    c=input("Enter \'y\' to continue: ")
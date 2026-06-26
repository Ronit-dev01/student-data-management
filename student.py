import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='root',
    password="sakshi@123",
    database="STUDENT_MANAGEMENT"
)
cursor=db.cursor()
def add_student():
    name=input("Enter the name : ").upper()
    age=input("Enter the age : ")
    branch=input("Enter the branch : ").upper()
    sgpa=float(input("Enter the sgpa : "))
    contact=input("Enter contact no. : ")
    sql="INSERT INTO RECORDS (name,age,branch,sgpa,contact) VALUES (%s,%s,%s,%s,%s)"
    values=(name,age,branch,sgpa,contact)
    cursor.execute(sql,values)
    db.commit()
    print("student added succesfully")
def view_student():
    cursor.execute("SELECT * FROM RECORDS")
    data=cursor.fetchall()
    print(f"{"ID":<5}{"NAME":<15}{"AGE":<5}{"BRANCH":<15}{"SPGA":<8}{"CONATCT":<12}")
    print(55*"-")
    for row in data:
        print(f"{row[0]:<5}{row[1]:<15}{row[2]:<5}{row[3]:<15}{row[4]:<8}{row[5]:<12}")
    print(55*"-")
def update_student():
    student_id=int(input("ENTER THE ID OF THE STUDENT : "))
    while True :
        print("-"*33)
        print("what you want to update FOR ID :".upper(),student_id,)
        print("-"*33)
        print("1.update NAME".upper())
        print("2.update AGE".upper())
        print("3.update course".upper())
        print("4.update sgpa".upper())
        print("5.update contact no. ".upper())
        print("6.exit".upper())
        option=input("enter your choice : ".upper())
        if option=="1":
            set_name=input("enter the new name : ".upper())
            set_name=set_name.upper()
            cursor.execute("UPDATE RECORDS SET name = %s where ID= %s",(set_name,student_id))
            db.commit()
            print("name updated successfully ✅ ")
        elif option=="2":
            set_age=input("enter new age : ".upper())
            set_age=set_age.upper()
            cursor.execute("UPDATE RECORDS SET age = %s where ID= %s",(set_age,student_id))
            db.commit()
            print("age updated successfully ✅".upper())
        elif option=="3":
            set_course=input("enter new course : ".upper())
            set_course=set_course.upper()
            cursor.execute("UPDATE RECORDS SET branch=%s where ID=%s",(set_course,student_id))
            db.commit()                
            print("course changed successfully ✅ 3")
        elif option=="4":
            set_sgpa=float(input("enter new sgpa : "))
            cursor.execute("UPDATE RECORDS SET sgpa=%s where ID=%s",(set_sgpa,student_id))
            db.commit()
            print("SGPA UPDATED SUCCESSFULLY ✅")
        elif option=="5":
            set_contact=input("enter new contact.no : ".upper())
            cursor.execute("UPDATE RECORDS SET contact=%s where id=%s",(set_contact,student_id))
            db.commit()
            print("contact updated successfully ✅")
        elif option == "6":
            print("thank you for using")
            break
        else:
                print("invalid choice".upper())
def search_student():
    while True:
        print("-"*15)
        print("SEARCH STUDENT")
        print("-"*15)
        print("TYPE 2 IF YOU WANT TO EXIT PROGRAM")
        print(" ")
        name=input("enter the name of student :".upper())
        print("")
        if name=="2":
            break
        name=name.upper()
        cursor.execute("SELECT * FROM RECORDS WHERE NAME LIKE %s",("%" + name + "%",))
        result=cursor.fetchall()
        print(f"{"ID":<5}{"NAME":<15}{"AGE":<8}{"BRANCH":<10}{"SPGA":<10}{"CONATCT":<12}")
        print(60*"-")
        for row in result:
            print(f"{row[0]:<5}{row[1]:<15}{row[2]:<8}{row[3]:<10}{row[4]:<10}{row[5]:<12}")
            
while True:
    print("-"*81)
    print("----------------------------STUDENT MANAGEMENT SYSTEM----------------------------".upper())
    print("-"*81)
    print(" ")
    print("choose option for operation :- ".upper())
    print("-"*30)
    print("1.add student".upper())
    print("2.view student info".upper())
    print("3.update students data".upper())
    print("4.search student ".upper())
    print("5.exit".upper())
    choice=input("enter your choice: ".upper())
    if choice=="1":
        add_student()
    elif choice=="2":
        view_student()
    elif choice=="3":
        update_student()    
    elif choice=="4":
        search_student()
    elif choice=="5":
        print("thank you for using")
        break
    else:
        print("invalid choice")

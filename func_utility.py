from db_conn import *
from unique_id import get_unique_id
import tkinter
from tkinter import messagebox
import datetime

def get_user_id():
    uid=get_unique_id(length=3)
    return str(uid)

def get_pid():
    pid=get_unique_id(length=3)
    return str(pid)


    
def validate_register(name,user_name,password):
    mydb=get_connection()
    mycursor=mydb.cursor(buffered=True)
    try:
        sql="Select count(*) from user where username=%s"
        uname=(user_name,)
        mycursor.execute(sql,uname)
        res=mycursor.fetchone()
        if res[0]==0:
            user_id=get_user_id()
            sql_1="insert into user (name,username,password,user_id) values(%s,%s,%s,%s)"
            set1=(name,user_name,password,user_id)
            mycursor.execute(sql_1,set1)
            mydb.commit()
            mydb.close()
            return None
        else:
            return("This username has been taken!")
    except Exception as e:
        print(e)
        return("Database Error")


def validate_login(user_name,password):
    mydb=get_connection()
    mycursor=mydb.cursor(buffered=True)
    try:
        sql_2="Select user_id from user where username=%s and  password=%s"
        set2=(user_name,password)
        mycursor.execute(sql_2,set2)
        res=mycursor.fetchone()
        if(res is None):
            messagebox.showerror("Error","Invalid Credentials")
            return None
        else:
            arg=res[0]
            print("successful login")
            return user_name
    except Exception as e:
        messagebox.showerror("DATABASE ERROR!",e)


def get_todo_id():
    tid=get_unique_id(length=6)
    return tid

def get_status(init_date):
    if(datetime.datetime.now()==init_date):
        return 0
    else:
        return -1

def get_uid(username):
    mydb=get_connection()
    mycursor=mydb.cursor(buffered=True)
    try:
        qry="Select user_id from user where username=%s"
        set1=(username,)
        mycursor.execute(qry,set1)
        res=mycursor.fetchone()
        mydb.close()
        return res[0]
    except Exception as e:
        print(e)


def create_todo(user_name,title,desc,init_date):
    mydb=get_connection()
    mycursor=mydb.cursor(buffered=True)
    init_date=init_date.strftime("%Y%m%d")
    try:
        status=get_status(init_date)
        todo_id=get_todo_id()
        user_id=get_uid(user_name)
        sql_1="Insert into todo (title,description,status,todo_id,uid,date_created) values(%s,%s,%s,%s,%s,%s)"
        set1=(title,desc,status,todo_id,user_id,init_date)
        mycursor.execute(sql_1,set1)
        mydb.commit()
        mydb.close()
        return todo_id
    except Exception as e:
        print(e)
        messagebox.showerror("DATABASE ERROR",e)

def fetchTodo(username):
    mydb=get_connection()
    uid=get_uid(username)
    mycursor=mydb.cursor(buffered=True)
    try:
        qry="Select * from todo where uid=%s"
        set1=(uid,)
        mycursor.execute(qry,set1)
        res_set=mycursor.fetchall()
        mydb.close()
        return(res_set)
    except Exception as e:
        messagebox.showerror("DATABASE ERROR",e)


def todoUpdate(title,desc,status,tid):
    mydb=get_connection()
    mycursor=mydb.cursor(buffered=True)
    try:
        qry="update todo set title=%s, description=%s, status=%s where todo_id=%s"
        set1=(title,desc,status,tid)
        mycursor.execute(qry,set1)
        mydb.commit()
        mydb.close()
        return 1
    except Exception as e:
        messagebox.showerror("DATABASE ERROR",e)

def todoDelete(tid):
    mydb=get_connection()
    mycursor=mydb.cursor(buffered=True)
    try:
        qry="delete from todo where todo_id=%s"
        set1=(tid,)
        mycursor.execute(qry,set1)
        mydb.commit()
        mydb.close()
        return 1
    except Exception as e:
        messagebox.showerror("DATABASE ERROR",e)

def addDiary(username,desc):
    mydb=get_connection()
    mycursor=mydb.cursor(buffered=True)
    uid=get_uid(username)
    curr_date=datetime.datetime.today().strftime ('%Y%m%d')
    try:
        qry="Insert into daily_diary(date,description,uid) values(%s,%s,%s)"
        set1=(curr_date,desc,uid)
        mycursor.execute(qry,set1)
        mydb.commit()
        mydb.close()
        return 1
    except Exception as e:
        messagebox.showerror("DATABASE ERROR",e)
    

def fetchDiary(date):
    mydb=get_connection()
    mycursor=mydb.cursor(buffered=True)
    try:
        qry="Select * from daily_diary where date=%s"
        set1=(date,)
        mycursor.execute(qry,set1)
        res=mycursor.fetchall()
        mydb.close()
        return res[0]
    except Exception as e:
        messagebox.showerror("DATABASE ERROR",e)


def del_Diary(date):
    mydb=get_connection()
    mycursor=mydb.cursor(buffered=True)
    try:
        date=str(date)
        print(date)
        qry="delete from daily_diary where date=%s"
        set1=(date,)
        mycursor.execute(qry,set1)
        mydb.commit()
        print(mycursor.rowcount)
        if(mycursor.rowcount!=0):
            messagebox.showinfo("MyDiary","Deleted Successfully")
        else:
            messagebox.showerror("ERROR","Something went wrong,TRY AGAIN")
        mydb.close()
    except Exception as e:
        messagebox.showerror("DATABASE ERROR",e)
    

def deleteAcc(username):
    mydb=get_connection()
    mycursor=mydb.cursor(buffered=True)
    try:
        qry="delete from user where username=%s"
        set1=(username,)
        mycursor.execute(qry,set1)
        mydb.commit()
        if(mycursor.rowcount!=0):
            messagebox.showinfo("MyDiary","Account Deleted Successfully")
            return True
        else:
            return False
    except Exception as e:
        print(e)
        messagebox.showerror("DATABASE ERROR",e)


def save_loc_db(path,username):
    mydb=get_connection()
    mycursor=mydb.cursor(buffered=True)
    uid=get_uid(username)
    pid=get_pid()
    try:
        qry="insert into playlist values(%s,%s,%s)"
        set1=(path,pid,uid)
        mycursor.execute(qry,set1)
        mydb.commit()
        if(mycursor.rowcount!=0):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        messagebox.showerror("DATABASE ERROR",e)
    
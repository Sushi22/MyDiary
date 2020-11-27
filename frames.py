import tkinter
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from func_utility import *
import datetime
from tkinter import ttk
from tkinter import filedialog
from songs import *
import random



class Register:

    def __init__(self):
        self.root=Tk()
        self.root.geometry("950x650+300+100")
        self.root.title("MyDiary")

        self.root.resizable(False,False)

        self.headingframe=Frame(self.root,bg="white")
        self.headingframe.place(x=0,y=0,relwidth=1,relheight=0.25)
        Label(self.headingframe,text="MyDiary",font=("Raleway","40","bold"),fg="OrangeRed2",bg="white").pack(pady=30)

        self.bg=ImageTk.PhotoImage(file="images/diary4.jpg")
        self.body=Frame(self.root)
        self.body.place(x=0,y=160,relwidth=1,relheight=0.75)
        Label(self.body,image=self.bg).place(relwidth=1,relheight=1)

        self.form=Frame(self.body).place(x=30,y=30,relwidth=0.6,relheight=0.8)

        Label(self.form,text="Start Writing!!",font=("Helvetica",23),fg="DodgerBlue2").place(x=200,y=230)

        name=Label(self.form,text="Name",font=("Timesnewroman",15)).place(x=80,y=300)
        self.e_name=Entry(self.form,font=("Timesnewroman",15))
        self.e_name.place(x=200,y=300)

        username=Label(self.form,text="Username",font=("Timesnewroman",15))
        username.place( x=80,y=350)
        self.e_username=Entry(self.form,font=("Timesnewroman",15))
        self.e_username.place(x=200,y=350)

        password=Label(self.form,text="Password",font=("Timesnewroman",15))
        password.place( x=80,y=400)
        self.e_password=Entry(self.form,font=("Timesnewroman",15),show="*")
        self.e_password.place(x=200,y=400)

        Button(self.form, text="Register",font=("Helvetica",16),fg="DodgerBlue2",command=self.register).place(x=100,y=480)
        Button(self.form, text="Existing User ?",font=("Helvetica",16),fg="DodgerBlue2",command=self.login).place(x=350,y=480)

        self.root.mainloop()

    def register(self):
        param1=self.e_name.get()
        param2=self.e_username.get()
        param3=self.e_password.get()
        error=validate_register(param1,param2,param3)
        if(param2=="" or param3==""):
            messagebox.showerror("showerror","Username and Password are mandatory")
        else:
            if error:
                messagebox.showerror("showerror",error)
            else:
                self.root.destroy()
                Login()
    
    def login(self):
        self.root.destroy()
        Login()



class Login:
    def __init__(self):
        self.root=Tk()
        self.root.geometry("950x650+300+100")
        self.root.title("MyDiary")

        self.root.resizable(False,False)

        self.headingframe=Frame(self.root,bg="white")
        self.headingframe.place(x=0,y=0,relwidth=1,relheight=0.25)
        Label(self.headingframe,text="MyDiary",font=("Raleway","40","bold"),fg="OrangeRed2",bg="white").pack(pady=30)

        self.bg=ImageTk.PhotoImage(file="images/diary4.jpg")
        self.body=Frame(self.root)
        self.body.place(x=0,y=160,relwidth=1,relheight=0.75)
        Label(self.body,image=self.bg).place(relwidth=1,relheight=1)

        self.form=Frame(self.body).place(x=30,y=30,relwidth=0.6,relheight=0.8)

        Label(self.form,text="Login",font=("Helvetica",23),fg="DodgerBlue2").place(x=250,y=230)

        username=Label(self.form,text="Username",font=("Timesnewroman",15))
        username.place( x=80,y=350)
        self.e_username=Entry(self.form,font=("Timesnewroman",15))
        self.e_username.place(x=200,y=350)

        password=Label(self.form,text="Password",font=("Timesnewroman",15))
        password.place( x=80,y=400)
        self.e_password=Entry(self.form,font=("Timesnewroman",15),show="*")
        self.e_password.place(x=200,y=400)

        Button(self.form, text="Not Registered?",font=("Helvetica",12,"bold"),fg="DodgerBlue2",command=self.register).place(x=240,y=480)
        Button(self.form, text="login",font=("Helvetica",16),bg="OrangeRed2",width="8",height="1",fg="white",command=self.login).place(x=250,y=560)

        self.root.mainloop()

    def register(self):
        self.root.destroy()
        Register()

    def login(self):
        param1=self.e_username.get()
        param2=self.e_password.get()
        if(param1=="" or param2==""):
            messagebox.showerror("showerror","All fields are required")
        else:
            result=validate_login(param1,param2)
            if(type(result)==str):
                self.root.destroy()
                mainFrame(result)


class mainFrame:

    flag=False
    def __init__(self,username):
        self.root=Tk()
        self.user=username
        self.root.geometry("950x650+300+100")
        self.root.title("MyDiary")

        self.root.resizable(False,False)

        self.headingframe=Frame(self.root,bg="white")
        self.headingframe.place(x=0,y=0,relwidth=1,relheight=0.25)
        Label(self.headingframe,text="MyDiary",font=("Raleway","40","bold"),fg="OrangeRed2",bg="white").pack(pady=30)
        
        note="Hello {}".format(self.user)

        Label(self.headingframe,text=note,bg="white",font=('Helvetica',16)).place(x=20,y=100)
        

        Button(self.headingframe,text="Log Out",bg="white",font=("Helvetica",10),command=self.logout).place(x=870,y=100)
        Button(self.headingframe,text="Delete Account",bg="white",font=("Helvetica",10),command=self.del_acc).place(x=740,y=100)

        self.todo_frame=Frame(self.root)
        self.todo_frame.place(x=0,y=160,relheight=0.75,relwidth=0.35)
        self.v=Scrollbar(self.todo_frame,orient=VERTICAL)
        self.v.pack(side=RIGHT,fill=Y)
        
        Label(self.todo_frame,text="Todos",font=("Helvetica",20)).place(x=30,y=40)

        Button(self.todo_frame,text="Add Task",font=("Helvetica",15,"bold"),bg="DodgerBlue2",fg="white",command=self.add_task).place(x=35,y=110)
        Button(self.todo_frame,text="Display Todos",font=("Helvetica",15,"bold"),bg="IndianRed1",fg="black",command=self.display).place(x=35,y=170)

        self.bg=ImageTk.PhotoImage(file="images/diary3.jpg")
        self.body=Frame(self.root)
        self.body.place(x=330,y=165,relwidth=0.65,relheight=0.75)
        Label(self.body,image=self.bg).place(relwidth=1,relheight=1)
        Label(self.body,text="Hey! how was your day ?",bg="pale turquoise",font=("Helvetica",11,"italic")).place(x=10,y=5)
        Label(self.body,text=datetime.datetime.today().strftime("%d-%B-%Y"),bg="pale turquoise",font=("Courier",12)).place(x=390,y=5)

        icon = ImageTk.PhotoImage(file="images/musicIcon1.png") 
        Button(self.body,image=icon,command=self.play_song).place(x=580,y=6)

        self.diary_desc=Text(self.body)
        self.diary_desc.place(x=0,y=40,relwidth=1)

        Button(self.body,text="Save Diary",font=("Lucida",13),bg="DodgerBlue",fg="white",command=self.add_diary).place(x=255,y=420)
        Button(self.body,text="See Diary",font=("Lucida",13),bg="DodgerBlue",fg="white",command=self.select_date).place(x=455,y=420)
        Button(self.body,text="Collections",font=("Lucida",13),bg="DodgerBlue",fg="white",command=lambda:Collections(self.user)).place(x=55,y=420)
        
        self.root.mainloop()


    def play_song(self):
        my_playlist=make_list(self.user)
        if(len(my_playlist)==0):
            messagebox.showinfo("MyDiary","Your playlist is empty!")
        else:
            print(self.flag)
            if(self.flag==False):
                self.flag=True
                song=random.choice(my_playlist)
                print(song)
                Play.trigger(self.user,song)
            else:
                Play.trigger()
                self.flag=False
                
            
        
    def del_acc(self):
        t=Toplevel(self.root)
        t.geometry("600x300+500+280")
        Label(t,text="Are you sure you want to delete your account?",font=("Helvetica",15)).place(x=55,y=110)
        Button(t,text="Delete",bg="red",fg="white",font=("Arial",12),command=self.sure_del).place(x=55,y=230)
        Button(t,text="Cancel",bg="dim gray",fg="white",font=("Arial",12),command=t.destroy).place(x=150,y=230)
        


    def sure_del(self):
        val=deleteAcc(self.user)
        if(val):
            self.root.destroy()
            Register()
        else:
            messagebox.showerror("ERROR","Something went wrong , TRY AGAIN")



    def logout(self):
        self.root.destroy()
        Login()
    
    def add_diary(self):
        param1=self.diary_desc.get("1.0",'end-1c')
        val=addDiary(self.user,param1)
        if val==1:
            messagebox.showinfo("MyDiary","Added to your Diary :)")

    def select_date(self):
        self.t=Toplevel(self.root)
        self.t.geometry("400x300+600+280")
        self.t.title("Select Date")
        Label(self.t,text="Enter Date :",font=("Helvetica",15,"bold")).place(x=50,y=80)
        Label(self.t,text="(Date must be in the format: 'YYMMDD')",font=("Lucida",10,"italic")).place(x=55,y=130)
        self.e_date=Entry(self.t,font=("Arial",12))
        self.e_date.place(x=55,y=160)
        Button(self.t,text="OK",font=('Helvetica',12),bg="DodgerBlue2",fg="white",command=self.see_diary).place(x=55,y=230)


    def see_diary(self):
        date=self.e_date.get()
        print(date)
        self.t.destroy()
        details=fetchDiary(date)
        print(details)
        if(details):
            fullDiary(self.user,details)
        else:
            messagebox.showerror("ERROR","Invalid date")
          



    def add_task(self):
        Todo(self.user)


    def display(self):
        self.todo_list=fetchTodo(self.user)
        if(len(self.todo_list)==0):
            Label(self.todo_frame,text="You have no todos!",font=("Courier",14),fg="red").place(x=35,y=260)

        for i in self.todo_list:
            self.single_todo=Frame(self.todo_frame)
            self.single_todo.place(x=0,y=250,relwidth=0.7)
            Label(self.single_todo,text="Assgined Date : {}".format(i[5]),font=("Courier",9,"bold")).pack()
            Label(self.single_todo,text=i[0],font=("Helvetica",12,"bold")).pack()
            Label(self.single_todo,text=i[1],font=("Helvetica",10)).pack()
            Button(self.single_todo,text="EDIT", bg="DodgerBlue2",fg="white",font=("Courier",9,"bold"),command=lambda:UpdateTodo(i[0],i[1],i[3])).pack()
            Button(self.single_todo,text="DELETE",bg="red",fg="White", font=("Courier",9,"bold"),command=lambda:self.delete_todo(i[3])).pack()
            
            if(i[2]==0):
                Label(self.single_todo,text="PENDING",font=("Helvetica",12,"bold"),fg="red").pack()
            elif(i[2]==1):
                Label(self.single_todo,text="COMPLETED",font=("Helvetica",12,"bold"),fg="green4").pack()
        
            
    def delete_todo(self,tid):
        val=todoDelete(tid)
        if val==1:
            messagebox.showinfo("MyDiary","Task Deleted")




class Todo:

    def __init__(self,username):
        self.root=Tk()
        self.user=username
        self.root.geometry("500x300+530+280")

        Label(self.root,text="Title",font=("Timesnewroman",14),fg="green4").place(x=50,y=20)
        self.e_title=Entry(self.root,font=("Timesnewroman",12),width="25")
        self.e_title.place(x=50,y=60)

        self.curr_date=datetime.datetime.today()
        now_date=self.curr_date.strftime("%d-%B-%Y")

        Label(self.root,text=now_date,font=("Courier",10,"bold")).place(x=350,y=20)

        Label(self.root,text="Description",font=("Timesnewroman",14),fg="green4").place(x=50,y=90)
        self.e_desc=Entry(self.root,font=("Timesnewroman",12),width="35")
        self.e_desc.place(x=50,y=120)

        Button(self.root,text="Save",font=("Helvetica",13),bg="deep sky blue",command=self.make).place(x=200,y=200)
        

        self.root.mainloop()

    def make(self):
        param1=self.e_title.get()
        param2=self.e_desc.get()
        create_todo(self.user,param1,param2,self.curr_date)
        messagebox.showinfo("TODO","Task added")
        self.root.destroy()
        

class UpdateTodo:
    val=None
    def __init__(self,title,desc,tid):
        self.root=Tk()
        self.tid=tid

        self.root.geometry("500x300+530+280")

        Label(self.root,text="Title",font=("Timesnewroman",14),fg="green4").place(x=50,y=20)
        self.e_title=Entry(self.root,font=("Timesnewroman",12),width="25")
        self.e_title.place(x=50,y=60)
        self.e_title.insert(END,title)

        self.curr_date=datetime.datetime.today()
        now_date=self.curr_date.strftime("%d-%B-%Y")

        Label(self.root,text=now_date,font=("Courier",10,"bold")).place(x=350,y=20)

        Label(self.root,text="Description",font=("Timesnewroman",14),fg="green4").place(x=50,y=90)
        self.e_desc=Entry(self.root,font=("Timesnewroman",12),width="35")
        self.e_desc.place(x=50,y=120)
        self.e_desc.insert(END,desc)

        var = tkinter.IntVar()
        self.checked=ttk.Checkbutton(self.root, text=" Completed ?")
        self.checked.place(x=130,y=180)

        Button(self.root,text="Save",font=("Helvetica",13),bg="firebrick",command=self.update).place(x=120,y=250)
        Button(self.root,text="Cancel",font=("Helvetica",13),bg="dim gray",command=self.cancel).place(x=200,y=250)

        
        self.root.mainloop()

    def update(self):
        param1=self.e_title.get()
        param2=self.e_desc.get()
        bool_val=self.checked.instate(['selected'])
        if(bool_val):
            param3=1
        else:
            param3=0
        val=todoUpdate(param1,param2,param3,self.tid)
        if val==1:
            messagebox.showinfo("INFO","Todo Updated successfully")
        self.root.destroy()

        mainFrame.display()

    def cancel(self):
        self.root.destroy()


class fullDiary:

    def __init__(self,username,details):
        self.root=Tk()
        self.user=username
        self.details=details
        self.root.geometry("950x650+300+100")
        self.root.title("MyDiary")

        self.root.resizable(False,False)

        self.headingframe=Frame(self.root,bg="white")
        self.headingframe.place(x=0,y=0,relwidth=1,relheight=0.25)
        Label(self.headingframe,text="MyDiary",font=("Raleway","40","bold"),fg="OrangeRed2",bg="white").pack(pady=30)
        
        note="Hello {}".format(self.user)

        Label(self.headingframe,text=note,bg="white",font=('Helvetica',18)).place(x=50,y=100)

        Button(self.headingframe,text="Log Out",bg="white",font=("Helvetica",16),command=self.logout).place(x=840,y=100)

        self.diary_frame=Frame(self.root)
        self.diary_frame.place(x=0,y=170,relwidth=1,relheight=0.75)

        Label(self.diary_frame,text=self.details[0].strftime("%d-%B-%Y"),font=("Courier",12,"bold")).pack(pady=2)

        Label(self.diary_frame,text=self.details[1]).pack(pady=5)


        Button(self.diary_frame,text="Delete",bg="black",fg="white",font=("Arial",12),command=self.delete_diary).pack()

        self.root.mainloop()



    def logout(self):
        self.root.destroy()
        Login()

    def delete_diary(self):
        del_Diary(self.details[0].strftime("%Y%m%d"))


class Collections:

    def __init__(self,username):
        self.root=Tk()
        self.user=username
        self.root.geometry("950x650+300+100")
        self.root.title("MyDiary")

        self.root.resizable(False,False)

        self.headingframe=Frame(self.root,bg="white")
        self.headingframe.place(x=0,y=0,relwidth=1,relheight=0.25)
        Label(self.headingframe,text="MyDiary",font=("Raleway","40","bold"),fg="OrangeRed2",bg="white").pack(pady=30)
        
        note="Hello {}".format(self.user)

        Label(self.headingframe,text=note,bg="white",font=('Helvetica',16)).place(x=20,y=100)
        

        Button(self.headingframe,text="Log Out",bg="white",font=("Helvetica",10),command=self.logout).place(x=870,y=100)


        Button(self.root,text="Playlist",font=("Helvetica",14),bg="OrangeRed2",fg="white",command=self.browse).place(x=50,y=170)


        self.root.mainloop()

    def logout(self):
        self.root.destroy()
        Login()


    def browse(self):
        self.t=Toplevel(self.root)
        self.t.geometry("400x300+600+280")
        self.t.title("Browse File")
        Label(self.t,text="Enter location of file",font=("Helvetica",15,"bold")).place(x=50,y=80)
        Label(self.t,text="(or you can browse)",font=("Lucida",10,"italic")).place(x=55,y=130)
        self.e_path=Entry(self.t,font=("Arial",12))
        self.e_path.place(x=55,y=160)
        Button(self.t,text="Browse",font=('Helvetica',12),bg="DodgerBlue2",fg="white",command=self.add_file).place(x=55,y=230)
        Button(self.t,text="ADD",font=('Helvetica',12),bg="DodgerBlue2",fg="white",command=self.add_song).place(x=170,y=230)

    def add_file(self):
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype=(("mp3 files","*.mp3"),("all files","*.*")) )
        self.t.attributes('-topmost',1)
        self.e_path.insert(0,self.filename)

    def add_song(self):
        self.t.attributes('-topmost',0)
        if(self.e_path.get()==""):
            messagebox.showinfo("MyDiary","Please enter path or browse")

        else:
            val=save_loc_db(self.e_path.get(),self.user)
         
            if(val):
                messagebox.showinfo("MyDiary","Song Added")
                save_to_directory(str(self.e_path.get()),self.user)
                
            else:
                messagebox.showerror("ERROR","Something went wrong,TRY AGAIN")

        self.t.destroy()
        self.root.destroy()

        


from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmpassEntry.delete(0, END)
    check.set(0)
    signup_window.destroy()
    import Signinpage


def connect_database():
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmpassEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif passwordEntry.get() != confirmpassEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please accept Terms and Conditions')
    else:
        try:
            con = pymysql.connect(host="localhost", user='root', password='root')
            mycursor = con.cursor()

        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, please try Again')
            return

        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key, email varchar(50), username varchar(255), password varchar(25))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query = 'select * from data where username=%s'
        mycursor.execute(query, (usernameEntry.get()))

        row = mycursor.fetchone()
        if row!=None:
            messagebox.showerror('Error', 'Username Already exists')
        else:
            query = 'insert into data(email, username, password) values(%s, %s, %s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is successful')
            clear()


def login_page():
    signup_window.destroy()
    import Signinpage


signup_window = Tk()
signup_window.title('signup Page')

background = ImageTk.PhotoImage(file='C://Users//kumar//Downloads//bg .jpg')

bgLabel = Label(signup_window, image=background)
bgLabel.grid()

frame = Frame(signup_window, bg='white')
frame.place(x=554, y=100)

heading = Label(frame, text="CREATE AN ACCOUNT", font=('Microsoft YaHei UI Light', 18, 'bold'), bg='white',
                fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

emailLabel = Label(frame, text="Email", font=('Microsoft YaHei UI Light', 10, 'bold'), bg='white', fg='firebrick1')
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))

emailEntry = Entry(frame, width=30, font=('Microsoft YaHei UI Light', 10, 'bold'), fg='white', bg='firebrick1')
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

usernameLabel = Label(frame, text="Username", font=('Microsoft YaHei UI Light', 10, 'bold'), bg='white',
                      fg='firebrick1')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))

usernameEntry = Entry(frame, width=30, font=('Microsoft YaHei UI Light', 10, 'bold'), fg='white', bg='firebrick1')
usernameEntry.grid(row=4, column=0, sticky='w', padx=25)

passwordLabel = Label(frame, text="Password", font=('Microsoft YaHei UI Light', 10, 'bold'), bg='white',
                      fg='firebrick1')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))

passwordEntry = Entry(frame, width=30, font=('Microsoft YaHei UI Light', 10, 'bold'), fg='white', bg='firebrick1')
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

confirmpassLabel = Label(frame, text="Confirm Password", font=('Microsoft YaHei UI Light', 10, 'bold'), bg='white',
                         fg='firebrick1')
confirmpassLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))

confirmpassEntry = Entry(frame, width=30, font=('Microsoft YaHei UI Light', 10, 'bold'), fg='white', bg='firebrick1')
confirmpassEntry.grid(row=8, column=0, sticky='w', padx=25)

check = IntVar()
termsandcondition = Checkbutton(frame, text='I agree to the Terms & Condition',
                                font=('Microsoft YaHei UI Light', 10, 'bold'), fg='firebrick1', bg='white',
                                activebackground='white', activeforeground='firebrick1', cursor='hand2', variable=check)
termsandcondition.grid(row=9, column=0, sticky='w', pady=10, padx=15)

signupbutton = Button(frame, text='Signup', font=('Open sans', 16, 'bold'), bd=0, bg='firebrick1', fg='white',
                      activebackground='firebrick1', activeforeground='white', width=17, command=connect_database)
signupbutton.grid(row=10, column=0, pady=10)

alreadyaccount = Label(frame, text="Don't have an account?", font=('Open Sans', 9, 'bold'), bg='white', fg='firebrick1')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=25)

Loginbutton = Button(frame, text='Log in', font=('Open sans', 10, 'bold underline'), bd=0, bg='white', cursor='hand2',
                     fg='blue', activebackground='white', activeforeground='blue', command=login_page)
Loginbutton.place(x=170, y=395)

signup_window.mainloop()
